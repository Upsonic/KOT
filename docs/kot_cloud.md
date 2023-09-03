---
layout: default
title: KOT CLOUD
nav_order: 23
has_children: false
---

# KOT Cloud
KOT Cloud: the ultimate, free cloud database for all Python developers. Experience reliability, efficiency, and top-notch security in one powerful solution. Start your seamless development journey with KOT Cloud today!

“Save your Python Things to the Cloud: Code Unrestricted, Scale Limitless with KOT Cloud!”



## Enable the cloud connection in your Python
```console
KOT cloud_key
```

> cloud-HWP0iUIvUlFd18acOgrNa6UmLx6yua

```python
from kot import KOT_cloud

cloud = KOT_cloud("YOUR_CLOUD_KEY")
```

## Sending


```python
#FUNCTION
@cloud.active
def remove_lines(string):
    return string.replace("\n","")

#CLASS
@cloud.active
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#VARIABLE
price = 15.2
cloud.set("price", price)
```


## Getting

```python
#FUNCTION
cloud.get("remove_lines")("Hi,\nhow are you")

#CLASS
cloud.get("human")("Onur", 100)

#VARIABLE
cloud.get("price")
```



## Encryption
You can give `encryption_key` to all functions, this will encrypt your things in your computer and after its send the encrypted version to KOT cloud.
