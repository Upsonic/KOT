import contextlib
import time
import unittest
import os
import sys
import shutil
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from kot import KOT, HASHES, KOT_serial, KOT_remote
import kot


class test_object:
    def exp(self):
        return {"test": "test"}


class TestKOT(unittest.TestCase):
    def test_bulk_set(self):
        kv_pairs = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
        self.KOT.bulk_set(kv_pairs)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.get("key2"), "value2")
        self.assertEqual(self.KOT.get("key3"), "value3")

    def test_bulk_get(self):
        kv_pairs = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
        self.KOT.bulk_set(kv_pairs)
        keys = ["key1", "key2", "key3"]
        values = self.KOT.bulk_get(keys)
        self.assertEqual(values, {"key1": "value1", "key2": "value2", "key3": "value3"})

    def test_bulk_delete(self):
        kv_pairs = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
        self.KOT.bulk_set(kv_pairs)
        keys = ["key1", "key2", "key3"]
        self.KOT.bulk_delete(keys)
        self.assertEqual(self.KOT.get("key1"), None)
        self.assertEqual(self.KOT.get("key2"), None)
        self.assertEqual(self.KOT.get("key3"), None)

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

    def test_set_get_delete(self):
        self.KOT.set("key1", self.test_vales)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.assertEqual(self.KOT.dict(), {"key1": self.test_vales})
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)

    def test_set_get_delete_location(self):
        self.KOT.set("key1", self.test_vales)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        # create a folder in the location if not exists
        currently_dir = os.getcwd()
        if not os.path.exists(currently_dir + "/test"):
            os.makedirs(currently_dir + "/test")

        false_kot = KOT(self.test_name, folder=currently_dir + "/test")
        self.assertNotEqual(false_kot.get("key1"), self.test_vales)

        true_kot = KOT(self.test_name, folder=currently_dir)
        self.assertEqual(true_kot.get("key1"), self.test_vales)

    def test_set_get_delete_file(self):
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.KOT.set("key1", file="test_file.txt")
        self.assertEqual(os.path.exists("test_file.txt"), False)
        file_path = self.KOT.get("key1")
        with open(file_path, "r") as f:
            self.assertEqual(f.read(), "test")
        self.KOT.delete("key1")
        self.assertEqual(os.path.exists(file_path), False)

    def test_set_get_delete_file_compress(self):
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.KOT.set("key1", file="test_file.txt", compress=True)
        with open(self.KOT.get("key1"), "r") as f:
            self.assertEqual(f.read(), "test")

    def test_set_get_delete_file_encryption(self):
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.KOT.set("key1", file="test_file.txt", encryption_key="Onur")
        with open(self.KOT.get("key1", encryption_key="Onur"), "r") as f:
            self.assertEqual(f.read(), "test")

    def test_set_get_delete_file_compress_encryption(self):
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.KOT.set("key1", file="test_file.txt", compress=True, encryption_key="Onur")
        with open(self.KOT.get("key1", encryption_key="Onur"), "r") as f:
            self.assertEqual(f.read(), "test")

    def test_set_get_delete_file_delete_function(self):
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.KOT.set("key1", file="test_file.txt")
        the_kot_file = self.KOT.get("key1")
        self.assertEqual(os.path.exists(the_kot_file), True)

        self.KOT.delete("key1")

        self.assertEqual(os.path.exists(the_kot_file), False)

    def test_set_get_delete_multiple(self):
        self.KOT.set("key1", self.test_vales)
        self.KOT.set("key2", self.test_vales)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.assertEqual(self.KOT.get("key2"), self.test_vales)
        self.assertEqual(
            self.KOT.dict(), {"key1": self.test_vales, "key2": self.test_vales}
        )
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)
        self.assertNotEqual(self.KOT.get("key2"), None)
        self.KOT.delete("key2")
        self.assertEqual(self.KOT.get("key2"), None)

    def test_set_get_delete_object_compress_encryption(self):
        self.KOT.set(
            "key1", test_object(), compress=True, encryption_key="OnurAtakanULUSOY"
        )
        self.assertEqual(
            self.KOT.get("key1", encryption_key="OnurAtakanULUSOY").exp(),
            test_object().exp(),
        )
        the_dict = self.KOT.dict(encryption_key="OnurAtakanULUSOY")
        the_dict["key1"] = the_dict["key1"].exp()
        self.assertEqual(the_dict, {"key1": test_object().exp()})
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)

    def test_set_invalid_key(self):
        with self.assertRaises(TypeError):
            self.KOT.set(123, "invalid_key")

    def test_set_invalid_file_name(self):
        with self.assertRaises(TypeError):
            self.KOT.set("123", file=13213)

    def test_set_withrkey_get_delete_without_key(self):
        key_name = self.KOT.set_withrkey(self.test_vales)
        self.assertEqual(self.KOT.get(key_name), self.test_vales)

    def test_set_get_delete_all(self):
        self.KOT.set("key1", self.test_vales)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.delete_all()
        self.assertEqual(self.KOT.get("key1"), None)

    def test_set_get_no_compress(self):
        self.KOT.set("key1", self.test_vales, compress=False)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)

    def test_set_get_yes_compress(self):
        self.KOT.set("key1", self.test_vales, compress=True)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)

    def test_set_get_size(self):
        self.KOT.set("key1", self.test_vales, compress=True)
        the_size_of_value = self.KOT.size("key1")
        self.assertGreater(the_size_of_value, 0)

    def test_set_get_compress_test(self):
        big_string = "a" * 1000000

        self.KOT.set("key1", big_string, compress=False)
        the_size_of_not_compress = self.KOT.size_all()
        self.KOT.delete_all()

        self.KOT.set("key1", big_string, compress=True)
        the_size_of_compress = self.KOT.size_all()
        self.KOT.delete_all()

        self.assertGreater(the_size_of_not_compress, the_size_of_compress)

    def test_set_get_compress_test_file_and_dont_remove_file(self):
        big_string = "a" * 1000000
        with open("test_file.txt", "w") as f:
            f.write(big_string)

        self.KOT.set(
            "key1", file="test_file.txt", compress=False, dont_remove_file=True
        )
        the_size_of_not_compress = self.KOT.size_all()
        self.KOT.delete_all()

        self.assertNotEqual(self.KOT.get("key1"), False)

        self.assertEqual(
            self.KOT.set("key1", file="test_file.txt", compress=True), True
        )
        the_size_of_compress = self.KOT.size_all()
        self.KOT.delete_all()

        self.assertGreater(the_size_of_not_compress, the_size_of_compress)

    def test_set_get_compress_test_file_size(self):
        a_db = KOT("test_set_get_compress_test_file_size_1")
        b_db = KOT("test_set_get_compress_test_file_size_2")
        a_db.set("key1", "test_file.txt")
        a_size = a_db.size("key1")

        big_string = "a" * 1000000
        with open("test_file.txt", "w") as f:
            f.write(big_string)
        b_db.set("key1", file="test_file.txt", compress=False, dont_remove_file=True)

        b_size = b_db.size("key1")

        self.assertGreater(b_size, a_size)

    def test_set_get_compress_encyrption_test(self):
        big_string = "a" * 1000000
        self.KOT.set(
            "key1", big_string, compress=True, encryption_key="OnurAtakanULUSOY"
        )
        self.assertEqual(
            self.KOT.get("key1", encryption_key="OnurAtakanULUSOY"), big_string
        )

    def test_set_get_delete_encryption_decryption(self):
        self.KOT.set("key1", self.test_vales, encryption_key="OnurAtakanULUSOY")

        self.assertNotEqual(self.KOT.get("key1"), self.test_vales)

        self.assertEqual(
            self.KOT.get("key1", encryption_key="OnurAtakanULUSOY"), self.test_vales
        )

        self.assertNotEqual(
            self.KOT.get("key1"), self.test_vales
        )


        self.assertNotEqual(self.KOT.dict(), {"key1": self.test_vales})
        self.assertEqual(
            self.KOT.dict(encryption_key="OnurAtakanULUSOY"), {"key1": self.test_vales}
        )
        

    def test_set_get_delete_cache(self):
        self.KOT.set("key1", self.test_vales, cache_policy=30)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=False)
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")

    def test_set_get_delete_function_cache(self):
        self.KOT.set("key1", self.test_vales, cache_policy=30)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.delete("key1")
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")

    def test_set_get_delete_cache_expired(self):
        self.KOT.set("key1", self.test_vales, cache_policy=3)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        time.sleep(4)
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")

    def test_set_get_delete_cache_no_cache(self):
        self.KOT.set("key1", self.test_vales, cache_policy=30)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.KOT.get("key1", no_cache=True), "value1aaaa")

    def test_set_get_delete_cache_clear_cache(self):
        with open("test_file.txt", "w") as f:
            f.write("test")
        self.KOT.set("key1", file="test_file.txt")
        self.assertEqual(os.path.exists("test_file.txt"), False)
        file_path = self.KOT.get("key1")
        with open(file_path, "r") as f:
            self.assertEqual(f.read(), "test")

        self.KOT.set("key1", self.test_vales, cache_policy=15)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.KOT.clear_cache()
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")
        self.assertEqual(os.path.exists(file_path), False)

    def test_backup_restore(self):
        self.KOT.set("key1", self.test_vales)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        backup_location = self.KOT.backup("test_backup")

        another_kp = KOT("backup_test")
        another_kp.delete_all()

        self.assertEqual(another_kp.get("key1"), None)
        result_of_restore = another_kp.restore(backup_location)
        self.assertTrue(result_of_restore)
        self.assertEqual(another_kp.get("key1"), self.test_vales)

    def test_database_list_delete_delete_all(self):
        backup_chdir = os.getcwd()
        the_time = str(int(time.time()))
        os.makedirs(os.path.join(self.KOT.location, the_time))
        kot.kot.start_location = os.path.join(self.KOT.location, the_time)
        database_list = KOT.database_list()

        self.assertEqual(database_list, {})
        a_new_kp = KOT("test_database_list")
        database_list = KOT.database_list()

        self.assertEqual(database_list, {"test_database_list": a_new_kp.location})
        a_new_other_kp = KOT("test_database_list2")
        database_list = KOT.database_list()

        self.assertEqual(
            database_list,
            {
                "test_database_list": a_new_kp.location,
                "test_database_list2": a_new_other_kp.location,
            },
        )

        KOT.database_delete("test_database_list2")

        database_list = KOT.database_list()

        self.assertEqual(database_list, {"test_database_list": a_new_kp.location})

        a_new_other_kp = KOT("test_database_list2")

        KOT.database_delete_all()

        database_list = KOT.database_list()

        self.assertEqual(database_list, {})

        with contextlib.suppress(PermissionError):
            shutil.rmtree(os.path.join(self.KOT.location, the_time))

        kot.kot.start_location = backup_chdir

    def test_database_rename_already(self):
        first_db = KOT("firstdb")
        first_db.set("key1", self.test_vales)
        self.assertEqual(first_db.get("key1"), self.test_vales)
        new_db = KOT("test_database_rename_already")
        new_db.delete_all()
        self.assertNotEqual(new_db.get("key1"), self.test_vales)
        result = KOT.database_rename("firstdb", "test_database_rename_already")
        self.assertFalse(result)

    def test_database_rename_force(self):
        first_db = KOT("firstdb")
        first_db.set("key1", self.test_vales)
        self.assertEqual(first_db.get("key1"), self.test_vales)
        new_db = KOT("test_database_rename_already")
        new_db.delete_all()
        self.assertNotEqual(new_db.get("key1"), self.test_vales)
        result = KOT.database_rename("firstdb", "test_database_rename_already", True)
        self.assertTrue(result)
        self.assertEqual(first_db.get("key1"), None)
        self.assertEqual(new_db.get("key1"), self.test_vales)

    def test_database_rename(self):
        first_db = KOT("firstdb")
        first_db.set("key1", self.test_vales)
        self.assertEqual(first_db.get("key1"), self.test_vales)
        result = KOT.database_rename(
            "firstdb",
            "test_database_rename_already",
        )
        self.assertTrue(result)
        self.assertEqual(first_db.get("key1"), None)
        self.assertEqual(
            KOT("test_database_rename_already").get("key1"), self.test_vales
        )

    def test_debug_function(self):
        kot_instance = KOT("debug_test")
        test_message = "This is a test message for the debug function."
        kot_instance.debug(test_message)
        record = kot_instance.get_all()
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)

    def test_info_function(self):
        kot_instance = KOT("info_test")
        test_message = "This is a test message for the info function."
        kot_instance.info(test_message)
        record = kot_instance.get_all()
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)

    def test_warning_function(self):
        kot_instance = KOT("warning_test")
        test_message = "This is a test message for the warning function."
        kot_instance.warning(test_message)
        record = kot_instance.get_all()
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)
    def test_error_function(self):
        kot_instance = KOT("error_test")
        test_message = "This is a test message for the error function."
        kot_instance.error(test_message)
        record = kot_instance.get_all()
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)

    def test_exception_function(self):
        kot_instance = KOT("exception_test")
        test_message = "This is a test message for the exception function."
        kot_instance.exception(test_message)
        record = kot_instance.get_all()
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)

    def test_dict_no_data(self):
        self.KOT.set("key1", self.test_vales)
        self.assertEqual(self.KOT.get("key1"), self.test_vales)
        self.assertEqual(self.KOT.dict(no_data=True), {"key1": True})
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)

    def test_get_count(self):
        self.KOT.set("key1", self.test_vales)
        count = self.KOT.get_count()
        expected_count = 1
        self.assertEqual(count, expected_count)

    def test_hash_type_error(self):
        with self.assertRaises(ValueError):
            HASHES.get_hash("test", hash_type="md5")

    def test_database_pop(self):
        # Create a database
        customer_db = KOT("customer_database")

        # Add some data to the database
        customer_db.set("John", "Doe")
        customer_db.set("Jane", "Smith")

        # Pop a value from the database
        value = KOT.database_pop("customer_database")

        self.assertEqual(customer_db.get("John"), None)
        self.assertEqual(customer_db.get("Jane"), None)

    def test_database_pop_all(self):
        # Create two databases
        db1 = KOT("database1")
        db2 = KOT("database2")

        # Write key-value pairs to the databases
        db1.set("key1", "value1")
        db2.set("key2", "value2")

        # Delete all data from the databases
        KOT.database_pop_all()

        # Check if the databases are empty
        self.assertEqual(db1.get_all(), {})
        self.assertEqual(db2.get_all(), {})

    def test_wait_system(self):
        the_indicator = os.path.join(self.KOT.location, "indicator")
        self.KOT.set("key1", self.test_vales)

        start_time = int(time.time())
        self.KOT.wait_system("indicator", sleep_amount=3)
        end_time = int(time.time())
        self.assertLess((end_time - start_time), 2)

    def test_wait_system_wait(self):
        the_indicator = os.path.join(self.KOT.location, "indicator")
        self.KOT.set("key1", self.test_vales)
        self.KOT.indicator_creator(the_indicator)

        def deletor():
            self.KOT.indicator_remover(the_indicator)

        start_time = int(time.time())
        self.KOT.wait_system(
            "indicator", sleep_amount=3, after_first_loop_trigger=deletor
        )
        end_time = int(time.time())
        self.assertGreater((end_time - start_time), 2)

    def test_execute_set_get(self):
        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1")
        value = KOT("settings").get("key1")
        value_2 = KOT.execute("GET settings key1")
        self.assertEqual(value, "value1")
        self.assertEqual(value_2, "value1")

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1")
        value = KOT("settings").get_all()
        value_2 = KOT.execute("GET_ALL settings")
        self.assertEqual(value, value_2)

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1 enc")
        value = KOT("settings").get("key1", encryption_key="enc")
        value_2 = KOT.execute("GET settings key1 enc")
        self.assertEqual(value, "value1")
        self.assertEqual(value_2, "value1")

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1 enc True")
        value = KOT("settings").get("key1", encryption_key="enc")
        value_2 = KOT.execute("GET settings key1 enc")
        self.assertEqual(value, "value1")
        self.assertEqual(value_2, "value1")

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1 None True")
        value = KOT("settings").get("key1")
        value_2 = KOT.execute("GET settings key1")
        self.assertEqual(value, "value1")
        self.assertEqual(value_2, "value1")

        a_dict = {"hi": "hello"}
        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1", value=a_dict)
        value = KOT("settings").get("key1")
        self.assertEqual(value, a_dict)

        # Use the execute function to delete the key-value pair
        KOT.execute("DELETE settings key1")
        value = KOT("settings").get("key1")

        # Assert that the key does not exist in the database anymore
        self.assertEqual(value, None)

        # Use the execute function to set a key-value pair
        KOT.execute('SET settings key1 "value1"')
        value = KOT.database_list()
        self.assertIn("settings", value)

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1")
        KOT.execute("DATABASE_DELETE settings")
        value = KOT.database_list()
        value_2 = KOT.execute("DATABASE_LIST")
        self.assertNotIn("settings", value)
        self.assertEqual(value, value_2)

        # Use the execute function to set a key-value pair
        KOT.execute('SET settings key1 "value1"')
        KOT.execute("DATABASE_DELETE_ALL")
        value = KOT.database_list()
        value_2 = KOT.execute("DATABASE_LIST")
        self.assertNotIn("settings", value)
        self.assertEqual(value, value_2)

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1")
        KOT.execute("DATABASE_POP settings")
        self.assertEqual(KOT("settings").get("key1"), None)

        # Use the execute function to set a key-value pair
        KOT.execute("SET settings key1 value1")
        KOT.execute("DATABASE_POP_ALL")
        self.assertEqual(KOT("settings").get("key1"), None)

        big_string = "a" * 1000000
        name_of_db = self.KOT.name
        KOT.execute(f"SET {name_of_db} key1 {big_string} OnurAtakanULUSOY True")
        self.assertEqual(
            self.KOT.get("key1", encryption_key="OnurAtakanULUSOY"), big_string
        )

    def test_database_delete_open_databases_pop_kot_serial(self):
        # Create a test database
        test_db = KOT_serial("test_db")

        # Call the database_delete method

        self.assertIn(
            "test_db" + str(False) + kot.kot.start_location, kot.kot.open_databases
        )
        KOT.database_delete("test_db")

        self.assertNotIn(
            "test_db" + str(False) + kot.kot.start_location, kot.kot.open_databases
        )

    def test_execute_non_string_query(self):
        with self.assertRaises(TypeError):
            KOT.execute(123)

    def test_execute_unsupported_command(self):
        with self.assertRaises(ValueError):
            KOT.execute("UNSUPPORTED_COMMAND")

    def test_set_shortcut(self):
        # Set a key-value pair with the short_cut parameter set to True
        custom_location = "test_location.pickle"
        self.KOT.set("key1", self.test_vales, custom_key_location=custom_location)

        # Retrieve the value
        value = self.KOT.get("key1")
        value_4 = self.KOT.get("key1", raw_dict=True)
        value_2 = self.KOT.get("key1", get_shotcut=True)
        value_3 = self.KOT.get("key1", get_shotcut=True, raw_dict=True)

        # Check if the retrieved value is a reference to the original value
        self.assertEqual(value, self.test_vales)
        self.assertEqual(value_4["value"], self.test_vales)

        self.assertEqual(os.path.exists("test_location.pickle"), True)
        self.assertEqual(value_2, custom_location)
        self.assertEqual(value_3["value"], custom_location)

        self.assertEqual(os.path.exists(custom_location), True)
        self.KOT.delete("key1")
        self.assertEqual(os.path.exists(custom_location), False)

    def test_get_key_none(self):
        self.assertEqual(self.KOT.get_key("dsadasdasdasdadsada"), None)

    def test_decorator_1(self):
        the_db = KOT("test_decorator_1")

        @the_db.save_by_name
        def my_function(param, param_optional="Optional Param"):
            return "Hello, World!"

        my_function("Hi", param_optional="World")
        self.assertEqual(
            the_db.execute("GET test_decorator_1 my_function"),
            [(("Hi",), {"param_optional": "World"}), "Hello, World!"],
        )

    def test_decorator_2(self):
        the_db = KOT("test_decorator_2")
        the_db.execute("DATABASE_POP test_decorator_2")

        @the_db.save_by_name_time
        def my_function(param, param_optional="Optional Param"):
            return "Hello, World!"

        my_function("Hi", param_optional="World")

        result = the_db.execute("GET_ALL test_decorator_2")

        the_time = float(list(result)[0].split("-")[1])
        result = result[list(result)[0]]

        currently_time = float(time.time())

        self.assertAlmostEqual(the_time, currently_time, delta=7)
        self.assertEqual(
            result, [(("Hi",), {"param_optional": "World"}), "Hello, World!"]
        )

    def test_transactional_operations(self):
        the_db = KOT("test_db")
        operations = [("SET", "key1", "value1"), ("GET", "key1"), ("DELETE", "key1")]
        results = the_db.transactional_operations(operations)
        self.assertEqual(results, [True, "value1", True])
        self.assertEqual(the_db.get("key1"), None)

        operations = [
            ("SET", "key1", "value1"),
            ("GET", "key1", None),
        ]
        results = the_db.transactional_operations(operations)
        self.assertEqual(results, [True, "value1"])
        self.assertEqual(the_db.get("key1"), "value1")

    def test_asynchronous_operations(self):
        the_db = KOT("test_db")
        thread = the_db.asynchronous_operations("SET", "key1", "value1")
        thread.join()
        self.assertEqual(the_db.get("key1"), "value1")

        thread = the_db.asynchronous_operations("GET", "key1")
        thread.join()
        self.assertEqual(the_db.get("key1"), "value1")

        thread = the_db.asynchronous_operations("DELETE", "key1")
        thread.join()
        self.assertEqual(the_db.get("key1"), None)

    def test_decorator_3(self):
        the_db = KOT("test_decorator_3")
        the_db.execute("DATABASE_POP test_decorator_3")

        @the_db.save_by_name_time_random
        def my_function(param, param_optional="Optional Param"):
            return "Hello, World!"

        my_function("Hi", param_optional="World")

        result = the_db.execute("GET_ALL test_decorator_3")

        the_time = float(list(result)[0].split("-")[1])
        random = int(list(result)[0].split("-")[2])
        result = result[list(result)[0]]

        currently_time = float(time.time())

        self.assertAlmostEqual(the_time, currently_time, delta=7)
        self.assertEqual(
            result, [(("Hi",), {"param_optional": "World"}), "Hello, World!"]
        )

        self.assertGreater(random, 0)

    @patch('requests.request')
    def test_remote_send_request(self, mock_request):
        # Create an instance of KOT_remote
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        # Define the mock response
        mock_response = mock_request.return_value
        mock_response.json.return_value = {'success': True}

        # Call the _send_request method
        response = kot_remote._send_request('GET', '/endpoint')

        # Check the response
        self.assertEqual(response, {'success': True})

    @patch('requests.request')
    def test_remote_set(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        kot_remote.set('key', 'value')

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["json"],{'database_name': 'database_name', 'key': 'key', 'value': 'value', 'encryption_key': None, 'compress': None})

    @patch('requests.request')
    def test_remote_get(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        kot_remote.get('key', True)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/get'))
        self.assertEqual(mock_send_request._mock_call_args[1]["json"],{'database_name': 'database_name', 'key': 'key', 'compress': True})

    @patch('requests.request')
    def test_remote_delete(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        kot_remote.delete('key')

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/delete'))
        self.assertEqual(mock_send_request._mock_call_args[1]["json"],{'database_name': 'database_name', 'key': 'key'})

    @patch('requests.request')
    def test_remote_list(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        kot_remote.database_list()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/list'))
        self.assertEqual(mock_send_request._mock_call_args[1]["json"],None)


    @patch('requests.request')
    def test_remote_pop(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        kot_remote.database_pop('database_name',)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/database/pop'))
        self.assertEqual(mock_send_request._mock_call_args[1]["json"],{'database_name': 'database_name'})


    @patch('requests.request')
    def test_remote_pop_all(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')

        kot_remote.database_pop_all()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/pop_all'))
        self.assertEqual(mock_send_request._mock_call_args[1]["json"],None)

    @patch('requests.request')
    def test_debug(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the debug function."
        mock_send_request.return_value.json.return_value = {'success': True}
        result = kot_remote.debug(test_message)
        self.assertEqual(result, {'success': True})

    @patch('requests.request')
    def test_info(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the info function."
        mock_send_request.return_value.json.return_value = {'success': True}
        result = kot_remote.info(test_message)
        self.assertEqual(result, {'success': True})

    @patch('requests.request')
    def test_warning(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the warning function."
        mock_send_request.return_value.json.return_value = {'success': True}
        result = kot_remote.warning(test_message)
        self.assertEqual(result, {'success': True})

    @patch('requests.request')
    def test_error(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the error function."
        mock_send_request.return_value.json.return_value = {'success': True}
        result = kot_remote.error(test_message)
        self.assertEqual(result, {'success': True})

    @patch('requests.request')
    def test_exception(self, mock_send_request):
        kot_remote = KOT_remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the exception function."
        mock_send_request.return_value.json.return_value = {'success': True}
        result = kot_remote.exception(test_message)
        self.assertEqual(result, {'success': True})

backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
