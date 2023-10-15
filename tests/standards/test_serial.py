import contextlib
import time
import unittest
import os
import sys
import shutil
import copy
from unittest.mock import patch



from upsonic import Upsonic, HASHES, Upsonic_Serial
import upsonic


class test_object:
    def exp(self):
        return {"test": "test"}

def my_function():
    return 123


class TestUpsonic(unittest.TestCase):


    def setUp(self):
        Upsonic.database_delete_all()

        self.test_name = "test_user"
        self.Upsonic = Upsonic(self.test_name)

        self.test_vales = [
            "Merhaba",
            123,
            123.213,
            {"test": "test"},
            ["test", "test2"],
            ("test", "test2"),
            True,
            False,
            None,
        ]

    def tearDown(self):
        shutil.rmtree(self.Upsonic.location)
    def test_database_delete_open_databases_pop_Upsonic_Serial(self):
        # Create a test database
        test_db = Upsonic_Serial("test_db")

        # Call the database_delete method

        self.assertIn(
            "test_db" + str(False) + upsonic.core.upsonic.start_location, upsonic.core.upsonic.open_databases
        )
        Upsonic.database_delete("test_db")

        self.assertNotIn(
            "test_db" + str(False) + upsonic.core.upsonic.start_location, upsonic.core.upsonic.open_databases
        )


backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
