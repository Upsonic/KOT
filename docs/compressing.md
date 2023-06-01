---
layout: default
title: Compressing
nav_order: 6
has_children: false
---

# Compressing
We learned how to set and get data from database. Now we will learn to use compressing feature in `set` function. Let's set a data to database with compressing.

```python
from kot import KOT

my_activity_db = KOT("activity_of_team_members")

my_activity_db.set("Onur", "LONG TEXT", compress=True)

print(my_activity_db.get("Onur"))
```

Output:

```console
LONG TEXT
```