---
layout: default
title: USING AS LOGGER
nav_order: 21
has_children: false
---

# Using as Logger

This document provides documentation for the debug, info, warning, error, and exception functions of the KOT class.

## Debug Function

The debug function is used to log debug messages. It takes a single parameter:

- `message` (str): The message to be logged.

Example usage:

```python
from kot import KOT

# Creating a database
logger = KOT("logs")

logger.debug("This is a debug message")
```

The function does not return any value and does not raise any exceptions.

## Info Function

The info function is used to log informational messages. It takes a single parameter, `message`, which is the message to be logged.

Example usage:

```python
from kot import KOT

# Creating a database
logger = KOT("logs")

logger.info("This is an info message")
```

The function does not return any value and does not raise any exceptions.

## Warning Function

The warning function is used to log warning messages. It takes a single parameter:

- `message` (str): The message to be logged.

Example usage:

```python
from kot import KOT

# Creating a database
logger = KOT("logs")

logger.warning("This is a warning message")
```

The function does not return any value and does not raise any exceptions.

## Error Function

The error function is used to log error messages. It takes a single parameter:

- `message` (str): The message to be logged.

Example usage:


```python
from kot import KOT

# Creating a database
logger = KOT("logs")

logger.error("This is an error message")
```

The function does not return any value and does not raise any exceptions.

## Exception Function

The exception function is used to log exception messages. It takes a single parameter:

- `message` (str): The message to be logged.

Example usage:


```python
from kot import KOT

# Creating a database
logger = KOT("logs")

logger.exception("This is an exception message")
```

The function does not return any value and does not raise any exceptions.



## Getting logs

```console
KOT --name logs get_all
```
