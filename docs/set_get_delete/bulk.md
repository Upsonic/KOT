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
