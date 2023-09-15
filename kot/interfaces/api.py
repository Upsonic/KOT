#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import threading
import traceback
from waitress import serve
from flask import Flask, request, Response, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from kot import KOT_Serial
from kot import KOT
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv(dotenv_path=".env")

folder = os.environ.get("folder", "")
password = os.environ.get("password", "KOT")
threads = os.environ.get("threads", 4)
access_key = os.environ.get("access_key", "false").lower() == "true"
access_key_folder = os.environ.get("access_key_folder", "")
access_key_lists = os.environ.get("access_key_lists", "")
access_key_lists_cache = int(os.environ.get("access_key_lists_cache", 0))
restricted = os.environ.get("restricted", "")
restricted = restricted.split(",")


rate_limit = os.environ.get("rate_limit", "")
rate_limit = rate_limit.split(",")
key_lenght = os.environ.get("key_lenght", None)
key_lenght = int(key_lenght) if key_lenght is not None else key_lenght
value_lenght = os.environ.get("value_lenght", None)
value_lenght = int(value_lenght) if value_lenght is not None else value_lenght
database_name_lenght = os.environ.get("database_name_lenght", None)
database_name_lenght = (
    int(database_name_lenght)
    if database_name_lenght is not None
    else database_name_lenght
)
maximum_database_amount = os.environ.get("maximum_database_amount", None)
maximum_database_amount = (
    int(maximum_database_amount)
    if maximum_database_amount is not None
    else maximum_database_amount
)
maximum_key_amount = os.environ.get("maximum_key_amount", None)
maximum_key_amount = (
    int(maximum_key_amount) if maximum_key_amount is not None else maximum_key_amount
)
maximum_database_amount_user = os.environ.get("maximum_database_amount_user", None)
maximum_database_amount_user = (
    int(maximum_database_amount_user)
    if maximum_database_amount_user is not None
    else maximum_database_amount_user
)
maximum_key_amount_user = os.environ.get("maximum_key_amount_user", None)
maximum_key_amount_user = (
    int(maximum_key_amount_user)
    if maximum_key_amount_user is not None
    else maximum_key_amount_user
)


database_name_caches = []
key_name_caches = []
database_name_caches_user = {}
key_name_caches_user = {}


limiter = Limiter(get_remote_address, app=app, default_limits=rate_limit)


set_url = "/controller/set"
get_url = "/controller/get"
get_all_url = "/controller/get_all"
delete_url = "/controller/delete"
database_list_url = "/database/list"
database_pop_url = "/database/pop"
database_pop_all_url = "/database/pop_all"
database_rename_url = "/database/rename"
database_delete_url = "/database/delete"
database_delete_all_url = "/database/delete_all"
debug_url = "/controller/debug"
info_url = "/controller/info"
warning_url = "/controller/warning"
error_url = "/controller/error"
exception_url = "/controller/exception"


access_key_database = KOT("access_key_database", folder=access_key_folder)
access_key_database.set(
    "access_keys", access_key_lists, cache_policy=access_key_lists_cache
)


def access_keys():
    a = access_key_database.get("access_keys")
    a = a.split(",")
    if a == [""]:
        a = []
    return a


@app.before_request
def check():
    global password
    global key_lenght
    global value_lenght
    global database_name_lenght
    global maximum_database_amount
    global database_name_caches
    global maximum_key_amount
    global key_name_caches
    global maximum_database_amount_user
    global database_name_caches_user
    global maximum_key_amount_user
    global key_name_caches_user
    global access_key

    auth = request.authorization
    if not auth:
        return Response(
            "Could not verify your access level for that URL. Make basic auth.\n"
            "You have to login with proper credentials",
            401,
            {"WWW-Authenticate": 'Basic realm="Login Required"'},
        )
    if not access_key:
        if auth.username != "" or auth.password != password:
            return Response(
                "Could not verify your access level for that URL. Use password.\n"
                "You have to login with proper credentials",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            )
    else:
        if auth.password not in access_keys():
            return Response(
                "Could not verify your access level for that URL. Use access key.\n"
                "You have to login with proper credentials",
                401,
                {"WWW-Authenticate": 'Basic realm="Access Key Required"'},
            )

    for restrict in restricted:
        if restrict == request.endpoint:
            return Response(
                "Access to this URL is restricted.\n"
                "You do not have the necessary permissions",
                403,  # Change status code to 403 Forbidden
                {"WWW-Authenticate": 'Basic realm="Access Required"'},
            )

    if key_lenght is not None:
        if request.form.get("key") is not None:
            if len(request.form.get("key")) > key_lenght:
                return Response(
                    "Key lenght is restricted.\n" "You do not have the true key lenght",
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="True Key Lenght Required"'},
                )

    if value_lenght is not None:
        if request.form.get("value") is not None:
            if len(request.form.get("value")) > value_lenght:
                return Response(
                    "Value lenght is restricted.\n"
                    "You do not have the true value lenght",
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="True Value Lenght Required"'},
                )

    if database_name_lenght is not None:
        if request.form.get("database_name") is not None:
            if len(request.form.get("database_name")) > database_name_lenght:
                return Response(
                    "Database name lenght is restricted.\n"
                    "You do not have the true database name lenght",
                    403,  # Change status code to 403 Forbidden
                    {
                        "WWW-Authenticate": 'Basic realm="True Database Name Lenght Required"'
                    },
                )

    if maximum_database_amount is not None:
        if request.form.get("database_name") is not None:
            if (
                len(database_name_caches) >= maximum_database_amount
                and request.form.get("database_name") not in database_name_caches
            ):
                return Response(
                    "You cant create more database (SYSTEM).\n"
                    "You do not have right to create more database (SYSTEM)",
                    403,  # Change status code to 403 Forbidden
                    {
                        "WWW-Authenticate": 'Basic realm="Reached Different Database Limit (SYSTEM)"'
                    },
                )
            else:
                if request.form.get("database_name") not in database_name_caches:
                    database_name_caches.append(request.form.get("database_name"))

    if maximum_key_amount is not None:
        if request.form.get("key") is not None:
            if (
                len(key_name_caches) >= maximum_key_amount
                and request.form.get("key") not in key_name_caches
            ):
                return Response(
                    "You cant create more keys.\n"
                    "You do not have right to create more key",
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="Reached Different Key Limit"'},
                )
            else:
                if request.form.get("key") not in key_name_caches:
                    key_name_caches.append(request.form.get("key"))

    if maximum_database_amount_user is not None:
        if request.form.get("database_name") is not None:
            user = request.remote_addr
            if user not in database_name_caches_user:
                database_name_caches_user[user] = []
            if (
                len(database_name_caches_user[user]) >= maximum_database_amount_user
                and request.form.get("database_name")
                not in database_name_caches_user[user]
            ):
                return Response(
                    "You cant create more database (USER).\n"
                    "You do not have right to create more database (USER)",
                    403,  # Change status code to 403 Forbidden
                    {
                        "WWW-Authenticate": 'Basic realm="Reached Different Database Limit (USER)"'
                    },
                )
            else:
                if (
                    request.form.get("database_name")
                    not in database_name_caches_user[user]
                ):
                    database_name_caches_user[user].append(
                        request.form.get("database_name")
                    ) if request.form.get(
                        "database_name"
                    ) not in database_name_caches_user[
                        user
                    ] else None

    if maximum_key_amount_user is not None:
        if request.form.get("key") is not None:
            user = request.remote_addr
            if user not in key_name_caches_user:
                key_name_caches_user[user] = []
            if (
                len(key_name_caches_user[user]) >= maximum_key_amount_user
                and request.form.get("key") not in key_name_caches_user[user]
            ):
                return Response(
                    "You cant create more key (USER).\n"
                    "You do not have right to create more key (USER)",
                    403,  # Change status code to 403 Forbidden
                    {
                        "WWW-Authenticate": 'Basic realm="Reached Different Key Limit (USER)"'
                    },
                )
            else:
                if request.form.get("key") not in key_name_caches_user[user]:
                    key_name_caches_user[user].append(
                        request.form.get("key")
                    ) if request.form.get("key") not in key_name_caches_user[
                        user
                    ] else None


@app.route(set_url, methods=["POST"])
@limiter.exempt
def set():
    database_name = request.form.get("database_name")
    key = request.form.get("key")
    value = request.form.get("value")
    compress = request.form.get("compress")
    encryption_key = request.form.get("encryption_key")
    cache_policy = request.form.get("cache_policy")
    if cache_policy is None:
        cache_policy = 0
    else:
        cache_policy = int(cache_policy)

    database = KOT_Serial(database_name, folder=folder)
    database.set(
        key,
        value,
        compress=compress,
        encryption_key=encryption_key,
        cache_policy=cache_policy,
    )

    return "Data set successfully"


@app.route(get_url, methods=["POST"])
@limiter.exempt
def get():
    database_name = request.form.get("database_name")
    key = request.form.get("key")
    encryption_key = request.form.get("encryption_key")

    database = KOT_Serial(database_name, folder=folder)
    data = database.get(key, encryption_key=encryption_key)

    return jsonify(data)


@app.route(get_all_url, methods=["POST"])
@limiter.exempt
def get_all():
    database_name = request.form.get("database_name")
    encryption_key = request.form.get("encryption_key")
    database = KOT_Serial(database_name, folder=folder)
    datas = database.get_all(encryption_key=encryption_key)

    return jsonify(datas)


@app.route(delete_url, methods=["POST"])
@limiter.exempt
def delete():
    database_name = request.form.get("database_name")
    key = request.form.get("key")

    database = KOT_Serial(database_name, folder=folder)
    database.delete(key)

    return "Data deleted successfully"


@app.route(database_list_url)
def database_list():
    databases = KOT.database_list(folder=folder)

    return jsonify(databases)


@app.route(database_pop_url, methods=["POST"])
@limiter.exempt
def database_pop():
    database_name = request.form.get("database_name")

    KOT.database_pop(database_name, folder=folder)

    return "Database popped successfully"


@app.route(database_pop_all_url, methods=["GET"])
@limiter.exempt
def database_pop_all():
    KOT.database_pop_all(folder=folder)

    return "All database popped successfully"


@app.route(database_rename_url, methods=["POST"])
@limiter.exempt
def database_rename():
    database_name = request.form.get("database_name")
    new_name = request.form.get("new_database_name")

    KOT.database_rename(database_name, new_name, folder=folder)

    return "Database renamed successfully"


@app.route(database_delete_url, methods=["POST"])
@limiter.exempt
def database_delete():
    database_name = request.form.get("database_name")

    KOT.database_delete(database_name, folder=folder)

    return "Database deleted successfully"


@app.route(database_delete_all_url, methods=["GET"])
@limiter.exempt
def database_delete_all():
    database_name = request.form.get("database_name")

    KOT.database_delete_all(folder=folder)

    return "All database deleted successfully"


@app.route(debug_url, methods=["POST"])
@limiter.exempt
def debug():
    message = request.form.get("message")
    database = KOT_Serial("debug", folder=folder)
    database.debug(message)
    return "Debug message logged successfully"


@app.route(info_url, methods=["POST"])
@limiter.exempt
def info():
    message = request.form.get("message")
    database = KOT_Serial("info", folder=folder)
    database.info(message)
    return "Info message logged successfully"


@app.route(warning_url, methods=["POST"])
@limiter.exempt
def warning():
    message = request.form.get("message")
    database = KOT_Serial("warning", folder=folder)
    database.warning(message)
    return "Warning message logged successfully"


@app.route(error_url, methods=["POST"])
@limiter.exempt
def error():
    message = request.form.get("message")
    database = KOT_Serial("error", folder=folder)
    database.error(message)
    return "Error message logged successfully"


@app.route(exception_url, methods=["POST"])
@limiter.exempt
def exception():
    message = request.form.get("message")
    database = KOT_Serial("exception", folder=folder)
    database.exception(message)
    return "Exception message logged successfully"


def API(
    host_data,
    port_data,
):
    host = host_data if host_data is not None else host  # pragma: no cover
    port = port_data if port_data is not None else port  # pragma: no cover
    global threads

    def starter():
        try:
            serve(app, host=host, port=port, threads=threads)  # pragma: no cover
        except:
            traceback.print_exc()

    threading.Thread(target=starter).start()  # pragma: no cover
