#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from hashlib import sha256
import pickle

import fire


class KeyPact:

    def __init__(self, name):
        self.name = name
        self.hashed_name = sha256(name.encode()).hexdigest()
        self.location = os.path.join(os.getcwd(), self.hashed_name)

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
            pickle.dump(value, f)

    def get(self, key: str):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        if not os.path.isfile(os.path.join(self.location, key_location)):
            raise FileNotFoundError("Key not found")

        with open(os.path.join(self.location, key_location), "rb") as f:
            return pickle.load(f)
        
    def delete(self, key: str):
        key_location = os.path.join(self.location, sha256(key.encode()).hexdigest())

        try:
            os.remove(os.path.join(self.location, key_location))
        except OSError:
            pass


def main():
    fire.Fire(KeyPact)    