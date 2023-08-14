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



@app.before_request
def check_auth():
    global password
    auth = request.authorization
    if not auth or (auth.username != "" or auth.password != password):
            return Response('Could not verify your access level for that URL.\n'
                            'You have to login with proper credentials', 401,
                            {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/controller/set', methods=['POST'])
def set_data():
    database_name = request.form.get('database_name')
    key = request.form.get('key')
    value = request.form.get('value')
    compress = request.form.get('compress')
    encryption_key = request.form.get('encryption_key')
    
    database = KOT_serial(database_name, folder=folder)
    database.set(key, value, compress=compress, encryption_key=encryption_key)
    
    return 'Data set successfully'

@app.route('/controller/get', methods=['POST'])
def get_data():
    database_name = request.form.get('database_name')
    key = request.form.get('key')
    encryption_key = request.form.get('encryption_key')
    
    database = KOT_serial(database_name, folder=folder)
    data = database.get(key, encryption_key=encryption_key)
    
    return jsonify(data)

@app.route('/controller/get_all', methods=['POST'])
def get_all():
    database_name = request.form.get('database_name')
    encryption_key = request.form.get('encryption_key')
    if encryption_key is None:
        encryption_key = ""
    database = KOT_serial(database_name, folder=folder)
    datas = database.get_all(encryption_key=encryption_key)

    return jsonify(datas)

@app.route('/controller/delete', methods=['POST'])
def delete_data():
    database_name = request.form.get('database_name')
    key = request.form.get('key')
    
    database = KOT_serial(database_name, folder=folder)
    database.delete(key)
    
    return 'Data deleted successfully'

@app.route('/database/list')
def list_databases():
    databases = KOT.database_list(folder=folder)
    
    return jsonify(databases)

@app.route('/database/pop', methods=['POST'])
def pop_database():
    database_name = request.form.get('database_name')
    
    KOT.database_pop(database_name, folder=folder)
    
    return 'Database popped successfully'

@app.route('/database/pop_all', methods=['POST'])
def pop_all_database():

    
    KOT.database_pop_all(folder=folder)
    
    return 'All database popped successfully'



@app.route('/database/rename', methods=['POST'])
def rename_database():
    database_name = request.form.get('database_name')
    new_name = request.form.get('new_database_name')
    
    KOT.database_rename(database_name, new_name, folder=folder)
    
    return 'Database renamed successfully'

@app.route('/database/delete', methods=['POST'])
def delete_database():
    database_name = request.form.get('database_name')
    
    KOT.database_delete(database_name, folder=folder)
    
    return 'Database deleted successfully'

@app.route('/database/delete_all', methods=['POST'])
def delete_all_database():
    database_name = request.form.get('database_name')
    
    KOT.database_delete_all(folder=folder)
    
    return 'All database deleted successfully'

@app.route('/execute', methods=['POST'])
def execute():
    query = request.form.get('query')
    return jsonify(KOT.execute(query, folder=folder))


def API(folder_data, password_data, host_data, port_data):
    global folder
    global host
    global port
    global password
    folder = folder_data
    host = host_data
    port = port_data
    password = password_data
    serve(app, host=host, port=port)
