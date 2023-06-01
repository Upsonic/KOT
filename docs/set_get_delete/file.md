---
layout: default
title: File
nav_order: 4
has_children: false
parent: SET GET DELETE
---

# Set and Get File
Previously section we set and get data from database. Now we will learn how to set and get file from database. This feature is move or copy the file by your `dont_remove` argument in the `set_file` to database inside. Let's set a file to database.

```python
from kot import KOT

my_image_db = KOT("images_of_team_members")

my_image_db.set_file("Onur", "Onur.jpg")

print(my_image_db.get_file("Onur"))

my_image_db.delete_file("Onur")
```

Output:

```console
new_location_of_onur.jpg
```


