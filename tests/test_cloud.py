import contextlib
import time
import unittest
import os
import sys
import shutil
import copy
from unittest.mock import patch
from waitress.server import create_server
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from kot import KOT, HASHES, KOT_Serial, KOT_Cloud
import kot

import kot


kot.api.password = "pass"
kot.api.folder = os.getcwd()

class test_object:
    def exp(self):
        return {"test": "test"}

def my_function():
    return 123


class TestCloud(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.remote = KOT_Cloud(KOT.cloud_key())

    def test_remote_api_set_get_deletestring(self):

        

        the = time.time()
        value = f"Value{the}"

        self.remote.set("key", value)

        self.assertEqual(self.remote.get("key",), value)

        self.remote.delete("key")


        self.assertNotEqual(self.remote.get("key"), value)

    def test_remote_api_active(self):
        self.remote.active(my_function)
        self.assertEqual(self.remote.get("my_function")(), 123)

backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
