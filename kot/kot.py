#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from rich import print as rprint
import base64
import contextlib
import hashlib
import os
import time
import traceback
from datetime import datetime
from hashlib import sha256
from shutil import copy
from shutil import make_archive
from shutil import move
from shutil import rmtree
from shutil import unpack_archive
import random
import ast

import copy as cpv



open_databases = {}
start_location = os.getcwd()


class HASHES:
    cache = {}

    @staticmethod
    def get_hash(string: str, hash_type: str = "sha256") -> str:
        if string in HASHES.cache:
            return HASHES.cache[string]
        if hash_type == "sha256":
            result = sha256(string.encode()).hexdigest()
        else:
            raise ValueError("Hash type must be sha256")
        HASHES.cache[string] = result
        return result


class KOT:

    force_compress = False
    force_encrypt = False
    
    @staticmethod
    def cloud_key():
        from cryptography.fernet import Fernet # pragma: no cover
        return "cloud-"+(((Fernet.generate_key()).decode()).replace("-","").replace("_",""))[:30] # pragma: no cover

    def __enter__(self):
        return self  # pragma: no cover
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # pragma: no cover

    def bulk_set(self, kv_pairs: list) -> bool:
        for pair in kv_pairs:
            key, value = pair
            self.set(key, value)
        return True

    def bulk_get(self, keys: list) -> dict:
        result = {}
        for key in keys:
            value = self.get(key)
            if value is not None:
                result[key] = value
        return result

    def bulk_delete(self, keys: list) -> bool:
        for key in keys:
            self.delete(key)
        return True

    @staticmethod
    def execute(query, value: bool = None, folder: str = ""):
        # Check if the input is a string
        if not isinstance(query, str):
            raise TypeError("Query must be a string")
        custom_value = None
        if value is not None:
            custom_value = cpv.copy(value)
        value = None

        # Parse the SQL query
        command, database_name, key, value, encryption_key, compress = KOT.parse_query(
            query
        )

        if custom_value is not None:
            value = custom_value

        if command == "SET":
            result = KOT_Serial(database_name, folder=folder).set(
                key, value, encryption_key=encryption_key, compress=compress
            )
        elif command == "GET":
            result = KOT_Serial(database_name, folder=folder).get(
                key, encryption_key=value
            )
        elif command == "DELETE":
            result = KOT_Serial(database_name, folder=folder).delete(key)
        elif command == "DATABASE_DELETE":
            result = KOT.database_delete(database_name, folder=folder)
        elif command == "DATABASE_DELETE_ALL":
            result = KOT.database_delete_all(folder=folder)
        elif command == "DATABASE_POP":
            result = KOT.database_pop(database_name, folder=folder)
        elif command == "DATABASE_POP_ALL":
            result = KOT.database_pop_all(folder=folder)
        elif command == "DATABASE_LIST":
            result = KOT.database_list(folder=folder)
        elif command == "GET_ALL":
            result = KOT_Serial(database_name, folder=folder).get_all()
        else:
            raise ValueError(f"Unsupported command: {command}")

        # Return the result of the operation
        return result

    def transactional_operations(self, operations: list, folder: str = ""):
        results = []

        for operation in operations:
            if len(operation) == 2:
                command, key = operation
                value = None
            elif len(operation) == 3:
                command, key, value = operation
            if command == "SET":
                result = self.set(key, value)
            elif command == "GET":
                result = self.get(key)
            elif command == "DELETE":
                result = self.delete(key)
            results.append(result)

        return results

    def asynchronous_operations(
        self, operation: str, key: str, value=None, folder: str = ""
    ):
        import threading

        if operation == "SET":
            thread = threading.Thread(target=self.set, args=(key, value))
        elif operation == "GET":
            thread = threading.Thread(target=self.get, args=(key,))
        elif operation == "DELETE":
            thread = threading.Thread(target=self.delete, args=(key,))
        thread.start()
        return thread

    @staticmethod
    def parse_query(query):
        # Parse the SQL query and return the database name, command, key, and value
        parts = query.split()
        command = parts[0]
        database_name = (parts[1]) if len(parts) > 1 else None
        key = (parts[2]) if len(parts) > 2 else None
        value = (parts[3]) if len(parts) > 3 else None
        encryption_key = (parts[4]) if len(parts) > 4 else None
        compress = bool(parts[5]) if len(parts) > 5 else False

        if encryption_key == "None":
            encryption_key = None

        return command, database_name, key, value, encryption_key, compress

    @staticmethod
    def benchmark_set(
        number: int = 10000, compress: bool = False, encryption_key: str = None
    ) -> float:  # pragma: no cover
        compress = True if KOT.force_compress else compress  # pragma: no cover
        encryption_key = (
            KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        )  # pragma: no cover

        my_db = KOT_Serial("KOT-benchmark", self_datas=True)  # pragma: no cover
        start = time.time()  # pragma: no cover
        for i in range(number):  # pragma: no cover
            my_db.set(
                "key" + str(i),
                "value" + str(i),
                compress=compress,
                encryption_key=encryption_key,
            )  # pragma: no cover
        end = time.time()  # pragma: no cover
        my_db.delete_all()  # pragma: no cover
        return end - start  # pragma: no cover

    @staticmethod
    def benchmark_get(
        number: int = 10000,
        compress: bool = False,
        encryption_key: str = None,
        dont_generate: bool = False,
    ) -> float:  # pragma: no cover
        compress = True if KOT.force_compress else compress  # pragma: no cover
        encryption_key = (
            KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        )  # pragma: no cover
        my_db = KOT_Serial("KOT-benchmark", self_datas=True)  # pragma: no cover
        if not dont_generate:  # pragma: no cover
            for i in range(number):  # pragma: no cover
                my_db.set(
                    "key" + str(i),
                    "value" + str(i),
                    compress=compress,
                    encryption_key=encryption_key,
                )  # pragma: no cover
        start = time.time()  # pragma: no cover
        for i in range(number):  # pragma: no cover
            my_db.get("key" + str(i), encryption_key=encryption_key)  # pragma: no cover
        end = time.time()  # pragma: no cover
        my_db.delete_all()  # pragma: no cover
        return end - start  # pragma: no cover

    @staticmethod
    def benchmark_delete(
        number: int = 10000,
        compress: bool = False,
        encryption_key: str = None,
        dont_generate: bool = False,
    ) -> float:  # pragma: no cover
        compress = True if KOT.force_compress else compress  # pragma: no cover
        encryption_key = (
            KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        )  # pragma: no cover
        my_db = KOT_Serial("KOT-benchmark", self_datas=True)  # pragma: no cover
        if not dont_generate:  # pragma: no cover
            for i in range(number):  # pragma: no cover
                my_db.set(
                    "key" + str(i),
                    "value" + str(i),
                    compress=compress,
                    encryption_key=encryption_key,
                )  # pragma: no cover
        start = time.time()  # pragma: no cover
        for i in range(number):  # pragma: no cover
            my_db.delete("key" + str(i))  # pragma: no cover
        end = time.time()  # pragma: no cover
        my_db.delete_all()  # pragma: no cover
        return end - start  # pragma: no cover

    @staticmethod
    def benchmark(
        number: int = 10000, compress: bool = False, encryption_key: str = None
    ) -> float:  # pragma: no cover
        compress = True if KOT.force_compress else compress  # pragma: no cover
        encryption_key = (
            KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        )  # pragma: no cover
        total_time = 0  # pragma: no cover
        total_time += KOT.benchmark_set(
            number, compress, encryption_key
        )  # pragma: no cover
        total_time += KOT.benchmark_get(
            number, compress, encryption_key, dont_generate=True
        )  # pragma: no cover
        total_time += KOT.benchmark_delete(
            number, compress, encryption_key, dont_generate=True
        )  # pragma: no cover
        return total_time  # pragma: no cover

    @staticmethod
    def database_list(folder: str = "") -> dict:
        database_index = KOT_Serial(
            "KOT-database-index", self_datas=True, folder=folder
        )
        return database_index.dict()

    @staticmethod
    def gui(password, folder: str = ""):  # pragma: no cover
        try:
            from .gui import GUI  # pragma: no cover

            GUI(folder, password)  # pragma: no cover
        except ModuleNotFoundError:
            rprint(
                "Warning: GUI module not found. Please install the 'kot_gui' package."
            )  # pragma: no cover

    @staticmethod
    def api(
        password, folder: str = "", host="localhost", port=5000, restricted="", rate_limit="", key_lenght = None, value_lenght = None, database_name_lenght = None, maximum_database_amount = None, maximum_key_amount = None, maximum_database_amount_user = None, maximum_key_amount_user = None, 
    ):  # pragma: no cover
        try:
            from .api import API  # pragma: no cover

            API(folder, password, host, port, restricted, rate_limit, key_lenght, value_lenght, database_name_lenght, maximum_database_amount, maximum_key_amount, maximum_database_amount_user, maximum_key_amount_user)  # pragma: no cover
        except ModuleNotFoundError:
            rprint(
                "Warning: API module not found. Please install the 'kot_api' package."
            )  # pragma: no cover

    @staticmethod
    def web(
        password, folder: str = "", host="localhost", port=5000
    ):  # pragma: no cover
        try:
            from .gui import WEB  # pragma: no cover

            WEB(folder, password, host, port)  # pragma: no cover
        except ModuleNotFoundError:
            rprint(
                "Warning: WEB module not found. Please install the 'kot_web' package."
            )  # pragma: no cover

    @staticmethod
    def database_delete(name: str, folder: str = "") -> bool:
        database_index = KOT_Serial(
            "KOT-database-index", self_datas=True, folder=folder
        )

        the_db = KOT(name, folder=folder, self_datas=True)
        for each_key in the_db.get_all():
            the_db.delete(each_key)
        rmtree(database_index.get(name))

        global open_databases
        folder = start_location if not folder != "" else folder
        if name + str(False) + folder in open_databases:
            open_databases.pop(name + str(False) + folder)
        database_index.delete(name)
        return True

    @staticmethod
    def database_delete_all(folder: str = ""):
        database_index = KOT_Serial(
            "KOT-database-index", self_datas=True, folder=folder
        )

        for each_database in database_index.dict():
            try:
                KOT.database_delete(each_database, folder=folder)
            except:  # pragma: no cover
                return False  # pragma: no cover

    @staticmethod
    def database_pop(name: str, folder: str = "") -> bool:
        database_index = KOT_Serial(
            "KOT-database-index", self_datas=True, folder=folder
        )
        the_db = KOT(name, folder=folder, self_datas=True)
        for each_key in the_db.get_all():
            the_db.delete(each_key)

        return True

    @staticmethod
    def database_pop_all(folder: str = ""):
        database_index = KOT_Serial(
            "KOT-database-index", self_datas=True, folder=folder
        )

        for each_database in database_index.dict():
            try:
                KOT.database_pop(each_database, folder=folder)
            except:  # pragma: no cover
                return False  # pragma: no cover

    @staticmethod
    def database_rename(
        name: str, new_name: str, force: bool = False, folder: str = ""
    ) -> bool:
        if new_name in KOT.database_list() and not force:
            return False
        try:
            first_db = KOT(name, folder=folder)
            location = first_db.backup(".")
            KOT.database_delete(name)
            second_db = KOT(new_name, folder=folder)
            second_db.restore(location)
            os.remove(location)
        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover
            return False
        return True

    def __init__(self, name, self_datas: bool = False, folder: str = "", enable_fast:bool=False):
        self.name = name
        self.hashed_name = HASHES.get_hash(name)
        global start_location
        the_main_folder = start_location if not folder != "" else folder
        self.the_main_folder = the_main_folder
        self.location = os.path.join(the_main_folder, "KOT-" + self.hashed_name)

        if enable_fast:
            import pickle
            self.engine = pickle
        else:
            import dill
            self.engine = dill

        if not self_datas:
            self.open_files_db = KOT_Serial(
                "KOT-open_files_db", self_datas=True, folder=folder
            )
            database_index = KOT_Serial(
                "KOT-database-index", self_datas=True, folder=folder
            )
            database_index.set(self.name, self.location)

        self.counter = 0

        self.cache = {}

        self.initialize()

    def initialize(self):
        try:
            os.makedirs(self.location)
        except OSError:  # pragma: no cover
            if not os.path.isdir(self.location):  # pragma: no cover
                raise  # pragma: no cover

    def clear_cache(self):
        self.cache = {}
        for each_file in self.open_files_db.dict():
            if os.path.exists(each_file):
                os.remove(each_file)
        self.open_files_db.delete_all()

    def encrypt(self, key, message):
        from cryptography.fernet import Fernet
        # Generate a Fernet key from the user-defined key
        fernet_key = base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest())
        # Initialize a Fernet object with the generated key
        fernet = Fernet(fernet_key)
        # Encrypt the message using the encrypt method of the Fernet object
        encrypted_message = fernet.encrypt(self.engine.dumps(message))
        return encrypted_message

    def decrypt(self, key, message):
        from cryptography.fernet import Fernet
        # Initialize a Fernet object with the user-defined key
        fernet = Fernet(base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest()))
        # Decrypt the message using the decrypt method of the Fernet object
        decrypted_message = self.engine.loads(fernet.decrypt(message))
        return decrypted_message

    def set_compress(
        self, key_location_loading, key_location_compress_indicator, the_dict
    ):
        self.indicator_creator(key_location_compress_indicator)
        import mgzip

        with mgzip.open(key_location_loading, "wb") as f:
            self.engine.dump(the_dict, f)

    def set_normal(
        self, key_location_loading, key_location_compress_indicator, the_dict
    ):
        self.indicator_remover(key_location_compress_indicator)

        with open(key_location_loading, "wb") as f:
            self.engine.dump(the_dict, f)

    def get_encryption(self, key_location):
        import mgzip

        result = None
        with mgzip.open(key_location, "rb") as f:
            result = self.engine.load(f)
        return result

    def get_normal(self, key_location):
        result = None
        with open(key_location, "rb") as f:
            result = self.engine.load(f)
        return result

    def read_file(self, file):
        value = None
        with open(file, "rb") as f:
            value = f.read()
        return value

    def set(
        self,
        key: str,
        value=None,
        file: str = "",
        compress: bool = False,
        encryption_key: str = None,
        cache_policy: int = 0,
        dont_delete_cache: bool = False,
        dont_remove_original_file: bool = True,
        custom_key_location: str = "",
        short_cut: bool = False,
    ) -> bool:
        compress = True if KOT.force_compress else compress
        encryption_key = KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        self.counter += 1

        meta = {"type": "value", "file": None, "direct_file": True}

        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(file, str):
            raise TypeError("File must be a string")

        try:
            (
                standart_key_location,
                key_location,
                key_location_loading,
                key_location_reading_indicator,
                key_location_compress_indicator,
                key_location_loading_indicator,
            ) = self.indicator_generator(key, custom_key_location)
            key_location_loading_indicator = key_location_loading_indicator + str(
                random.randint(10000, 99999)
            )

            if custom_key_location != "" and not short_cut:
                self.set(
                    key,
                    value=key_location,
                    file=file,
                    compress=compress,
                    encryption_key=encryption_key,
                    cache_policy=cache_policy,
                    dont_delete_cache=dont_delete_cache,
                    dont_remove_original_file=dont_remove_original_file,
                    short_cut=True,
                )

            if file != "":
                meta["type"] = "file"
                meta["file"] = os.path.join(
                    self.location, key_location + "." + file.split(".")[-1]
                )
                try:
                    if not compress and encryption_key == None:
                        value = ""
                        if not dont_remove_original_file:
                            move(file, meta["file"])
                        else:
                            copy(file, meta["file"])
                    else:
                        meta["direct_file"] = False
                        value = self.read_file(file)
                except:  # pragma: no cover
                    traceback.print_exc()  # pragma: no cover
                    return False  # pragma: no cover

            if encryption_key != None:
                value = self.encrypt(encryption_key, value)

            the_dict = {"key": key, "value": value, "meta": meta, "short_cut": False}
            if short_cut:
                the_dict["short_cut"] = True

            if cache_policy != 0:
                the_dict["cache_time"] = time.time()
                the_dict["cache_policy"] = cache_policy
            else:
                if key in self.cache and not dont_delete_cache:
                    del self.cache[key]

            if compress:
                self.set_compress(
                    key_location_loading, key_location_compress_indicator, the_dict
                )
            else:
                self.set_normal(
                    key_location_loading, key_location_compress_indicator, the_dict
                )

            self.indicator_creator(key_location_loading_indicator)

            self.wait_system(key_location_reading_indicator)

            with contextlib.suppress(FileNotFoundError):
                move(key_location_loading, key_location)

            self.indicator_remover(key_location_loading_indicator)

        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover
            return False  # pragma: no cover

        return True

    def set_withrkey(self, value) -> str:
        key = str(self.counter) + str(time.time())
        try:
            self.set(key, value)
            return key
        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover
            return ""  # pragma: no cover

    def transformer(self, element, encryption_key: str = None):
        if "meta" not in element:
            element["meta"] = {"type": "value"}  # pragma: no cover
        if "short_cut" not in element:
            element["short_cut"] = False  # pragma: no cover
        if element["meta"]["type"] == "value":
            if encryption_key != None:
                return self.decrypt(encryption_key, element["value"])
            return element["value"]
        elif element["meta"]["type"] == "file":
            self.open_files_db.set(element["meta"]["file"], True)
            return element["meta"]["file"]

    def wait_system(
        self,
        indicator: str,
        after_first_loop_trigger=None,
        max_try_number=6,
        sleep_amount=0.25,
    ):
        try_number = 0
        busy = True
        while busy and try_number < max_try_number:
            any_file = False
            try:
                for each_file in os.listdir(self.location):
                    if each_file.startswith(indicator):
                        any_file = True
            except:
                pass
            if not any_file:
                busy = False
                break
            try_number += 1
            time.sleep(sleep_amount)
            if after_first_loop_trigger is not None:
                after_first_loop_trigger()

    def indicator_creator(self, indicator: str):
        with contextlib.suppress(Exception):
            with open(indicator, "wb") as f:
                f.write(b"1")

    def indicator_remover(self, indicator: str):
        if os.path.isfile(indicator):
            with contextlib.suppress(Exception):
                os.remove(indicator)

    def indicator_generator(self, key, custom_key_location):
        standart_key_location = os.path.join(self.location, HASHES.get_hash(key))
        key_location = (
            standart_key_location if custom_key_location == "" else custom_key_location
        )

        key_location_loading = os.path.join(self.location, standart_key_location + ".l")
        key_location_reading_indicator = os.path.join(
            self.location, standart_key_location + ".re"
        )
        key_location_compress_indicator = os.path.join(
            self.location, standart_key_location + ".co"
        )
        key_location_loading_indicator = os.path.join(
            self.location, standart_key_location + ".li"
        )

        return (
            standart_key_location,
            key_location,
            key_location_loading,
            key_location_reading_indicator,
            key_location_compress_indicator,
            key_location_loading_indicator,
        )

    def create_file_of_key(self, total_result_standart, encryption_key):
        # Create the file if there is an compress or encryption situation

        with open(total_result_standart["meta"]["file"], "wb") as f:
            the_bytes = total_result_standart["value"]
            if encryption_key != None:
                the_bytes = self.decrypt(encryption_key, the_bytes)
            f.write(the_bytes)

    def get(
        self,
        key: str,
        custom_key_location: str = "",
        encryption_key: str = None,
        no_cache: bool = False,
        raw_dict: bool = False,
        get_shotcut: bool = False,
    ):
        encryption_key = KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        if key in self.cache and not no_cache:
            cache_control = False
            currently = time.time()
            last_time = self.cache[key]["cache_time"]
            cache_policy = self.cache[key]["cache_policy"]

            if currently - last_time < cache_policy:
                cache_control = True

            if cache_control:
                return self.transformer(self.cache[key])

        (
            standart_key_location,
            key_location,
            key_location_loading,
            key_location_reading_indicator,
            key_location_compress_indicator,
            key_location_loading_indicator,
        ) = self.indicator_generator(key, custom_key_location)
        key_location_reading_indicator = key_location_reading_indicator + str(
            random.randint(10000, 99999)
        )

        self.wait_system(key_location_loading_indicator)

        if not os.path.isfile(key_location):
            return None

        total_result = None
        total_result_standart = None

        try:
            self.indicator_creator(key_location_reading_indicator)

            # Read the file
            if os.path.exists(key_location_compress_indicator):
                result = self.get_encryption(key_location)
            else:
                result = self.get_normal(key_location)

            # Transform the result
            total_result_standart = result
            try:
                total_result = self.transformer(result, encryption_key=encryption_key)
            except TypeError:  # pragma: no cover
                traceback.print_exc()  # pragma: no cover
                total_result = result  # pragma: no cover

            # Add to cache
            if "cache_time" in total_result_standart:
                self.cache[key] = total_result_standart

        except EOFError or FileNotFoundError:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover

        self.indicator_remover(key_location_reading_indicator)

        if total_result_standart["meta"]["type"] == "file":
            if not total_result_standart["meta"]["direct_file"]:
                self.create_file_of_key(total_result_standart, encryption_key)

        # Return the result
        if raw_dict:
            if total_result_standart["short_cut"] and not get_shotcut:
                total_result_standart = self.get(
                    key,
                    custom_key_location=total_result_standart["value"],
                    encryption_key=encryption_key,
                    no_cache=no_cache,
                    raw_dict=raw_dict,
                )

            return total_result_standart

        if total_result_standart["short_cut"] and not get_shotcut:
            total_result = self.get(
                key,
                custom_key_location=total_result_standart["value"],
                encryption_key=encryption_key,
                no_cache=no_cache,
                raw_dict=raw_dict,
            )

        return total_result

    def get_key(self, key_location: str):
        key_location_compress_indicator = os.path.join(
            self.location, key_location + ".co"
        )
        if not os.path.isfile(os.path.join(self.location, key_location)):
            return None
        total_result = None

        try:
            if os.path.exists(key_location_compress_indicator):
                import mgzip

                with mgzip.open(os.path.join(self.location, key_location), "rb") as f:
                    result = self.engine.load(f)
            else:
                with open(os.path.join(self.location, key_location), "rb") as f:
                    result = self.engine.load(f)

            if not "cache_time" in result:
                result["cache_time"] = 0
            if not "cache_policy" in result:
                result["cache_policy"] = 0
            if not "meta" in result:
                result["meta"] = {"type": "value"}  # pragma: no cover
            try:
                total_result = result["key"]
            except TypeError:  # pragma: no cover
                total_result = False  # pragma: no cover

        except EOFError or FileNotFoundError:  # pragma: no cover
            pass  # pragma: no cover
        return total_result

    def get_all(self, encryption_key: str = None):
        return self.dict(encryption_key=encryption_key)

    def get_count(self):
        return len(self.dict(no_data=True))

    def delete(self, key: str) -> bool:
        try:
            if key in self.cache:
                del self.cache[key]
            key_location = os.path.join(self.location, HASHES.get_hash(key))
            key_location_compress_indicator = os.path.join(
                self.location, key_location + ".co"
            )

            with contextlib.suppress(TypeError):
                maybe_file = self.get(key)
                if os.path.exists(maybe_file):
                    os.remove(maybe_file)

            the_get = self.get(key, no_cache=True, raw_dict=True, get_shotcut=True)
            with contextlib.suppress(TypeError):
                if the_get["short_cut"]:
                    os.remove(the_get["value"])

            if os.path.exists(key_location_compress_indicator):
                os.remove(os.path.join(self.location, key_location_compress_indicator))
            if os.path.exists(os.path.join(self.location, key_location)):
                os.remove(os.path.join(self.location, key_location))
        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover
            return False

        return True

    def delete_all(self) -> bool:
        try:
            for key in self.dict():
                self.delete(key)
        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover
            return False
        return True

    def dict(self, encryption_key: str = None, no_data: bool = False):
        encryption_key = KOT.force_encrypt if KOT.force_encrypt != False else encryption_key
        result = {}
        for key in os.listdir(self.location):
            if not "." in key:
                with contextlib.suppress(Exception):
                    the_key = self.get_key(key)
                    if not the_key is None:
                        if the_key != False:
                            result_of_key = (
                                self.get(the_key, encryption_key=encryption_key)
                                if not no_data
                                else True
                            )
                            if not result_of_key is None:
                                result[the_key] = result_of_key
        return result

    def size_all(self) -> int:
        # Calculate self.location size
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(self.location):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

        return total_size

    def size(self, key: str) -> int:
        total_size = 0
        try:
            key_location = os.path.join(self.location, HASHES.get_hash(key))

            key_location_compress_indicator = os.path.join(
                self.location, key_location + ".co"
            )

            if os.path.exists(key_location_compress_indicator):
                total_size += os.path.getsize(
                    os.path.join(self.location, key_location + ".co")
                )

            with contextlib.suppress(TypeError):
                maybe_file = self.get(key)
                if os.path.exists(maybe_file):
                    total_size += os.path.getsize(maybe_file)

            total_size += os.path.getsize(os.path.join(self.location, key_location))
        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover

        return total_size

    def backup(self, backup_location: str) -> str:
        # create a name for backup that a date
        name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        location = os.path.join(backup_location, name)
        make_archive(location, "zip", self.location)
        move(location + ".zip", location + ".KOT")
        return location + ".KOT"

    def restore(self, backup_location: str) -> bool:
        try:
            move(backup_location, backup_location.replace(".KOT", ".zip"))
            backup_location = backup_location.replace(".KOT", ".zip")
            unpack_archive(backup_location, self.location)
            move(backup_location, backup_location.replace(".zip", ".KOT"))
            return True
        except:  # pragma: no cover
            traceback.print_exc()  # pragma: no cover
            return False  # pragma: no cover

    def save_by_name(self, func):
        def runner(*args, **kwargs):
            params = args, kwargs
            result = func(*args, **kwargs)
            value = [params, result]
            key = func.__name__
            try:
                self.set(key, value)
            except Exception as e:  # pragma: no cover
                print(f"Exception occurred in save_by_name: {e}")  # pragma: no cover
            return value

        return runner

    def save_by_name_time(self, func):
        def runner(*args, **kwargs):
            params = args, kwargs
            result = func(*args, **kwargs)
            value = [params, result]
            key = func.__name__ + "-" + str(time.time())
            try:
                self.set(key, value)
            except Exception as e:  # pragma: no cover
                print(f"Exception occurred in save_by_name: {e}")  # pragma: no cover
            return value

        return runner

    def save_by_name_time_random(self, func):
        def runner(*args, **kwargs):
            params = args, kwargs
            result = func(*args, **kwargs)
            value = [params, result]
            key = (
                func.__name__
                + "-"
                + str(time.time())
                + "-"
                + str(random.randint(10000, 99999))
            )
            try:
                self.set(key, value)
            except Exception as e:  # pragma: no cover
                print(f"Exception occurred in save_by_name: {e}")  # pragma: no cover
            return value

        return runner

    def debug(self, message):
        @self.save_by_name_time_random
        def debug_writer():
            rprint("[green]DEBUG:[/green]", message)
            return message

        debug_writer()

    def info(self, message):
        @self.save_by_name_time_random
        def info_writer():
            rprint("[blue]INFO:[/blue]", message)
            return message

        info_writer()

    def warning(self, message):
        @self.save_by_name_time_random
        def warning_writer():
            rprint("[yellow]WARNING:[/yellow]", message)
            return message

        warning_writer()

    def error(self, message):
        @self.save_by_name_time_random
        def error_writer():
            rprint("[red]ERROR:[/red]", message)
            return message

        error_writer()

    def exception(self, message):
        @self.save_by_name_time_random
        def exception_writer():
            rprint("[magenta]EXCEPTION:[/magenta]", message)
            return message

        exception_writer()

    def active(self, _function=None,
        custom_key_location: str = "",
        encryption_key: str = None,
        no_cache: bool = False,
        raw_dict: bool = False,
        get_shotcut: bool = False,compress=None, cache_policy: int = 0, dont_delete_cache: bool = False,):


        def decorate(_function):

            key = _function.__name__
            self.set(key, _function, compress=compress, encryption_key=encryption_key, cache_policy=cache_policy, dont_delete_cache=dont_delete_cache, custom_key_location=custom_key_location)

        if _function == None:
            return decorate
        else:
            decorate(_function)
            return _function



def KOT_Serial(name, self_datas: bool = False, folder: str = ""):
    global start_location
    folder = start_location if not folder != "" else folder

    global open_databases
    name_hash = name + str(self_datas) + folder

    if name_hash in open_databases:
        return open_databases[name_hash]
    else:
        database = KOT(name, self_datas=self_datas, folder=folder)
        open_databases[name_hash] = database
        return database


def main():  # pragma: no cover
    import fire  # pragma: no cover

    fire.Fire(KOT)  # pragma: no cover




class KOT_Remote:


    def __enter__(self):
        return self  # pragma: no cover
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # pragma: no cover

    def __init__(self, database_name, api_url, password):
        import requests
        from requests.auth import HTTPBasicAuth

        self.requests = requests
        self.HTTPBasicAuth = HTTPBasicAuth

        self.api_url = api_url
        self.password = password

        self.database_name = database_name

    def debug(self, message):
        data = {"message": message}
        return self._send_request("POST", "/controller/debug", data)

    def info(self, message):
        data = {"message": message}
        return self._send_request("POST", "/controller/info", data)

    def warning(self, message):
        data = {"message": message}
        return self._send_request("POST", "/controller/warning", data)

    def error(self, message):
        data = {"message": message}
        return self._send_request("POST", "/controller/error", data)

    def exception(self, message):
        data = {"message": message}
        return self._send_request("POST", "/controller/exception", data)

    def _send_request(self, method, endpoint, data=None):
        try:
            response = self.requests.request(
                method,
                self.api_url + endpoint,
                data=data,
                auth=self.HTTPBasicAuth("", self.password),
            )
            response.raise_for_status()
            return response.text
        except self.requests.exceptions.RequestException as e:  # pragma: no cover
            print(f"Error: {e}")  # pragma: no cover
            return None  # pragma: no cover

    def set(self, key, value, encryption_key="a", compress=None):
        compress = True if KOT.force_compress else compress
        encryption_key = KOT.force_encrypt if KOT.force_encrypt != False else encryption_key

        if encryption_key is not None:
            db = KOT_Serial(self.database_name)
            db.set(key, value, encryption_key=encryption_key)
            value = db.get(key)
            db.delete(key)
        
        data = {
            "database_name": self.database_name,
            "key": key,
            "value": value,
            "compress": compress,
        }
        return self._send_request("POST", "/controller/set", data)

    def get(self, key, encryption_key="a"):
        encryption_key = KOT.force_encrypt if KOT.force_encrypt != False else encryption_key

        data = {"database_name": self.database_name, "key": key}
        response = self._send_request("POST", "/controller/get", data)
        
        if not response == "null\n":
            # Decrypt the received value
            if encryption_key is not None:
                db = KOT_Serial(self.database_name)
                db.set(key, response)
                response = db.get(key, encryption_key=encryption_key)
                db.delete(key)
            
            
            return response
        else:
            return None


    def active(self,value=None, encryption_key="a", compress=None):
        def decorate(value):
            key = value.__name__
            self.set(key, value, encryption_key=encryption_key, compress=compress)
        if value == None:
            return decorate
        else:
            decorate(value)
            return value





    def get_all(self, encryption_key="a"):
        encryption_key = KOT.force_encrypt if KOT.force_encrypt != False else encryption_key

        data = {"database_name": self.database_name}
        datas = self._send_request("POST", "/controller/get_all", data)

        datas = json.loads(datas)
        db = KOT_Serial(self.database_name)
        for each in datas:
                db.set(each, datas[each])
                datas[each] = db.get(each, encryption_key=encryption_key)
                db.delete(each)            
        return datas


    def delete(self, key):
        data = {"database_name": self.database_name, "key": key}
        return self._send_request("POST", "/controller/delete", data)

    def database_list(self):
        return ast.literal_eval(self._send_request("GET", "/database/list"))

    def database_pop(self, database_name):
        data = {"database_name": database_name}
        return self._send_request("POST", "/database/pop", data)

    def database_pop_all(self):
        return self._send_request("GET", "/database/pop_all")

    def database_delete(self, database_name):
        data = {"database_name": database_name}
        return self._send_request("POST", "/database/delete", data)

    def database_delete_all(self):
        return self._send_request("GET", "/database/delete_all")



def KOT_Cloud(database_name):
    return KOT_Remote(database_name, 'http://scan.test_net.1.naruno.org:5000', 'onuratakan') # pragma: no cover
