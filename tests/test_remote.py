import contextlib
import time
import unittest
import os
import sys
import shutil
import copy
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from kot import KOT, HASHES, KOT_Serial, KOT_Remote
import kot


class test_object:
    def exp(self):
        return {"test": "test"}

def my_function():
    return 123


class TestRemote(unittest.TestCase):

    @patch('requests.request')
    def test_remote_send_request(self, mock_request):
        # Create an instance of KOT_Remote
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        # Define the mock response
        mock_response = mock_request.return_value
        mock_response.text.return_value = {'success': True}

        # Call the _send_request method
        response = KOT_Remote._send_request('GET', '/endpoint')

        # Check the response
        self.assertEqual(response(), {'success': True})

    @patch('requests.request')
    def test_remote_set(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')



        KOT_Remote.set('key', 'value')

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["database_name"],'database_name')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["key"],'key')
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"]["value"],'value')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["compress"],None)



    @patch('requests.request')
    def test_remote_active(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.active(my_function)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["database_name"],'database_name')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["key"],'my_function')
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"]["value"],'value')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["compress"],None)

    @patch('requests.request')
    def test_remote_active_with_enc(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.active(my_function,  encryption_key="3123213123")

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["database_name"],'database_name')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["key"],'my_function')
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"]["value"],'value')
        self.assertEqual(mock_send_request._mock_call_args[1]["data"]["compress"],None)






    @patch('requests.request')
    def test_remote_set_enc(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.set('key', 'value', encryption_key="dsadad")

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/set'))
        self.assertNotEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name', 'key': 'key', 'value': 'value', 'compress': None})


    @patch('requests.request')
    def test_remote_get(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.get('key', "dsadasda")

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/get'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name', 'key': 'key'})

    @patch('kot.KOT_Remote._send_request')
    def test_remote_get_all(self, mock_send_request):
        backup = copy.copy(KOT.force_encrypt)
        KOT.force_encrypt = None
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        mock_send_request.return_value = '{"success": "True"}'
        the_return = KOT_Remote.get_all()
        self.assertEqual(the_return, {'success': 'True'})
        KOT.force_encrypt = backup


    @patch('requests.request')
    def test_remote_delete_key(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.delete('key')

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/controller/delete'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name', 'key': 'key'})

    @patch('requests.request')
    def test_remote_list(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.database_list()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/list'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],None)


    @patch('requests.request')
    def test_remote_pop(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.database_pop('database_name',)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/database/pop'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name'})


    @patch('requests.request')
    def test_remote_pop_all(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.database_pop_all()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/pop_all'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],None)


    @patch('requests.request')
    def test_remote_delete(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.database_delete('database_name',)

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('POST', 'http://localhost:5000/database/delete'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],{'database_name': 'database_name'})


    @patch('requests.request')
    def test_remote_delete_all(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')

        KOT_Remote.database_delete_all()

        self.assertEqual(mock_send_request._mock_call_args[1]["auth"].__dict__, {'username': '', 'password': 'password'})
        self.assertEqual(mock_send_request._mock_call_args[0],('GET', 'http://localhost:5000/database/delete_all'))
        self.assertEqual(mock_send_request._mock_call_args[1]["data"],None)

    @patch('requests.request')
    def test_remote_debug(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the debug function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_Remote.debug(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_info(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the info function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_Remote.info(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_warning(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the warning function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_Remote.warning(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_error(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the error function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_Remote.error(test_message)
        self.assertEqual(result(), {'success': True})

    @patch('requests.request')
    def test_remote_exception(self, mock_send_request):
        KOT_remote = KOT_Remote("database_name",'http://localhost:5000', 'password')
        test_message = "This is a test message for the exception function."
        mock_send_request.return_value.text.return_value = {'success': True}
        result = KOT_Remote.exception(test_message)
        self.assertEqual(result(), {'success': True})

backup = sys.argv
sys.argv = [sys.argv[0]]
unittest.main(exit=False)
sys.argv = backup
