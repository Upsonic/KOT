---
layout: default
title: EXECUTE FUNCTION
nav_order: 11
has_children: false
---


# Execute Function

The `KOT.execute` function allows users to execute SQL queries in the KOT database. It takes two parameters:

- `query`: A string representing the SQL query.
- `value`: An optional value to be stored in the database.

The function returns the result of the SQL query.

Here are some examples of how to use the `KOT.execute` function:

```python
# Set a key-value pair
KOT.execute("SET my_database my_key my_value")

# Set a key-value pair with custom value type
custom_value = {"hi","Hello"}
KOT.execute("SET my_database my_key", value=custom_value)

# Get a value
value = KOT.execute("GET my_database my_key")
print(value)

# Delete a key
KOT.execute("DELETE my_database my_key")

# Set a key-value pair with encryption
KOT.execute("SET my_database my_key my_value my_encryption_key")

# Get an encrypted value
value = KOT.execute("GET my_database my_key my_encryption_key")
print(value)
```

Note: The `KOT.execute` function raises a `TypeError` if the `query` parameter is not a string, and a `ValueError` if the SQL command is not supported.

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
These commands allow you to delete, pop, and list databases using SQL queries.

