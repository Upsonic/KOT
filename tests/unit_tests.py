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

if __name__ == '__main__':
    unittest.main()
