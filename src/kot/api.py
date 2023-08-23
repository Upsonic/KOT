#!/usr/bin/python3
# -*- coding: utf-8 -*-

from waitress import serve
from flask import Flask, request, Response, jsonify
from .kot import KOT_serial
from .kot import KOT

app = Flask(__name__)


folder = None
host = None
port = None
password = None
restricted = None



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
execute_url = "/execute"






@app.before_request
def check_auth():


    global password
    auth = request.authorization
    if not auth or (auth.username != "" or auth.password != password):
        return Response(
            "Could not verify your access level for that URL.\n"
            "You have to login with proper credentials",
            401,
            {"WWW-Authenticate": 'Basic realm="Login Required"'},
        )
    print("restricteds", restricted)
    for restrict in restricted:
        print("endpoitn:", type(request.endpoint) )
        if restrict == request.endpoint:
            return Response(
            "Access to this URL is restricted.\n"
            "You do not have the necessary permissions", 
            403,  # Change status code to 403 Forbidden
            {"WWW-Authenticate": 'Basic realm="Access Required"'}
        )


@app.route(set_url, methods=["POST"])
def set():
    database_name = request.form.get("database_name")
    key = request.form.get("key")
    value = request.form.get("value")
    compress = request.form.get("compress")
    encryption_key = request.form.get("encryption_key")

    database = KOT_serial(database_name, folder=folder)
    database.set(key, value, compress=compress, encryption_key=encryption_key)

    return "Data set successfully"


@app.route(get_url, methods=["POST"])
def get():
    database_name = request.form.get("database_name")
    key = request.form.get("key")
    encryption_key = request.form.get("encryption_key")

    database = KOT_serial(database_name, folder=folder)
    data = database.get(key, encryption_key=encryption_key)

    return jsonify(data)


@app.route(get_all_url, methods=["POST"])
def get_all():
    database_name = request.form.get("database_name")
    encryption_key = request.form.get("encryption_key")
    if encryption_key is None:
        encryption_key = ""
    database = KOT_serial(database_name, folder=folder)
    datas = database.get_all(encryption_key=encryption_key)

    return jsonify(datas)


@app.route(delete_url, methods=["POST"])
def delete():
    database_name = request.form.get("database_name")
    key = request.form.get("key")

    database = KOT_serial(database_name, folder=folder)
    database.delete(key)

    return "Data deleted successfully"


@app.route(database_list_url)
def database_list():
    databases = KOT.database_list(folder=folder)

    return jsonify(databases)


@app.route(database_pop_url, methods=["POST"])
def database_pop():
    database_name = request.form.get("database_name")

    KOT.database_pop(database_name, folder=folder)

    return "Database popped successfully"


@app.route(database_pop_all_url, methods=["POST"])
def database_pop_all():
    KOT.database_pop_all(folder=folder)

    return "All database popped successfully"


@app.route(database_rename_url, methods=["POST"])
def database_rename():
    database_name = request.form.get("database_name")
    new_name = request.form.get("new_database_name")

    KOT.database_rename(database_name, new_name, folder=folder)

    return "Database renamed successfully"


@app.route(database_delete_url, methods=["POST"])
def database_delete():
    database_name = request.form.get("database_name")

    KOT.database_delete(database_name, folder=folder)

    return "Database deleted successfully"


@app.route(database_delete_all_url, methods=["POST"])
def database_delete_all():
    database_name = request.form.get("database_name")

    KOT.database_delete_all(folder=folder)

    return "All database deleted successfully"


@app.route(debug_url, methods=["POST"])
def debug():
    message = request.form.get("message")
    database = KOT_serial("debug", folder=folder)
    database.debug(message)
    return "Debug message logged successfully"


@app.route(info_url, methods=["POST"])
def info():
    message = request.form.get("message")
    database = KOT_serial("info", folder=folder)
    database.info(message)
    return "Info message logged successfully"


@app.route(warning_url, methods=["POST"])
def warning():
    message = request.form.get("message")
    database = KOT_serial("warning", folder=folder)
    database.warning(message)
    return "Warning message logged successfully"


@app.route(error_url, methods=["POST"])
def error():
    message = request.form.get("message")
    database = KOT_serial("error", folder=folder)
    database.error(message)
    return "Error message logged successfully"


@app.route(exception_url, methods=["POST"])
def exception():
    message = request.form.get("message")
    database = KOT_serial("exception", folder=folder)
    database.exception(message)
    return "Exception message logged successfully"


@app.route(execute_url, methods=["POST"])
def execute():
    query = request.form.get("query")
    return jsonify(KOT.execute(query, folder=folder))


def API(folder_data, password_data, host_data, port_data, restricted_data):
    global folder
    global host
    global port
    global password
    global restricted
    folder = folder_data
    host = host_data
    port = port_data
    password = password_data
    restricted = list(restricted_data)
    serve(app, host=host, port=port)
