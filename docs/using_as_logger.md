---
layout: default
title: USING AS LOGGER
nav_order: 21
has_children: false
---

# Using as Logger

This document provides documentation for the debug, info, warning, error, and exception functions of the Upsonic class.

These functions takes a single parameter:

- `message` (str): The message to be logged.

Example usage:

```python
from upsonic import Upsonic

#If you want you can set the global encrypton and compress for logs 
#Upsonic.force_encrypt = "My_Global_Enc_Key"
#Upsonic.force_compress = True

# Creating a database
logger = Upsonic("logs")

logger.debug("This is a log message")
logger.info("This is a log message")
logger.warning("This is a log message")
logger.error("This is a log message")
logger.exception("This is a log message")


```




## Getting logs

```console
Upsonic --name logs get_all
```
