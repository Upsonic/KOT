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

# Create a database and set file
my_image_db = KOT("images_of_team_members")
my_image_db.set_file("Onur", "Onur.jpg")

# Get size of data and file
print(my_location_db.size("Onur"))
print(my_image_db.size_file("Onur"))

# Get size of all data and file
print(my_location_db.size_all())
print(my_image_db.size_all())

```

Output:

```console
5
5555
5
5555
```