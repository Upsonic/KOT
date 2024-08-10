---
layout: default
title: Get Size
nav_order: 6
has_children: false
parent: FEATURES
---

# Get Size
In here we will learn how to sizes of datas in database. Let's get size of a data from database.



```python
from kot import KOT

# Create a database and set data
my_location_db = KOT("locations_of_team_members")
my_location_db.set("Onur", "Sivas")



# Get size of data
print(my_location_db.size("Onur"))


# Get size of all data
print(my_location_db.size_all())


```

Output:

```console
5
5555
```