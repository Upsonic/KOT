# KOT | Multithreaded Simultaneous Writing Key-Value DB
KOT is an efficient key-value data storage system that aims to making simultaneous writing with multithreaded. 

## Features
- Multithread Support
- Simultaneous Writing
- Easy to use
- Easy to integrate
- Easy to deploy
- Able to saving files
- Able to compressing datas
- Able to storing pyton objects (Pickle)
- Able to encryption
- Able to caching
- Able to backup and restore
- Able to listing, deleting and deleting all databases


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

print(my_kot.get("Onur"))
```

### Console

```console	
kot --name=client_addresses set Onur Sivas
```
```console
kot --name=client_addresses get Onur
```


## Contributing
Contributions to KOT are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
KOT is released under the MIT License.
