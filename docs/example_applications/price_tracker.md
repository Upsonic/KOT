---
layout: default
title: Price Tracker
nav_order: 2
has_children: false
parent: EXAMPLE APPLICATIONS
---

# 1. Importing KOT
```python 
from kot import KOT
```

# 2. Create a new instance of the `KOT` class to represent the price tracker:

```python
customer_db = KOT("price_tracker")
```

# 3. Add a price record to the database using the `set` method:

```python
customer_db.set("Price 1", {"product": "Product 1", "price": 10.99})
```

# 4. Retrieve a price record from the database using the `get` method:

```python
price = customer_db.get("Price 1")
print(price)
```

# 5. Delete a price record from the database using the `delete` method:

```python
customer_db.delete("Price 1")
```

# Using Compressing

To use compressing in the price tracker, you can pass a `compress` argument to the `set` method when adding a price record. Here's an example:

```python
customer_db.set("Price 1", {"product": "Product 1", "price": 10.99}, compress=True)
```

To retrieve a compressed price record, you can simply use the `get` method. Here's an example:

```python
price = customer_db.get("Price 1")
print(price)
```

This will output the retrieved price record.



# Specifiying Database Location

To specify the location of the database file for the price tracker, you can pass a `folder` argument to the `KOT` class. Here's an example:

```python
customer_db = KOT("price_tracker", folder="data")
```

This will create a `customer_database` in the `data` folder.
