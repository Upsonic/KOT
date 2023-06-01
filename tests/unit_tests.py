import unittest
import os
import shutil
from keypact import KeyPact

class TestKeyPact(unittest.TestCase):

    def setUp(self):
        self.test_data = {"key1": "value1", "key2": 5, "key3": True}
        self.test_name = "test_user"
        self.kp = KeyPact(self.test_name)
        
    def tearDown(self):
        shutil.rmtree(self.kp.location)

    def test_set_get_delete(self):
        self.kp.set("key1", "value1")
        self.assertEqual(self.kp.get("key1"), "value1")
        self.assertEqual(self.kp.dict(), {"key1":"value1"})
        self.kp.delete("key1")
        self.assertEqual(self.kp.get("key1"), None)

    def test_set_get_multiple(self):
        for key, value in self.test_data.items():
            self.kp.set(key, value)

        retrieved_data = {k: self.kp.get(k) for k in self.test_data.keys()}
        self.assertEqual(retrieved_data, self.test_data)

    def test_set_invalid_key(self):
        with self.assertRaises(TypeError):
            self.kp.set(123, "invalid_key")


    def test_set_get_delete_file(self):
        # Create a file to test with
        with open("test_file.txt", "w") as f:
            f.write("test")

        self.kp.set_file("test_file", "test_file.txt")

        self.assertEqual(os.path.exists("test_file.txt"), False)
        the_key = self.kp.get_file("test_file")
        self.assertEqual(os.path.exists(os.path.join(self.kp.location, the_key)), True)


        #Open the file and check the contents
        with open(os.path.join(self.kp.location, self.kp.get_file("test_file")), "r") as f:
            self.assertEqual(f.read(), "test")
        
        # Delete the file
        self.kp.delete_file("test_file")
        self.assertEqual(os.path.exists(os.path.join(self.kp.location, the_key)), False)



    def test_set_withrkey_get_delete_without_key(self):
        key_name = self.kp.set_withrkey("value1")
        self.assertEqual(self.kp.get(key_name), "value1")
        self.assertEqual(self.kp.dict(), {key_name:"value1"})
        self.kp.delete(key_name)
        self.assertEqual(self.kp.get(key_name), None)


    def test_set_withrkey_get_delete_file(self):
        # Create a file to test with
        with open("test_file.txt", "w") as f:
            f.write("test")

        the_file_key = self.kp.set_file_withrkey("test_file.txt")

        self.assertEqual(os.path.exists("test_file.txt"), False)
        the_key = self.kp.get_file(the_file_key)
        self.assertEqual(os.path.exists(os.path.join(self.kp.location, the_key)), True)


        #Open the file and check the contents
        with open(os.path.join(self.kp.location, self.kp.get_file(the_file_key)), "r") as f:
            self.assertEqual(f.read(), "test")
        
        # Delete the file
        self.kp.delete_file(the_file_key)
        self.assertEqual(os.path.exists(os.path.join(self.kp.location, the_key)), False)



    def test_set_get_delete_all(self):
        self.kp.set("key1", "value1")
        self.assertEqual(self.kp.get("key1"), "value1")
        self.assertEqual(self.kp.dict(), {"key1":"value1"})
        self.kp.delete_all()
        self.assertEqual(self.kp.get("key1"), None)
        self.assertEqual(self.kp.dict(), {})

    def test_set_get_no_compress(self):
        self.kp.set("key1", "value1", compress=False)
        self.assertEqual(self.kp.get("key1"), "value1")
        self.assertEqual(self.kp.dict(), {"key1":"value1"})
        self.kp.delete("key1")
        self.assertEqual(self.kp.get("key1"), None)        

    def test_set_get_yes_compress(self):
        self.kp.set("key1", "value1", compress=True)
        self.assertEqual(self.kp.get("key1"), "value1")
        self.assertEqual(self.kp.dict(), {"key1":"value1"})
        self.kp.delete("key1")
        self.assertEqual(self.kp.get("key1"), None)    



    def test_set_get_size(self):
        self.kp.set("key1", "value1", compress=True)
        self.assertEqual(self.kp.get("key1"), "value1")
        self.assertEqual(self.kp.dict(), {"key1":"value1"})
        the_size_of_value = self.kp.size("key1")
        self.kp.delete("key1")
        self.assertEqual(self.kp.get("key1"), None) 

        self.assertGreater(the_size_of_value, 0)

    def test_set_get_compress_test(self):

        #create a big string
        big_string = "a" * 1000000


        self.kp.set("key1", big_string, compress=False)
        self.assertEqual(self.kp.get("key1"), big_string)
        self.assertEqual(self.kp.dict(), {"key1":big_string})
        the_size_of_not_compress = self.kp.size_all()
        self.kp.delete_all()
        
        self.kp.set("key1", big_string, compress=True)
        self.assertEqual(self.kp.get("key1"), big_string)
        self.assertEqual(self.kp.dict(), {"key1":big_string})
        the_size_of_compress = self.kp.size_all()
        self.kp.delete_all()

        self.assertGreater(the_size_of_not_compress, the_size_of_compress)


    def test_set_get_delete_encryption_decryption(self):
        self.kp.set("key1", "value1", encryption_key="OnurAtakanULUSOY")
        self.assertNotEqual(self.kp.get("key1"), "value1")
        self.assertEqual(self.kp.get("key1", encryption_key="OnurAtakanULUSOY"), "value1")
        self.assertNotEqual(self.kp.dict(), {"key1":"value1"})
        self.assertEqual(self.kp.dict(encryption_key="OnurAtakanULUSOY"), {"key1":"value1"})
        self.kp.delete("key1")
        self.assertEqual(self.kp.get("key1"), None)


    def test_set_get_delete_cache(self):
        self.kp.set("key1", "value1", cache_policy=30)
        self.assertEqual(self.kp.get("key1"), "value1")
        self.kp.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertNotEqual(self.kp.get("key1"), "value1")
        self.kp.set("key1", "value1aaaa", dont_delete_cache=True)
        self.assertEqual(self.kp.get("key1"), "value1aaaa")


if __name__ == '__main__':
    unittest.main()
