# KOT database | [![Tests](https://github.com/onuratakan/KOT/actions/workflows/tests.yml/badge.svg)](https://github.com/onuratakan/KOT/actions/workflows/tests.yml) | [![codecov](https://codecov.io/gh/onuratakan/KOT/branch/master/graph/badge.svg?token=Q38EWFNSIJ)](https://codecov.io/gh/onuratakan/KOT) | [![After Deploy Test Every 15 Minute](https://github.com/onuratakan/KOT/actions/workflows/after_deploy_test.yml/badge.svg)](https://github.com/onuratakan/KOT/actions/workflows/after_deploy_test.yml)

The KOT database is a flexible, secure and scalable database that supports multiple data formats. It comes with built-in features for compressing and encrypting data, and is compatible with all operating systems. With easy-to-use commands, the KOT database is an excellent choice for developers seeking an efficient and reliable storage solution for their data.

## Installation
You can install KOT by pip3:

```console
pip3 install kot
```


## 🎉 KOT Cloud is published ! | [![Cloud Test Every - 15 Minute](https://github.com/onuratakan/KOT/actions/workflows/cloud_test.yml/badge.svg)](https://github.com/onuratakan/KOT/actions/workflows/cloud_test.yml) | [Go to Docs](https://onuratakan.github.io/KOT/KOT_Cloud.html)
KOT Cloud: the ultimate, free cloud database for all Python developers. Experience reliability, efficiency, and top-notch security in one powerful solution. Start your seamless development journey with KOT Cloud today!

- "Save your Python Things to the Cloud: Code Unrestricted, Scale Limitless with KOT Cloud!"

![KOT Cloud](https://github.com/onuratakan/KOT/assets/41792982/fb3aa83d-d641-4f79-b4ea-46d33dba0ad1)



### Creating Your Free Cloud Key
```console
KOT cloud_key
```

### Using Your Cloud | Setting

```python
from kot import KOT_Cloud
cloud = KOT_Cloud("YOUR_CLOUD_KEY")

@cloud.active
def get_address():
    return "Hello World I am from KOT Cloud"
```

### Using Your Cloud | Getting

```python
from kot import KOT_Cloud
cloud = KOT_Cloud("YOUR_CLOUD_KEY")


print(cloud.get("get_address")())
```

## Demo

```python
from kot import KOT

# Creating databases
db = KOT("My_New_DB")


# Flexible
db.set("Key", "String")
db.set("Key", 123)
db.set("Key", 123.213)
db.set("Key", Object())
db.set("Key", ["Alist"])
db.set("Key", {"a": "dict"})
db.set("Key", (1,"Atuple"))
db.set("Key", file="onur.jpg")
db.set("Key", file="onur.anytype")


# Secure
db.set("Key", "String",        encryption_key="my_encryption_key")
db.set("Key", 123,             encryption_key="my_encryption_key")
db.set("Key", 123.213,         encryption_key="my_encryption_key")
db.set("Key", Object(),        encryption_key="my_encryption_key")
db.set("Key", ["Alist"],       encryption_key="my_encryption_key")
db.set("Key", {"a": "dict"},   encryption_key="my_encryption_key")
db.set("Key", (1,"Atuple"),    encryption_key="my_encryption_key")
db.set("Key", file="onur.jpg", encryption_key="my_encryption_key")



# Scalable
db.get("Key") #Instant, no waiting and no searching


```

## Interfaces
- [CLI](https://onuratakan.github.io/KOT/interfaces/cli.html)
- [GUI](https://onuratakan.github.io/KOT/interfaces/gui.html)
- [WEB](https://onuratakan.github.io/KOT/interfaces/web.html)
- [CLI](https://onuratakan.github.io/KOT/interfaces/api.html)

## Features

- **Flexibility**: Save data in any format, including objects and files, providing great flexibility and adaptability to different use cases and data structures.
- **Compressing**: Compress data to minimize storage space while enabling faster data retrieval and processing.
- **Encryption**: Keep sensitive information secure and private with the included encryption feature.
- **Scalability**: Offers stable processing times of set, get, and delete commands, regardless of the dataset's size.
- **Fault Tolerance**: By the design of the KOT database, it is fully fault-tolerant because each datas are designed to be independent of each other on the disk.
- **Memory Friendly**: The KOT database is designed to use as little memory as possible. It only loads the data you want to access into memory.
- **Cross-Platform Compatibility**: Compatible with all operating systems, making it easier to integrate into any project.
- **Docker Avaibility**: You can use KOT database API as an container on Docker platform. It's good for more stable, safe and durable uses.
- **Transactional and Asynchronous Operations**: Perform multiple operations in a single transaction or perform operations asynchronously for improved performance.


```mermaid
graph TD;
    A[KOT Database];

    A --> O[API];
    A --> P[CLI];
    A --> Q[GUI];
    A --> R[Web];
    O --> N[Interfaces];
    P --> N[Interfaces];
    Q --> N[Interfaces];
    R --> N[Interfaces];

    N --> J[Functions];


    J --> B[Features];
    B --> C[Multi-threaded Writing];
    B --> D[Compression];
    B --> E[Encryption];
    B --> F[Scalability];
    B --> G[Fault Tolerance];
    B --> H[Memory Friendly];
    B --> I[Cross-Platform Compatibility];


```

## Documentation
You can find the documentation [here](https://onuratakan.github.io/KOT/).


## Contributing
Contributions to KOT are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
KOT is released under the MIT License.
