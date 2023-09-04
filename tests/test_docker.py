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

from kot import KOT, HASHES, KOT_Serial, KOT_Remote
import kot
from kot.api import app

import kot


kot.api.password = "pass"
kot.api.folder = os.getcwd()

class test_object:
    def exp(self):
        return {"test": "test"}

def my_function():
    return 123


class TestDocker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.chdir(os.path.join(os.path.dirname(__file__), "..",".."))
        os.system("docker build -t ghcr.io/onuratakan/api:latest -f KOT/docker/local/api/Dockerfile .")
        os.system("docker run -d --name KOT_API -p 5000:5000 ghcr.io/onuratakan/api:latest KOT api pass                --host='0.0.0.0' --port=5000")

        cls.remote = KOT_Remote("TestRemote", "http://localhost:5000", 'pass')


    @classmethod
    def tearDownClass(cls):
        os.system("docker container stop KOT_API")
        os.system("docker container rm KOT_API")

        os.chdir(os.path.join(os.path.dirname(__file__), ".."))



    def test_remote_api_set_get_deletestring(self):
        the = time.time()
        value = f"Value{the}"

        self.remote.set("key", value)

        self.assertEqual(self.remote.get("key",), value)

        self.remote.delete("key")


        self.assertNotEqual(self.remote.get("key"), value)



backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
