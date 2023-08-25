---
layout: default
title: API
nav_order: 9
has_children: false
parent: INTERFACES
---

# API

## Start
You can start the API with `api` command but you must give an password.

```console
KOT api <password>
```

Also you can specify the 'host' and 'port'.

```console
KOT api <password> --host localhost --port 5000
```

## Authorization
You must use the API with `Basic Auth`.

- Authorization Type: Basic Auth
  - Username: ""
  - Password: The password that you used for starting API.


## Restriction
You restrict some uses via `--restricted` argument. You can restrict api endpoints via the name and seperate by comma.

```console
KOT api <password> --host localhost --port 5000 --restricted "set, get, delete"
```


## Rate Limit
You can set rate limits via `--rate_limit` argument. Write rate limits like this and seperate by comma.

```console
KOT api <password> --host localhost --port 5000 --rate_limit "5 per hour, 1 per minute"
```

## Key Lenght Limit
You can set key lenght limits via `--key_lenght` argument. Write rate limits like this:

```console
KOT api <password> --host localhost --port 5000 --key_lenght 15
```

this will limit to 15 character.

## Value Lenght Limit
You can set value lenght limits via `--value_lenght` argument. Write rate limits like this:

```console
KOT api <password> --host localhost --port 5000 --value_lenght 15
```

this will limit to 15 character.

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

### `execute`

- Method: POST
- Endpoint: `/execute`

Executes the query.