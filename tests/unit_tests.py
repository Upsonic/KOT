import contextlib
import time
import unittest
import os
import shutil
from kot import KOT

class TestKOT(unittest.TestCase):

    def setUp(self):
        self.test_data = {"key1": "value1", "key2": 5, "key3": True}
        self.test_name = "test_user"
        self.KOT = KOT(self.test_name)
        
    def tearDown(self):
        shutil.rmtree(self.KOT.location)

    def test_set_get_delete(self):
        self.KOT.set("key1", "value1")
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.dict(), {"key1":"value1"})
        self.assertEqual(self.KOT.get_key_type("key1"), "str")
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)

    def test_set_get_multiple(self):
        for key, value in self.test_data.items():
            self.KOT.set(key, value)

        retrieved_data = {k: self.KOT.get(k) for k in self.test_data.keys()}
        self.assertEqual(retrieved_data, self.test_data)

    def test_set_invalid_key(self):
        with self.assertRaises(TypeError):
            self.KOT.set(123, "invalid_key")


    def test_set_get_delete_file_size(self):
        # Create a file to test with
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.KOT.set_file("test_file", "test_file.txt")

        self.assertEqual(os.path.exists("test_file.txt"), False)
        the_key = self.KOT.get_file("test_file")
        self.assertEqual(os.path.exists(os.path.join(self.KOT.location, the_key)), True)


        #Open the file and check the contents
        with open(os.path.join(self.KOT.location, self.KOT.get_file("test_file")), "r") as f:
            self.assertEqual(f.read(), "test")
        
        #type
        self.assertEqual(self.KOT.get_key_type("test_file"), "file")

        #check the size
        self.assertGreater(self.KOT.size_file("test_file"), 0)

        # Delete the file
        self.KOT.delete_file("test_file")
        self.assertEqual(os.path.exists(os.path.join(self.KOT.location, the_key)), False)



    def test_set_withrkey_get_delete_without_key(self):
        key_name = self.KOT.set_withrkey("value1")
        self.assertEqual(self.KOT.get(key_name), "value1")
        self.assertEqual(self.KOT.dict(), {key_name:"value1"})
        self.KOT.delete(key_name)
        self.assertEqual(self.KOT.get(key_name), None)


    def test_set_withrkey_get_delete_file(self):
        # Create a file to test with
        with open("test_file.txt", "w") as f:
            f.write("test")

        the_file_key = self.KOT.set_file_withrkey("test_file.txt")

        self.assertEqual(os.path.exists("test_file.txt"), False)
        the_key = self.KOT.get_file(the_file_key)
        self.assertEqual(os.path.exists(os.path.join(self.KOT.location, the_key)), True)


        #Open the file and check the contents
        with open(os.path.join(self.KOT.location, self.KOT.get_file(the_file_key)), "r") as f:
            self.assertEqual(f.read(), "test")
        
        # Delete the file
        self.KOT.delete_file(the_file_key)
        self.assertEqual(os.path.exists(os.path.join(self.KOT.location, the_key)), False)



    def test_set_get_delete_all(self):
        self.KOT.set("key1", "value1")
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.dict(), {"key1":"value1"})
        self.KOT.delete_all()
        self.assertEqual(self.KOT.get("key1"), None)
        self.assertEqual(self.KOT.dict(), {})

    def test_set_get_no_compress(self):
        self.KOT.set("key1", "value1", compress=False)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.dict(), {"key1":"value1"})
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)        

    def test_set_get_yes_compress(self):
        self.KOT.set("key1", "value1", compress=True)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.dict(), {"key1":"value1"})
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)    



    def test_set_get_size(self):
        self.KOT.set("key1", "value1", compress=True)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.dict(), {"key1":"value1"})
        the_size_of_value = self.KOT.size("key1")
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None) 

        self.assertGreater(the_size_of_value, 0)

    def test_set_get_compress_test(self):

        #create a big string
        big_string = "a" * 1000000


        self.KOT.set("key1", big_string, compress=False)
        self.assertEqual(self.KOT.get("key1"), big_string)
        self.assertEqual(self.KOT.dict(), {"key1":big_string})
        the_size_of_not_compress = self.KOT.size_all()
        self.KOT.delete_all()
        
        self.KOT.set("key1", big_string, compress=True)
        self.assertEqual(self.KOT.get("key1"), big_string)
        self.assertEqual(self.KOT.dict(), {"key1":big_string})
        the_size_of_compress = self.KOT.size_all()
        self.KOT.delete_all()

        self.assertGreater(the_size_of_not_compress, the_size_of_compress)


    def test_set_get_compress_encyrption_test(self):

        #create a big string
        big_string = "a" * 1000000

        
        self.KOT.set("key1", big_string, compress=True, encryption_key="OnurAtakanULUSOY")
        self.assertEqual(self.KOT.get("key1", encryption_key="OnurAtakanULUSOY"), big_string)
        self.KOT.delete_all()



    def test_set_get_delete_encryption_decryption(self):
        self.KOT.set("key1", "value1", encryption_key="OnurAtakanULUSOY")
        self.assertNotEqual(self.KOT.get("key1"), "value1")
        self.assertEqual(self.KOT.get("key1", encryption_key="OnurAtakanULUSOY"), "value1")
        self.assertNotEqual(self.KOT.dict(), {"key1":"value1"})
        self.assertEqual(self.KOT.dict(encryption_key="OnurAtakanULUSOY"), {"key1":"value1"})
        self.KOT.delete("key1")
        self.assertEqual(self.KOT.get("key1"), None)


    def test_set_get_delete_cache(self):
        self.KOT.set("key1", "value1", cache_policy=30)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=False)
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")


    def test_set_get_delete_cache_expired(self):
        self.KOT.set("key1", "value1", cache_policy=3)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        time.sleep(4)
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")

    def test_set_get_delete_cache_no_cache(self):
        self.KOT.set("key1", "value1", cache_policy=30)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.KOT.get("key1", no_cache=True), "value1aaaa")

    def test_set_get_delete_cache_clear_cache(self):
        self.KOT.set("key1", "value1", cache_policy=15)
        self.assertEqual(self.KOT.get("key1"), "value1")
        self.KOT.set("key1", "value1aaaa", dont_delete_cache=True)
        self.KOT.clear_cache()
        self.assertEqual(self.KOT.get("key1"), "value1aaaa")


    def test_backup_restore(self):
        self.KOT.set("key1", "value1")
        self.assertEqual(self.KOT.get("key1"), "value1")
        backup_location = self.KOT.backup("test_backup")

        another_kp = KOT("backup_test")
        another_kp.delete_all()

        self.assertEqual(another_kp.get("key1"), None)
        result_of_restore = another_kp.restore(backup_location)
        self.assertTrue(result_of_restore)
        self.assertEqual(another_kp.get("key1"), "value1")


    def test_database_list_delete_delete_all(self):
        backup_chdir = os.getcwd()
        the_time = str(int(time.time()))
        os.makedirs(os.path.join(self.KOT.location, the_time))
        os.chdir(os.path.join(self.KOT.location, the_time))
        database_list = KOT.database_list()

        self.assertEqual(database_list, {})
        a_new_kp = KOT("test_database_list")
        database_list = KOT.database_list()

        self.assertEqual(database_list, {"test_database_list":a_new_kp.location})
        a_new_other_kp = KOT("test_database_list2")
        database_list = KOT.database_list()

        self.assertEqual(database_list, {"test_database_list":a_new_kp.location, "test_database_list2":a_new_other_kp.location})

        KOT.database_delete("test_database_list2")

        database_list = KOT.database_list()

        self.assertEqual(database_list, {"test_database_list":a_new_kp.location})

        a_new_other_kp = KOT("test_database_list2")


        KOT.database_delete_all()

        database_list = KOT.database_list()

        self.assertEqual(database_list, {})

        with contextlib.suppress(PermissionError):
            shutil.rmtree(os.path.join(self.KOT.location, the_time))


        os.chdir(backup_chdir)


    def test_database_rename_already(self):
        first_db = KOT("firstdb")
        first_db.set("key1", "value1")
        self.assertEqual(first_db.get("key1"), "value1")
        new_db = KOT("test_database_rename_already")
        new_db.delete_all()
        self.assertNotEqual(new_db.get("key1"), "value1")
        result = KOT.database_rename("firstdb", "test_database_rename_already")
        self.assertFalse(result)


    def test_database_rename_force(self):
        first_db = KOT("firstdb")
        first_db.set("key1", "value1")
        self.assertEqual(first_db.get("key1"), "value1")
        new_db = KOT("test_database_rename_already")
        new_db.delete_all()
        self.assertNotEqual(new_db.get("key1"), "value1")
        result = KOT.database_rename("firstdb", "test_database_rename_already", True)
        self.assertTrue(result)
        self.assertEqual(first_db.get("key1"), None)
        self.assertEqual(new_db.get("key1"), "value1")
        
    def test_database_rename(self):
        first_db = KOT("firstdb")
        first_db.set("key1", "value1")
        self.assertEqual(first_db.get("key1"), "value1")
        KOT.database_delete("test_database_rename_already")
        result = KOT.database_rename("firstdb", "test_database_rename_already",)
        self.assertTrue(result)
        self.assertEqual(first_db.get("key1"), None)
        self.assertEqual(KOT("test_database_rename_already").get("key1"), "value1")

if __name__ == '__main__':
    unittest.main()
