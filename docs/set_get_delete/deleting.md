---
layout: default
title: Deleting
nav_order: 5
has_children: false
parent: SET GET DELETE
---

# Deleting
In here we will learn how to delete data and files from database. Let's delete a data from database.

```python
from kot import KOT

my_location_db = KOT("locations_of_team_members")
my_location_db.set("Onur", "Sivas")

my_image_db = KOT("images_of_team_members")
my_image_db.set_file("Onur", "Onur.jpg")


my_location_db.delete("Onur")
my_image_db.delete_file("Onur")
```
