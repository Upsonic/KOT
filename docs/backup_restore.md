---
layout: default
title: BACKUP RESTORE
nav_order: 9
has_children: false
---

# Backup and Restore
In here we will learn how to backup and restore databases. Let's backup a database.

```python
from kot import KOT

# Create a database and set data
my_location_db = KOT("locations_of_team_members")

# Generating a backup file and printing to console
location_db_backup_address = my_location_db.backup(".")
print(location_db_backup_address)

# Restore database from backup file
my_location_db.restore(location_db_backup_address)

```

Output:

```console
./2023_06_01_18_36_40.KOT
```
