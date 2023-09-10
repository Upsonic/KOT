---
layout: default
title: Helper Functions
nav_order: 24
has_children: False
parent: KOT CLOUD
---

# Helper Functions
When you develop some applications with KOT Cloud you will need some shortcuts for installing libraries or preventing exceptions.

## Auto Install Packages
With this feature you can write new functions with new libraries this decorator will install the library before the execution.

```python
from kot import KOT_Cloud
from kot import requires

cloud = KOT_Cloud("YOUR_CLOUD_KEY")

@cloud.active
@requires("kot")
def kot_database_integration():
    from kot import KOT
    my_db = KOT("My_DB")
    ...

```

You can use this command for all libraries in the pypi:

```python
@cloud.active
@requires("kot")
@requires("kot_api")
@requires("kot_gui")
@requires("waitress==2.1.2")
@requires("pytest")
@requires("naruno")
@requires("ANY_LIBRARY")
```



## Preventing Exception
When you distribute the cloud things to customers you will need to a system that not brokes. For this you can use this decorator after the `@cloud.active` decoration

```python
from kot import KOT_Cloud
from kot import no_exception

cloud = KOT_Cloud("YOUR_CLOUD_KEY")

@cloud.active
@no_exception
def broken_code():
    raise Exception()


```

This command is prevent the all exceptions on this function.


## Multiple Use

You should use this flow for decorators

- 1st: `@cloud.active` 
- 2nd: `@no_exception`
- 3nd: `@requires("librar")`

```python
from kot import KOT_Cloud
from kot import requires
from kot import no_exception

cloud = KOT_Cloud("YOUR_CLOUD_KEY")

@cloud.active
@no_exception
@requires("kot")
@requires("naruno")
@requires("kot_api")
@requires("waitress==2.1.2")
def broken_kot_database_integration():
    from kot import KOT
    my_db = KOT("My_DB")
    raise Exception()


```

Some problems can execute if you dont tract this flow.