---
layout: default
title: CREATING A DATABASE
nav_order: 2
has_children: false
---

# Creating a Database
In this section, we will learn how to create a database with KOT in currently dir. The KOT database library is have a easy to use interface. You can create a database with a single line of code. Also you can set the folder with `folder` paramater. Let's create a database with KOT.

```python
from kot import KOT

# Creating a database
my_db = KOT("my_database")
#my_db = KOT("my_database", folder="/root/my_databases")
```