---
layout: default
title: Compressing
nav_order: 7
has_children: false
parent: FEATURES
---

# Compressing
We learned how to set and get data from database. Now we will learn to use compressing feature in `set` function. Let's set a data to database with compressing.

```python
from kot import KOT

# Create a database
my_activity_db = KOT("activity_of_team_members")

# Set data with compressing
my_activity_db.set("Onur", "LONG TEXT", compress=True)

# Get data
print(my_activity_db.get("Onur"))
```

Output:

```console
LONG TEXT
```