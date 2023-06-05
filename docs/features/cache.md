---
layout: default
title: Cache
nav_order: 9
has_children: false
parent: FEATURES
---

# Cache
In here we will learn how to use and clean cache. Let's use cache.

## Use Cache
```python
from kot import KOT
import time

# Create a database
my_location_db = KOT("locations_of_team_members")

# Set data with compressing
my_location_db.set("Onur", "Sivas", cache_policy = 60) # 60 Seconds cache activated
my_location_db.set("Onur", "Hafik") # 60 Seconds cache activated

# Get data
print(my_location_db.get("Onur"))
# Get data after cache time
time.sleep(60)
print(my_location_db.get("Onur"))
```

Output:

```console
Sivas
Hafik
```

## Clean Cache
Cleaning Cache is so important for encrypted data. Because if you don't clean cache, your data will be stay in cache. Let's clean cache.

```python
from kot import KOT

# Create a database
my_location_db = KOT("locations_of_team_members")

my_location_db.clear_cache()
```
