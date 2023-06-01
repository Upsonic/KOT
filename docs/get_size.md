---
layout: default
title: Get Size
nav_order: 8
has_children: false
---

# Get Size
In here we will learn how to sizes of datas in database. Let's get size of a data from database.



```python
from kot import KOT

my_location_db = KOT("locations_of_team_members")
my_location_db.set("Onur", "Sivas")


print(my_location_db.size("Onur"))
print(my_location_db.size_all())

```

Output:

```console
5
5
```