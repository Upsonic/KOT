---
layout: default
title: Set and Get
nav_order: 3
has_children: false
---

# Set and Get
Previously section we created a database. Now we will learn how to set and get data from database. Let's set a data to database.

```python
from kot import KOT

my_location_db = KOT("locations_of_team_members")

my_location_db.set("Onur", "Sivas")

print(my_location_db.get("Onur"))
```

Output:

```console
Sivas
```