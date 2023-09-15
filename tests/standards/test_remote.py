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



from kot import KOT, HASHES, KOT_Serial, KOT_Remote
import kot
from kot.interfaces.api import app

import kot


kot.interfaces.api.password = "pass"
kot.interfaces.api.folder = os.getcwd()


def my_function():
    return 123


class TestRemote(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result = create_server(app, host="localhost", port=7777)
        cls.proc = threading.Thread(target=cls.result.run)
        cls.proc.start()

        cls.remote = KOT_Remote("TestRemote", "http://localhost:7777", 'pass')
        cls.local = KOT("TestRemote")

    @classmethod
    def tearDownClass(cls):
        cls.result.close()

    @patch('requests.request')
    def test_remote_send_request(self, mock_request):
        # Create an instance of KOT_Remote
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        # Define the mock response
        mock_response = mock_request.return_value
        mock_response.text.return_value = {'success': True}

        # Call the _send_request method
        response = KOT_remote._send_request('GET', '/endpoint')

        # Check the response
        self.assertEqual(response(), {'success': True})

    @patch('requests.request')
    def test_remote_set(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')



        KOT_remote.set('key', 'value')

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["database_name"],'database_name')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["key"],'key')
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"]["value"],'value')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["compress"],None)



    @patch('requests.request')
    def test_remote_active(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.active(my_function)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["database_name"],'database_name')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["key"],'my_function')
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"]["value"],'value')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["compress"],None)

    @patch('requests.request')
    def test_remote_active_with_enc(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.active(my_function,  encryption_key="3123213123")

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["database_name"],'database_name')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["key"],'my_function')
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"]["value"],'value')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["compress"],None)






    @patch('requests.request')
    def test_remote_set_enc(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.set('key', 'value', encryption_key="dsadad")

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name', 'key': 'key', 'value': 'value', 'compress': None})


    @patch('requests.request')
    def test_remote_get(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.get('key', "dsadasda")

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/get'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name', 'key': 'key'})

    @patch('kot.remote.controller.KOT_Remote._send_request')
    def test_remote_get_all(self, mock_send_request):
        backup = copy.copy(KOT.force_encrypt)
        KOT.force_encrypt = None
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        mock_send_request.return_value = '{"success": "True"}'
        the_return = KOT_remote.get_all()
        self.assertEqual(the_return, {'success': 'True'})
        KOT.force_encrypt = backup


    @patch('requests.request')
    def test_remote_delete_key(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.delete('key')

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/delete'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name', 'key': 'key'})


    @patch('requests.request')
    def test_remote_pop(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.database_pop('database_name',)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/database/pop'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name'})


    @patch('requests.request')
    def test_remote_pop_all(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.database_pop_all()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/pop_all'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],None)


    @patch('requests.request')
    def test_remote_delete(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.database_delete('database_name',)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/database/delete'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name'})


    @patch('requests.request')
    def test_remote_delete_all(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_remote.database_delete_all()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/delete_all'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],None)

    @patch('requests.request')
    def test_remote_debug(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the debug function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_remote.debug(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_info(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the info function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_remote.info(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_warning(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the warning function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_remote.warning(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_error(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the error function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_remote.error(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_exception(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the exception function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_remote.exception(test_message)
        self.assertEqual(result(), {'success': True})






    ## WITH API

    def test_remote_api_set_get_deletestring(self):
        the = time.time()
        value = f"Value{the}"

        self.remote.set("key", value)
        self.assertEqual(self.local.get("key", encryption_key="a"), value)
        self.assertEqual(self.remote.get("key",), value)

        self.remote.delete("key")

        self.assertNotEqual(self.local.get("key", encryption_key="a"), value)
        self.assertNotEqual(self.remote.get("key"), value)

    def test_remote_api_set_get_compex(self):
        the = time.time()
        value = my_function

        self.remote.set("key", value)
        self.assertEqual(self.local.get("key", encryption_key="a"), value)
        self.assertEqual(self.remote.get("key",), value)


    def test_remote_api_active(self):
        self.remote.active(my_function)
        self.assertEqual(self.remote.get("my_function")(), 123)


    def test_remote_api_get_all(self):
        self.assertEqual(self.remote.get_all(), self.local.get_all(encryption_key="a"))

    def test_remote_api_database_list(self):   
        self.assertEqual(self.remote.database_list()["TestRemote"], self.local.database_list()["TestRemote"])

    def test_remote_api_database_delete(self):
        KOT("aaaaaaa")
        self.assertIn("aaaaaaa", self.local.database_list())
        self.remote.database_delete("aaaaaaa")
        self.assertNotIn("aaaaaaa", self.local.database_list())

    def test_remote_api_database_delete_all(self):
        KOT("aaaaaaa")
        self.assertIn("aaaaaaa", self.local.database_list())
        self.remote.database_delete_all()
        self.assertNotIn("aaaaaaa", self.local.database_list())
        self.assertEqual(len(self.remote.database_list()), 0)
        KOT("TestRemote")


    def test_remote_api_database_pop(self):
        KOT("aaaaaaa").set("sdad", "32413")
        KOT("aaaaaaaaaa").set("sdad", "32413")
        self.assertGreater(len(KOT("aaaaaaa").get_all()), 0)
        self.assertGreater(len(KOT("aaaaaaaaaa").get_all()), 0)
        self.remote.database_pop("aaaaaaaaaa")
        self.assertGreater(len(KOT("aaaaaaa").get_all()), 0)
        self.assertEqual(len(KOT("aaaaaaaaaa").get_all()), 0)


    def test_remote_api_database_pop_all(self):
        KOT("aaaaaaa").set("sdad", "32413")
        KOT("aaaaaaaaaa").set("sdad", "32413")
        self.assertGreater(len(KOT("aaaaaaa").get_all()), 0)
        self.assertGreater(len(KOT("aaaaaaaaaa").get_all()), 0)
        self.remote.database_pop_all()
        self.assertEqual(len(KOT("aaaaaaa").get_all()), 0)
        self.assertEqual(len(KOT("aaaaaaaaaa").get_all()), 0)






    def test_info_function(self):
        kot_instance = KOT_Remote("info", "http://localhost:7777", 'pass')
        test_message = "This is a test message for the info function."
        kot_instance.info(test_message)
        record = kot_instance.get_all(encryption_key=None)
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)

    def test_warning_function(self):
        kot_instance = KOT_Remote("warning", "http://localhost:7777", 'pass')
        test_message = "This is a test message for the warning function."
        kot_instance.warning(test_message)
        record = kot_instance.get_all(encryption_key=None)
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)
    def test_error_function(self):
        kot_instance = KOT_Remote("error", "http://localhost:7777", 'pass')
        test_message = "This is a test message for the error function."
        kot_instance.error(test_message)
        record = kot_instance.get_all(encryption_key=None)
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)

    def test_exception_function(self):
        kot_instance = KOT_Remote("exception", "http://localhost:7777", 'pass')
        test_message = "This is a test message for the exception function."
        kot_instance.exception(test_message)
        record = kot_instance.get_all(encryption_key=None)
        logged_message = record[list(record)[0]][1]
        self.assertEqual(logged_message, test_message)




backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
