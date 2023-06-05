---
layout: default
title: File Operations
nav_order: 4
has_children: false
parent: SET GET DELETE
---

# Set, Get and Delete File
Previously section we set and get data from database. Now we will learn how to set and get file from database. This feature is move or copy the file by your `dont_remove` argument in the `set_file` to database inside. Let's set a file to database.

```python
from kot import KOT

# Create a database
my_image_db = KOT("images_of_team_members")

# Set file
my_image_db.set_file("Onur", "Onur.jpg")

# Get file
print(my_image_db.get_file("Onur"))

# Delete file
my_image_db.delete_file("Onur")
```

Output:

```console
/root/KOT-92e2df9705120b6a67451c18e6e8a861c893e21d2d0488528b979e81ef2401d2/ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb_Onur.jpg
```


