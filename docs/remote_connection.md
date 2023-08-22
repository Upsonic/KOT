---
layout: default
title: REMOTE CONNECTION
nav_order: 19
has_children: false
---

# Remote Connection
KOT project have a module that named as `KOT_remote` with this you can easily use remote KOT API's. In this example we will use the docker api installation.

```python
from kot import KOT_remote

# Creating a database
my_db = KOT_remote("my_db", 'http://localhost:5000', 'dockerpass')

my_db.set("My_key", "My_value")
my_db.get("My_key")
my_db.delete("My_key")


my_db.database_list()
my_db.database_pop("my_db")
my_db.database_pop_all()

my_db.debug("This is a debug message")
my_db.info("This is an info message")
my_db.warning("This is a warning message")
my_db.error("This is an error message")
my_db.exception("This is an exception message")

```
