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

my_location_db = KOT("locations_of_team_members")

my_location_db.set("Onur", "Sivas")

print(my_location_db.get("Onur"))

my_location_db.delete("Onur")
```

Output:

```console
Sivas
```