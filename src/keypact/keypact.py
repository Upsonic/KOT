#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from hashlib import sha256
import pickle

import fire

import time

class KeyPact:

    def __init__(self, name):
        self.name = name
        self.hashed_name = sha256(name.encode()).hexdigest()
        self.location = os.path.join(os.getcwd(), "kp-" + self.hashed_name)

        self.initialize()

    def initialize(self):
        try: 
            os.makedirs(self.location)
        except OSError:
            if not os.path.isdir(self.location):
                raise

    def set(self, key: str, value):

        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        with open(os.path.join(self.location, key_location), "wb") as f:
            pickle.dump({"key":key,"value":value}, f)

    def get(self, key: str, custom_key_location: str = None):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest()) if custom_key_location == None else custom_key_location

        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None

        total_result = None

        try:
            with open(os.path.join(self.location, key_location), "rb") as f:
                result = pickle.load(f)
                try:
                    total_result = result["value"]
                except TypeError:
                    total_result = result
        except EOFError:
            pass

        return total_result

    def get_key(self, key_location: str):
       

        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None
        total_result = None

        try:
            with open(os.path.join(self.location, key_location), "rb") as f:
                result = pickle.load(f)
                try:
                    total_result = result["key"]
                except TypeError:
                    total_result = False
        except EOFError:
            pass            
        return total_result

    def delete(self, key: str):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        try:
            os.remove(os.path.join(self.location, key_location))
        except OSError:
            pass


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