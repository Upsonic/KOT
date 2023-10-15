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
from upsonic import Upsonic

# Create a database
my_activity_db = Upsonic("activity_of_team_members")

# Set data with compressing
my_activity_db.set("Onur", "LONG TEXT", compress=True)

# Get data
print(my_activity_db.get("Onur"))
```

Output:

```console
LONG TEXT
```

# Settng Global Compressing

```python
from upsonic import Upsonic


Upsonic.force_compress = True


#Your operations

```