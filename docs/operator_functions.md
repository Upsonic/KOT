---
title: OPERATOR FUNCTIONS
nav_order: 13
---

# Operator Functions

Operator functions in KOT are special methods that allow users to perform multiple operations in a single transaction or perform operations asynchronously. These functions enhance the functionality of the KOT class and provide users with more flexibility and performance improvements.


## Transactional Operations

Transactional operations allow users to perform multiple operations (SET, GET, DELETE) in a single transaction. If any operation fails, all operations in the transaction are rolled back, ensuring data consistency and integrity. The `transactional_operations` method allows users to perform multiple operations (SET, GET, DELETE) in a single transaction.

Here is an example of how to use this method:

```python
from kot import KOT

# Creating a database
my_db = KOT("my_database")

operations = [('SET', 'key1', 'value1'), ('GET', 'key1'), ('DELETE', 'key1')]
results = my_db.transactional_operations(operations)
```

## Asynchronous Operations

Asynchronous operations allow users to perform operations (SET, GET, DELETE) asynchronously. This can improve performance in scenarios where the user does not need to wait for the operation to complete before proceeding with other tasks. The `asynchronous_operations` method allows users to perform operations (set, get, delete) asynchronously.

Here is an example of how to use this method:

```python
from kot import KOT

# Creating a database
my_db = KOT("my_database")

thread = my_db.asynchronous_operations('SET', 'key1', 'value1')

# Make other thinks without any delay

thread.join()
```
