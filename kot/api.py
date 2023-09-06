#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from waitress import serve
from flask import Flask, request, Response, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .kot import KOT_Serial
from .kot import KOT

app = Flask(__name__)

""
folder = os.environ.get("folder","")
password = os.environ.get("password","KOT")
access_key = os.environ.get("access_key",False)
access_key_folder = os.environ.get("access_key_folder","")
access_key_lists = os.environ.get("access_key_folder","")
access_key_lists = list(access_key_lists)
access_key_lists_cache = os.environ.get("access_key_lists_cache",0)
restricted = os.environ.get("restricted","")
restricted = list(restricted)
    


rate_limit = os.environ.get("rate_limit","")
key_lenght = os.environ.get("key_lenght",None)
value_lenght = os.environ.get("value_lenght",None)
database_name_lenght = os.environ.get("database_name_lenght",None)
maximum_database_amount = os.environ.get("maximum_database_amount",None)
maximum_key_amount = os.environ.get("maximum_key_amount",None)
maximum_database_amount_user = os.environ.get("maximum_database_amount_user",None)
maximum_key_amount_user = os.environ.get("maximum_key_amount_user",None)



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
access_key_database.set("access_keys", access_key_lists, cache_policy=access_key_lists_cache)
def access_keys():
    return access_key_database.get("access_keys")




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
                    "Could not verify your access level for that URL.\n"
                    "You have to login with proper credentials",
                    401,
                    {"WWW-Authenticate": 'Basic realm="Login Required"'},
                )
    
    elif (auth.username != "" or auth.password != password) and not access_key:
            return Response(
                "Could not verify your access level for that URL.\n"
                "You have to login with proper credentials",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            )

    elif (auth.password not in access_keys()):
            return Response(
                "Could not verify your access level for that URL.\n"
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
                {"WWW-Authenticate": 'Basic realm="Access Required"'}
            )


    if key_lenght is not None:
        if request.form.get("key") is not None:
            if len(request.form.get("key")) > key_lenght:
                return Response(
                    "Key lenght is restricted.\n"
                    "You do not have the true key lenght", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="True Key Lenght Required"'}
                )            

    if value_lenght is not None:
        if request.form.get("value") is not None:
            if len(request.form.get("value")) > value_lenght:
                return Response(
                    "Value lenght is restricted.\n"
                    "You do not have the true value lenght", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="True Value Lenght Required"'}
                )            


    if database_name_lenght is not None:
        if request.form.get("database_name") is not None:
            if len(request.form.get("database_name")) > database_name_lenght:
                return Response(
                    "Database name lenght is restricted.\n"
                    "You do not have the true database name lenght", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="True Database Name Lenght Required"'}
                ) 


    if maximum_database_amount is not None:
        if request.form.get("database_name") is not None:
            if len(database_name_caches) >= maximum_database_amount:
                return Response(
                    "You cant create more database (SYSTEM).\n"
                    "You do not have right to create more database (SYSTEM)", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="Reached Different Database Limit (SYSTEM)"'}
                )
            else:
                if request.form.get("database_name") not in database_name_caches:
                    database_name_caches.append(request.form.get("database_name"))

    if maximum_key_amount is not None:
        if request.form.get("key") is not None:
            if len(key_name_caches) >= maximum_key_amount:
                return Response(
                    "You cant create more keys.\n"
                    "You do not have right to create more key", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="Reached Different Key Limit"'}
                )
            else:
                if request.form.get("key") not in key_name_caches:
                    key_name_caches.append(request.form.get("key"))


    if maximum_database_amount_user is not None:
        if request.form.get("database_name") is not None:
            user = request.remote_addr
            if user not in database_name_caches_user:
                database_name_caches_user[user] = []
            if len(database_name_caches_user[user]) >= maximum_database_amount_user:
                return Response(
                    "You cant create more database (USER).\n"
                    "You do not have right to create more database (USER)", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="Reached Different Database Limit (USER)"'}
                )
            else:
                if request.form.get("database_name") not in database_name_caches_user[user]:
                    database_name_caches_user[user].append(request.form.get("database_name")) if request.form.get("database_name") not in database_name_caches_user[user] else None


    if maximum_key_amount_user is not None:
        if request.form.get("key") is not None:
            user = request.remote_addr
            if user not in key_name_caches_user:
                key_name_caches_user[user] = []
            if len(key_name_caches_user[user]) >= maximum_key_amount_user:
                return Response(
                    "You cant create more key (USER).\n"
                    "You do not have right to create more key (USER)", 
                    403,  # Change status code to 403 Forbidden
                    {"WWW-Authenticate": 'Basic realm="Reached Different Key Limit (USER)"'}
                )
            else:
                if request.form.get("key") not in key_name_caches_user[user]:
                    key_name_caches_user[user].append(request.form.get("key")) if request.form.get("key") not in key_name_caches_user[user] else None


@app.route(set_url, methods=["POST"])
@limiter.limit(rate_limit) 
def set():
    database_name = request.form.get("database_name")
    key = request.form.get("key")
    value = request.form.get("value")
    compress = request.form.get("compress")
    encryption_key = request.form.get("encryption_key")

    database = KOT_Serial(database_name, folder=folder)
    database.set(key, value, compress=compress, encryption_key=encryption_key)

    return "Data set successfully"


@app.route(get_url, methods=["POST"])
@limiter.limit(rate_limit) 
def get():
    database_name = request.form.get("database_name")
    key = request.form.get("key")
    encryption_key = request.form.get("encryption_key")

    database = KOT_Serial(database_name, folder=folder)
    data = database.get(key, encryption_key=encryption_key)

    return jsonify(data)


@app.route(get_all_url, methods=["POST"])
@limiter.limit(rate_limit) 
def get_all():
    database_name = request.form.get("database_name")
    encryption_key = request.form.get("encryption_key")
    database = KOT_Serial(database_name, folder=folder)
    datas = database.get_all(encryption_key=encryption_key)

    return jsonify(datas)


@app.route(delete_url, methods=["POST"])
@limiter.limit(rate_limit) 
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
@limiter.limit(rate_limit) 
def database_pop():
    database_name = request.form.get("database_name")

    KOT.database_pop(database_name, folder=folder)

    return "Database popped successfully"


@app.route(database_pop_all_url, methods=["GET"])
@limiter.limit(rate_limit) 
def database_pop_all():
    KOT.database_pop_all(folder=folder)

    return "All database popped successfully"


@app.route(database_rename_url, methods=["POST"])
@limiter.limit(rate_limit) 
def database_rename():
    database_name = request.form.get("database_name")
    new_name = request.form.get("new_database_name")

    KOT.database_rename(database_name, new_name, folder=folder)

    return "Database renamed successfully"


@app.route(database_delete_url, methods=["POST"])
@limiter.limit(rate_limit) 
def database_delete():
    database_name = request.form.get("database_name")

    KOT.database_delete(database_name, folder=folder)

    return "Database deleted successfully"


@app.route(database_delete_all_url, methods=["GET"])
@limiter.limit(rate_limit) 
def database_delete_all():
    database_name = request.form.get("database_name")

    KOT.database_delete_all(folder=folder)

    return "All database deleted successfully"


@app.route(debug_url, methods=["POST"])
@limiter.limit(rate_limit) 
def debug():
    message = request.form.get("message")
    database = KOT_Serial("debug", folder=folder)
    database.debug(message)
    return "Debug message logged successfully"


@app.route(info_url, methods=["POST"])
@limiter.limit(rate_limit) 
def info():
    message = request.form.get("message")
    database = KOT_Serial("info", folder=folder)
    database.info(message)
    return "Info message logged successfully"


@app.route(warning_url, methods=["POST"])
@limiter.limit(rate_limit) 
def warning():
    message = request.form.get("message")
    database = KOT_Serial("warning", folder=folder)
    database.warning(message)
    return "Warning message logged successfully"


@app.route(error_url, methods=["POST"])
@limiter.limit(rate_limit) 
def error():
    message = request.form.get("message")
    database = KOT_Serial("error", folder=folder)
    database.error(message)
    return "Error message logged successfully"


@app.route(exception_url, methods=["POST"])
@limiter.limit(rate_limit) 
def exception():
    message = request.form.get("message")
    database = KOT_Serial("exception", folder=folder)
    database.exception(message)
    return "Exception message logged successfully"





def API(host_data, port_data,):
    host = host_data if host_data is not None else host  # pragma: no cover
    port = port_data if port_data is not None else port  # pragma: no cover
    serve(app, host=host, port=port)  # pragma: no cover
