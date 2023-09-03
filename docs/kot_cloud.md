---
layout: default
title: KOT CLOUD
nav_order: 23
has_children: false
---

# KOT Cloud
KOT Cloud: the ultimate, free cloud database for all Python developers. Experience reliability, efficiency, and top-notch security in one powerful solution. Start your seamless development journey with KOT Cloud today!

“Save your Python Things to the Cloud: Code Unrestricted, Scale Limitless with KOT Cloud!”


## Generate a key for your cloud

```console
KOT cloud_key
```
```console
> cloud-HWP0iUIvUlFd18acOgrNa6UmLx6yua

```

## Enable the cloud connection in your Python

```python
from kot import KOT_cloud
cloud = KOT_cloud("YOUR_CLOUD_KEY")
```


## Cloud Functions

This function is removes the lines of given string and when you want to access this function to anywhere you can send to cloud.

```python
def remove_lines(string):
    return string.replace("\n","")

cloud._function(remove_lines) # Sending to Cloud
```

Now its sent to your cloud and now you can access easily in another code and another machine.
```python

from kot import KOT_cloud
cloud = KOT_cloud("YOUR_CLOUD_KEY")

my_string = "Hello\n I am Onur\n Who are you ?"

my_removed_lines_string = cloud._function("remove_lines")(my_string)
```

Now you the `my_removed_lines_string` variable is equal to:

```python
"Hello I am Onur Who are you ?"
```


## Cloud Classes

This class have `name` and `age` records and when you want to access this class to anywhere you can send to cloud.

```python
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cloud._class(human)

```

Now its sent to your cloud and now you can access easily in another code and another machine.
```python

from kot import KOT_cloud
cloud = KOT_cloud("YOUR_CLOUD_KEY")

onur = cloud._class("human")("Onur", 100)
```

Now you the `onur` variable is an object of human class.

