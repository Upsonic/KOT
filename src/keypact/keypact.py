#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from hashlib import sha256
import pickle

import fire

import time
from shutil import move, copy

class KeyPact:

    def __init__(self, name):
        self.name = name
        self.hashed_name = sha256(name.encode()).hexdigest()
        self.location = os.path.join(os.getcwd(), "kp-" + self.hashed_name)


        self.counter = 0

        self.initialize()

    def initialize(self):
        try: 
            os.makedirs(self.location)
        except OSError:
            if not os.path.isdir(self.location):
                raise

    def set(self, key: str, value, type_of_value="str") -> str:
        self.counter += 1
        
        


        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())
        key_location_loading = os.path.join(self.location, key_location+".l")
        key_location_loading_indicator = os.path.join(self.location, key_location+".li")

        key_location_reading_indicator = os.path.join(self.location, key_location+".re")

        while os.path.exists(key_location_reading_indicator):
            time.sleep(0.25)


        with open(key_location_loading, "wb") as f:
            pickle.dump({"key":key,"value":value, "type":type}, f)


        #Create a file that inform is loading
        with open(key_location_loading_indicator, "wb") as f:
            f.write(b"1")
        move(key_location_loading, key_location)

        #Remove the loading indicator
        os.remove(key_location_loading_indicator)

        return key


    def set_withrkey(self, value, type_of_value="str") -> str:
        key = str(self.counter) + str(time.time())
        return self.set(key, value, type_of_value)


    def set_file(self, key: str, file, dont_remove: bool = False) -> str:

        the_key = self.set(key, file, type_of_value="file")
        key_name = self.get_file(key)
        if not dont_remove:
            move(file, os.path.join(self.location, key_name))
        else:
            copy(file, os.path.join(self.location, key_name))

        return the_key


    def set_file_withrkey(self, file, dont_remove: bool = False) -> str:
        key = str(self.counter) + str(time.time())
        return self.set_file(key, file, dont_remove)


    def get_file(self, key: str, custom_key_location: str = None):
        the_key = self.get(key,custom_key_location)
        return the_key+the_key.split("/")[-1]




    def get(self, key: str, custom_key_location: str = None):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest()) if custom_key_location == None else custom_key_location

        key_location_loading_indicator = os.path.join(self.location, key_location+".li")
        key_location_reading_indicator = os.path.join(self.location, key_location+".re")

        while os.path.exists(key_location_loading_indicator):
            time.sleep(0.1)



        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None

        total_result = None

        try:
            
            with open(key_location_reading_indicator, "wb") as f:
                f.write(b"1")
            with open(os.path.join(self.location, key_location), "rb") as f:
                result = pickle.load(f)
                try:
                    total_result = result["value"]
                except TypeError:
                    total_result = result
        except EOFError or FileNotFoundError:
            pass

        if os.path.isfile(key_location_reading_indicator):
            os.remove(key_location_reading_indicator)

        return total_result

    def get_key(self, key_location: str):
       

        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None
        total_result = None

        try:
            with open(os.path.join(self.location, key_location), "rb") as f:
                result = pickle.load(f)
                if not "type" in result:
                    result["type"] = "str"
                try:
                    total_result = result["key"]
                except TypeError:
                    total_result = False
        except EOFError or FileNotFoundError:
            pass            
        return total_result

    def delete(self, key: str):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        try:
            os.remove(os.path.join(self.location, key_location))
        except OSError:
            pass

    def delete_file(self, key: str):
        

        try:
            os.remove(os.path.join(self.location, self.get_file(key)))
        except OSError:
            pass

        self.delete(key)
        

    def dict(self):
        result ={}
        for key in os.listdir(self.location):
            the_key = self.get_key(key)
            if not the_key is None:
                if the_key != False:
                    result_of_key = self.get(the_key)
                    if not result_of_key is None:
                        result[the_key] = result_of_key
        return result

def main():
    fire.Fire(KeyPact)    