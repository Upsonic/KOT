import shutil
import sys
import unittest

import kot
from kot import KOT, KOT_Serial


class test_object:
    def exp(self):
        return {"test": "test"}


def my_function():
    return 123


class TestKOT(unittest.TestCase):
    def setUp(self):
        KOT.database_delete_all()

        self.test_name = "test_user"
        self.KOT = KOT(self.test_name)

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
        shutil.rmtree(self.KOT.location)

    def test_database_delete_open_databases_pop_KOT_Serial(self):
        # Create a test database
        test_db = KOT_Serial("test_db")

        # Call the database_delete method

        self.assertIn(
            "test_db" + str(False) + kot.core.kot.start_location,
            kot.core.kot.open_databases,
        )
        KOT.database_delete("test_db")

        self.assertNotIn(
            "test_db" + str(False) + kot.core.kot.start_location,
            kot.core.kot.open_databases,
        )


backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
