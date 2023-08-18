---
layout: default
title: DECORATOR FUNCTIONS
nav_order: 11
has_children: false
---
## Decorator Functions
This is an fast method for implementing KOT database to your function in one line.


## Saving of an Function 

### by Function Name
```python
from kot import KOT

db = KOT("My_Database")

@db.save_by_name
def my_function(param, param_optional="Optional Param"):
    return "Hello, World!"

my_function("Hi",param_optional="World")
```
```console
KOT execute "GET_ALL My_Database"

> my_function: [[["Hi"], {"param_optional": "World"}], "Hello, World!"]
```

### by Function Name + Time
```python
from kot import KOT

db = KOT("My_Database")

@db.save_by_name_time
def my_function(param, param_optional="Optional Param"):
    return "Hello, World!"

my_function("Hi",param_optional="World")
```
```console
KOT execute "GET_ALL My_Database"

> my_function-1692291105.6838315: [[["Hi"], {"param_optional": "World"}], "Hello, World!"]
```

### by Function Name + Time + Random (For High Speed Uses)
```python
from kot import KOT

db = KOT("My_Database")

@db.save_by_name_time_random
def my_function(param, param_optional="Optional Param"):
    return "Hello, World!"

my_function("Hi",param_optional="World")
```
```console
KOT execute "GET_ALL My_Database"

> my_function-1692291156.88717-91746: [[["Hi"], {"param_optional": "World"}], "Hello, World!"]
```