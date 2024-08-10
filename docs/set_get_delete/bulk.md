---
layout: default
title: Bulk Operations
nav_order: 5
has_children: false
parent: SET GET DELETE
---

# Bulk Operations
In this section we will learn how to get all data from database and delete all data from database. Let's get all data from database.

## Get All Data
```python
from kot import KOT

my_location_db = KOT("locations_of_team_members")

# Set data
my_location_db.set("Onur", "Sivas")
my_location_db.set("Atakan", "Ankara")

# Get all data
print(my_location_db.get_all())
```

Output:

```console
{'Onur': 'Sivas', 'Atakan': 'Ankara'}
```

## Delete All Data
```python

from kot import KOT

my_location_db = KOT("locations_of_team_members")

# Set data
my_location_db.set("Onur", "Sivas")

# Delete all data
my_location_db.delete_all()

# Get all data
print(my_location_db.get_all())
```

Output:

```console
{}
```


## Multiple Set
The `bulk_set` function allows you to insert multiple key-value pairs into the database in a single operation. It accepts a list of key-value pairs and returns a boolean indicating the success of the operation.

Example:
```python
from kot import KOT

db = KOT("My_Database")

kv_pairs = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
db.bulk_set(kv_pairs)
```

## Multiple Get
The `bulk_get` function allows you to retrieve multiple keys from the database in a single operation. It accepts a list of keys and returns a dictionary with the keys and their corresponding values.

Example:
```python
from kot import KOT

db = KOT("My_Database")

keys = ["key1", "key2", "key3"]
values = db.bulk_get(keys)
```

## Multiple Delete
The `bulk_delete` function allows you to delete multiple keys from the database in a single operation. It accepts a list of keys and returns a boolean indicating the success of the operation.

Example:
```python
from kot import KOT

db = KOT("My_Database")

keys = ["key1", "key2", "key3"]
db.bulk_delete(keys)
