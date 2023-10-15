---
layout: default
title: EXECUTE FUNCTION
nav_order: 12
has_children: false
---


# Execute Function

The `Upsonic.execute` function allows users to execute queries in the Upsonic. It takes two parameters:

- `query`: A string representing the query.
- `value`: An optional value to be stored in the database.

The function returns the result of the query.

Here are some examples of how to use the `Upsonic.execute` function:

```python
from upsonic import Upsonic


# Set a key-value pair
Upsonic.execute("SET my_database my_key my_value")

# Get a value
value = Upsonic.execute("GET my_database my_key")
print(value)

# Delete a key
Upsonic.execute("DELETE my_database my_key")

# Set a key-value pair with encryption
Upsonic.execute("SET my_database my_key my_value my_encryption_key")

# Set a key-value pair with encryption and Compressing
Upsonic.execute("SET my_database my_key my_value my_encryption_key True")

# Get an encrypted value
value = Upsonic.execute("GET my_database my_key my_encryption_key")
print(value)

# Set a key-value pair with Compressing
Upsonic.execute("SET my_database my_key my_value None True")

# Get an compressed value
value = Upsonic.execute("GET my_database my_key")
print(value)

# Get all datas of database
value = Upsonic.execute("GET_ALL my_database")
print(value)

```

Note: The `Upsonic.execute` function raises a `TypeError` if the `query` parameter is not a string, and a `ValueError` if the command is not supported.

## Database Commands

The `Upsonic.execute` function also supports commands for managing databases. Here are some examples:

```python
# Delete a specified database
Upsonic.execute("DATABASE_DELETE my_database")

# Delete all databases
Upsonic.execute("DATABASE_DELETE_ALL")

# Pop a specified database
Upsonic.execute("DATABASE_POP my_database")

# Pop all databases
Upsonic.execute("DATABASE_POP_ALL")

# List all databases
databases = Upsonic.execute("DATABASE_LIST")
print(databases)
```
These commands allow you to delete, pop, and list databases using queries.

