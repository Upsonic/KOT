---
layout: default
title: Encryption
nav_order: 8
has_children: false
---

# Encryption
Now we learned how to apply compressing in `set` function. Now we will learn how to apply encryption in `set` function. Let's set a data to database with encryption.


```python
from kot import KOT

my_address_db = KOT("addresses_of_team_members")

my_address_db.set("Onur", "Turkey, Sivas, ....", encryption_key="my_encryption_key")

print(my_address_db.get("Onur", encryption_key="my_encryption_key"))
```

Output:

```console
Turkey, Sivas, ....
```