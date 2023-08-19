---
layout: default
title: EXECUTE FUNCTION
nav_order: 12
has_children: false
---


# Execute Function

The `KOT.execute` function allows users to execute queries in the KOT database. It takes two parameters:

- `query`: A string representing the query.
- `value`: An optional value to be stored in the database.

The function returns the result of the query.

Here are some examples of how to use the `KOT.execute` function:

```python
from kot import KOT


# Set a key-value pair
KOT.execute("SET my_database my_key my_value")

# Get a value
value = KOT.execute("GET my_database my_key")
print(value)

# Delete a key
KOT.execute("DELETE my_database my_key")

# Set a key-value pair with encryption
KOT.execute("SET my_database my_key my_value my_encryption_key")

# Set a key-value pair with encryption and Compressing
KOT.execute("SET my_database my_key my_value my_encryption_key True")

# Get an encrypted value
value = KOT.execute("GET my_database my_key my_encryption_key")
print(value)

# Set a key-value pair with Compressing
KOT.execute("SET my_database my_key my_value None True")

# Get an compressed value
value = KOT.execute("GET my_database my_key")
print(value)

# Get all datas of database
value = KOT.execute("GET_ALL my_database")
print(value)

```

Note: The `KOT.execute` function raises a `TypeError` if the `query` parameter is not a string, and a `ValueError` if the command is not supported.

## Database Commands

The `KOT.execute` function also supports commands for managing databases. Here are some examples:

```python
# Delete a specified database
KOT.execute("DATABASE_DELETE my_database")

# Delete all databases
KOT.execute("DATABASE_DELETE_ALL")

# Pop a specified database
KOT.execute("DATABASE_POP my_database")

# Pop all databases
KOT.execute("DATABASE_POP_ALL")

# List all databases
databases = KOT.execute("DATABASE_LIST")
print(databases)
```
These commands allow you to delete, pop, and list databases using queries.

