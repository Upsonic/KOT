#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from hashlib import sha256
import pickle

import fire

import time
from shutil import move, copy

import mgzip



import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES




def encrypt(key, message):
    def pad(s):
        return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    padded_message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(padded_message.encode())).decode()

def decrypt(key, message):
    def unpad(s):
        return s[:-ord(s[len(s)-1:])]
    message = base64.b64decode(message.encode())
    iv = message[:AES.block_size]
    cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(message[AES.block_size:])).decode()


class KeyPact:

    def __init__(self, name):
        self.name = name
        self.hashed_name = sha256(name.encode()).hexdigest()
        self.location = os.path.join(os.getcwd(), "kp-" + self.hashed_name)


        self.counter = 0

        self.cache = {}

        self.initialize()

    def initialize(self):
        try: 
            os.makedirs(self.location)
        except OSError:
            if not os.path.isdir(self.location):
                raise



    def encrypt(self, key, message):
        def pad(s):
            return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        padded_message = pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(padded_message.encode())).decode()

    def decrypt(self, key, message):
        def unpad(s):
            return s[:-ord(s[len(s)-1:])]
        message = base64.b64decode(message.encode())
        iv = message[:AES.block_size]
        cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(message[AES.block_size:])).decode()

    def set(self, key: str, value, type_of_value: str ="str", compress: bool=False, encryption_key:str="None", cache_policy: int = 0, dont_delete_cache: bool=False) -> str:
        self.counter += 1
        
        


        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())
        key_location_loading = os.path.join(self.location, key_location+".l")
        key_location_loading_indicator = os.path.join(self.location, key_location+".li")

        key_location_reading_indicator = os.path.join(self.location, key_location+".re")
        key_location_compress_indicator = os.path.join(self.location, key_location+".co")

        if encryption_key != "None":
            value = encrypt(encryption_key, value)

        the_dict = {"key":key,"value":value, "type":type}

        if cache_policy != 0:
            the_dict["cache_time"] = time.time()
            the_dict["cache_policy"] = cache_policy
        else:
            if key in self.cache and not dont_delete_cache:
                del self.cache[key]


        if compress:
            # create key_location_compress_indicator
            with open(key_location_compress_indicator, "wb") as f:
                f.write(b"1")

            with mgzip.open(key_location_loading, "wb") as f:
                pickle.dump(the_dict, f)
        
        else:
            with open(key_location_loading, "wb") as f:
                pickle.dump(the_dict, f)




        #Create a file that inform is loading
        with open(key_location_loading_indicator, "wb") as f:
            f.write(b"1")

        while os.path.exists(key_location_reading_indicator):
                    time.sleep(0.25)

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




    def get(self, key: str, custom_key_location: str = None, encryption_key:str="None", no_cache: bool = False):

        if key in self.cache and not no_cache:
            cache_control = False
            currently = time.time()
            last_time = self.cache[key]["cache_time"]
            cache_policy = self.cache[key]["cache_policy"]

            if currently - last_time < cache_policy:
                cache_control = True
            
            if cache_control:
                return self.cache[key]["value"]

        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest()) if custom_key_location == None else custom_key_location

        key_location_loading_indicator = os.path.join(self.location, key_location+".li")
        key_location_reading_indicator = os.path.join(self.location, key_location+".re")
        key_location_compress_indicator = os.path.join(self.location, key_location+".co")

        while os.path.exists(key_location_loading_indicator):
            time.sleep(0.1)



        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None

        total_result = None

        total_result_standart = None

        try:
            
            with open(key_location_reading_indicator, "wb") as f:
                f.write(b"1")
            if os.path.exists(key_location_compress_indicator):
                with mgzip.open(os.path.join(self.location, key_location), "rb") as f:
                    result = pickle.load(f)
                    total_result_standart = result
                    try:
                        total_result = result["value"]
                    except TypeError:
                        total_result = result
            else:
                with open(os.path.join(self.location, key_location), "rb") as f:
                    result = pickle.load(f)
                    total_result_standart = result
                    try:
                        total_result = result["value"]
                    except TypeError:
                        total_result = result

            if encryption_key != "None":
                total_result = decrypt(encryption_key, total_result)

            if "cache_time" in total_result_standart:
                self.cache[key] = total_result_standart

        except EOFError or FileNotFoundError:
            pass

        if os.path.isfile(key_location_reading_indicator):
            os.remove(key_location_reading_indicator)

        return total_result

    def get_key(self, key_location: str):
       
        key_location_compress_indicator = os.path.join(self.location, key_location+".co")
        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None
        total_result = None

        try:
            if os.path.exists(key_location_compress_indicator):
                with mgzip.open(os.path.join(self.location, key_location), "rb") as f:
                    result = pickle.load(f)
                    if not "type" in result:
                        result["type"] = "str"
                    if not "cache_time" in result:
                        result["cache_time"] = 0
                    if not "cache_policy" in result:
                        result["cache_policy"] = 0
                    try:
                        total_result = result["key"]
                    except TypeError:
                        total_result = False            
            else:
                with open(os.path.join(self.location, key_location), "rb") as f:
                    result = pickle.load(f)
                    if not "type" in result:
                        result["type"] = "str"
                    if not "cache_time" in result:
                        result["cache_time"] = 0
                    if not "cache_policy" in result:
                        result["cache_policy"] = 0
                    try:
                        total_result = result["key"]
                    except TypeError:
                        total_result = False
        except EOFError or FileNotFoundError:
            pass            
        return total_result

    def delete(self, key: str):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        key_location_compress_indicator = os.path.join(self.location, key_location+".co")

        try:
            if os.path.exists(key_location_compress_indicator):
                os.remove(os.path.join(self.location, key_location_compress_indicator))
            os.remove(os.path.join(self.location, key_location))
        except OSError:
            pass

    def delete_file(self, key: str):
        

        try:
            os.remove(os.path.join(self.location, self.get_file(key)))
        except OSError:
            pass

        self.delete(key)
        

    def delete_all(self):
        for key in self.dict():
            self.delete(key)

    def dict(self, encryption_key:str="None"):
        result ={}
        for key in os.listdir(self.location):
            if not "." in key:
                the_key = self.get_key(key)
                if not the_key is None:
                    if the_key != False:
                        result_of_key = self.get(the_key, encryption_key=encryption_key)
                        if not result_of_key is None:
                            result[the_key] = result_of_key
        return result

    def size_all(self):
        #Calculate self.location size
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(self.location):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

        return total_size
    
    def size(self, key: str):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        key_location_compress_indicator = os.path.join(self.location, key_location+".co")

        return os.path.getsize(os.path.join(self.location, key_location))


def main():
    fire.Fire(KeyPact)    