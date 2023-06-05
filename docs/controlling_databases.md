---
layout: default
title: CONTROLLING DATABASES
nav_order: 10
has_children: false
---

# Get All Databases
In here we will learn how to get all databases in currently dir. Let's get all databases.

```python
from kot import KOT

# List all databases
print(KOT.database_list())
```

Output:

```console
{
    "mydb": "/root/KOT-b50d3038fdd554ed9b9d694bc52f73d9899d2576ed6d48899402b5923284edf1"
}
```

# Delete a Database
In here we will learn how to delete a database. Let's delete a database.

```python
from kot import KOT

# Delete a database
KOT.database_delete("mydb")
```

# Delete All Databases
In here we will learn how to delete all databases in currently dir. Let's delete all databases.

```python   
from kot import KOT

# Delete all databases
KOT.database_delete_all()
```
