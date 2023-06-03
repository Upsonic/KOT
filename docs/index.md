---
layout: default
title: Introduction
nav_order: 1
has_children: false
---

# KOT database

The KOT database is a flexible, secure, and scalable database that supports multiple data formats. It comes with built-in features for compressing and encrypting data, and is compatible with all operating systems. With easy-to-use commands, the KOT database is an excellent choice for developers seeking an efficient and reliable storage solution for their data.

## Features

- **Flexibility**: Save data in any format, including objects, definitions, numbers, strings, floats, and files, providing great flexibility and adaptability to different use cases and data structures.
- **Compressing**: Compress data to minimize storage space while enabling faster data retrieval and processing.
- **Encryption**: Keep sensitive information secure and private with the included encryption feature.
- **Scalability**: Offers stable processing times of set, get, and delete commands, regardless of the dataset's size.
- **Cross-Platform Compatibility**: Compatible with all operating systems, making it easier to integrate into any project.


## Installation
You can install KOT by pip3:

```console
pip3 install kot
```

## Usage
KOT is aimed to be used in Python and command line as well. You can use it in your Python code or in command line.


### In Python

```python
from kot import KOT

my_kot = KOT("client_addresses")

my_kot.set("Onur", "Sivas")
#my_kot.set("Onur", "Sivas", compress=True)
#my_kot.set("Onur", "Sivas", encryption_key="my_encryption_key"))
#my_kot.set_file("Onur_Image", "Onur.jpg")

print(my_kot.get("Onur"))

my_kot.delete("Onur")
#my_kot.delete_file("Onur_Image")
```

### Console

```console	
kot --name=client_addresses set Onur Sivas
```
```console
kot --name=client_addresses get Onur
```

## Documentation
You can find the documentation [here](https://onuratakan.github.io/KOT/).


## Contributing
Contributions to KOT are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
KOT is released under the MIT License.
