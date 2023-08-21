---
layout: default
title: Encryption
nav_order: 8
has_children: false
parent: FEATURES
---

# Encryption
Now we learned how to apply compressing in `set` function. Now we will learn how to apply encryption in `set` function. Let's set a data to database with encryption.


```python
from kot import KOT

# Create a database
my_address_db = KOT("addresses_of_team_members")

# Set data with encryption
my_address_db.set("Onur", "Turkey, Sivas, ....", encryption_key="my_encryption_key")

print(my_address_db.get("Onur", encryption_key="my_encryption_key"))
```

Output:

```console
Turkey, Sivas, ....
```

## Fernet Key Generation

In the encryption and decryption process, a Fernet key is generated. This is done using the `Fernet.generate_key()` function from the `cryptography.fernet` module. The Fernet key is necessary because it is used to initialize a Fernet object, which is used to encrypt and decrypt data.

Here is an example of how to generate a Fernet key:

```python
from kot import KOT
from cryptography.fernet import Fernet

# Generate a Fernet key
fernet_key = Fernet.generate_key()

# Create a database
my_address_db = KOT("addresses_of_team_members")

# Set data with encryption
my_address_db.set("Onur", "Turkey, Sivas, ....", encryption_key=fernet_key)

print(my_address_db.get("Onur", encryption_key=fernet_key))

print("Your Fernet key (SO Secret):", fernet_key)
```
