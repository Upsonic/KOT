import contextlib
import time
import unittest
import os
import sys
import shutil
import copy
from unittest.mock import patch
import threading



from upsonic import Upsonic, HASHES, Upsonic_Serial, Upsonic_Remote
import upsonic


class test_object:
    def exp(self):
        return {"test": "test"}

def my_function():
    return 123


class TestDocker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.chdir(os.path.join(os.path.dirname(__file__), "..",".."))
        os.system("docker build -t ghcr.io/upsonic-database/api:latest -f Upsonic/docker/local/api/Dockerfile .")
        os.system("docker run -d --name Upsonic_API -p 5000:5000 ghcr.io/upsonic-database/api:latest Upsonic api --host='0.0.0.0' --port=5000")
        time.sleep(100)

        cls.remote = Upsonic_Remote("TestRemote", "http://localhost:5000", 'Upsonic')


    @classmethod
    def tearDownClass(cls):
        os.system("docker container stop Upsonic_API")
        os.system("docker container rm Upsonic_API")

        os.chdir(os.path.join(os.path.dirname(__file__), ".."))


    def test_remote_api_set_get_deletestring(self):
        the = time.time()
        value = f"Value{the}"

        self.remote.set("key", value)
        time.sleep(1)
        self.assertEqual(self.remote.get("key",), value)

        self.remote.delete("key")


        self.assertNotEqual(self.remote.get("key"), value)

    def test_remote_api_active(self):
        self.remote.active(my_function)
        time.sleep(1)
        self.assertEqual(self.remote.get("my_function")(), 123)



backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
