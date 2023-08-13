---
layout: default
title: Customer Database
nav_order: 1
has_children: false
parent: EXAMPLE APPLICATIONS
---

# Customer Database

## 1. Importing KOT
```python 
from kot import KOT
```

## 2. Create a new instance of the `KOT` class to represent the customer database:

```python
customer_db = KOT("customer_database")
```

## 3. Add a customer record to the database using the `set` method:

```python
customer_db.set("John Doe", {"email": "johndoe@example.com", "phone": "1234567890"})
```

## 4. Retrieve a customer record from the database using the `get` method:

```python
customer = customer_db.get("John Doe")
print(customer)
```

## 5. Delete a customer record from the database using the `delete` method:

```python
customer_db.delete("John Doe")
```

## Using Encryption

To use encryption in the customer database, you can pass an encryption key to the `set` method when adding a customer record. Here's an example:

```python
customer_db.set("John Doe", {"email": "johndoe@example.com", "phone": "1234567890"}, encryption_key="my_encryption_key")
```

To retrieve an encrypted customer record, you need to provide the same encryption key used during the set operation. Here's an example:

```python
customer = customer_db.get("John Doe", encryption_key="my_encryption_key")
print(customer)
```

This will output the decrypted customer record.



## Specifiying Database Location

To specify the location of the database file, you can pass a `folder` argument to the `KOT` class. Here's an example:

```python
customer_db = KOT("customer_database", folder="data")
```

This will create a `customer_database` in the `data` folder.


## Backup and Restore

To create a backup of the customer database, you can use the `backup` method of the `KOT` class. Here's an example:

```python
backup_location = customer_db.backup(".")
print("Backup created at:", backup_location)
```

To restore the customer database from a backup, you can use the `restore` method of the `KOT` class. Here's an example:

```python
customer_db.restore(backup_location)
print("Database restored from backup")
```

Make sure to provide the correct backup location when restoring the database.