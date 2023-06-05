---
layout: default
title: Data Operations
nav_order: 3
has_children: false
parent: SET GET DELETE
---

# Set, Get and Delete Data
Previously section we created a database. Now we will learn how to set and get data from database. Let's set a data to database.

```python
from kot import KOT

# Create a database
my_location_db = KOT("locations_of_team_members")

# Set data
my_location_db.set("Onur", "Sivas")

# Get data
print(my_location_db.get("Onur"))

# Delete data
my_location_db.delete("Onur")
```

Output:

```console
Sivas
```