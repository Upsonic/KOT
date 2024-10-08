---
layout: default
title: API
nav_order: 9
has_children: false
parent: INTERFACES
---

# API

## Install
```console
pip3 install kot_api
```

## Start
You can start the API with `api` command, you can specify the 'host' and 'port'.

```console
kot api --host localhost --port 5000
```


## Configuration
Open `.env.template` and made your changes after that save as `.env`


## Authorization
You must use the API with `Basic Auth`.

- Authorization Type: Basic Auth
  - Username: ""
  - Password: The password or access_key.



## Referance

The API provides the following endpoints for interacting with the KOT key-value database.

### `set`

- Method: POST
- Endpoint: `/controller/set`
- Parameters:
  - `database_name`: The name of the database.
  - `key`: The key to set.
  - `value`: The value to set for the key.
  - `encryption_key`: (Optional) The encryption key for the value.
  - `compress`: (Optional) The compression option for the value.
  - 'cache_policy': (Optional) The cache time (seconds)

Sets the value for the given key in the specified database.

### `get`

- Method: POST
- Endpoint: `/controller/get`
- Parameters:
  - `database_name`: The name of the database.
  - `key`: The key to retrieve.
  - `compress`: (Optional) The compression option for the value.

Retrieves the value for the given key from the specified database.

### `get_all`

- Method: POST
- Endpoint: `/controller/get_all`
- Parameters:
  - `database_name`: The name of the database.
  - `encryption_key`: (Optional) The encryption key of values

Retrieves all the data from the specified database.

### `delete`

- Method: POST
- Endpoint: `/controller/delete`
- Parameters:
  - `database_name`: The name of the database.
  - `key`: The key to delete.

Deletes the value for the given key from the specified database.

### `database_list`

- Method: GET
- Endpoint: `/database/list`

Lists all the databases.

### `database_pop`

- Method: POST
- Endpoint: `/database/pop`
- Parameters:
  - `database_name`: The name of the database.

Deletes the specified database.

### `database_pop_all`

- Method: POST
- Endpoint: `/database/pop_all`

Deletes all the databases.

### `database_rename`

- Method: POST
- Endpoint: `/database/rename`
- Parameters:
  - `database_name`: The name of the database.
  - `new_database_name`: The new name for the database.

Renames the specified database.

### `database_delete`

- Method: POST
- Endpoint: `/database/delete`
- Parameters:
  - `database_name`: The name of the database.

Deletes the specified database.

### `database_delete_all`

- Method: POST
- Endpoint: `/database/delete_all`

Deletes all the databases.


### `debug`

- Method: POST
- Endpoint: `/controller/debug`
- Parameters:
  - `message`: The message to log.

Logs a debug message.

### `info`

- Method: POST
- Endpoint: `/controller/info`
- Parameters:
  - `message`: The message to log.

Logs an info message.

### `warning`

- Method: POST
- Endpoint: `/controller/warning`
- Parameters:
  - `message`: The message to log.

Logs a warning message.

### `error`

- Method: POST
- Endpoint: `/controller/error`
- Parameters:
  - `message`: The message to log.

Logs an error message.

### `exception`

- Method: POST
- Endpoint: `/controller/exception`
- Parameters:
  - `message`: The message to log.

Logs an exception message.

