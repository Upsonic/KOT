# KeyPact | Multithreaded Simultaneous Writing Key-Value DB
KeyPact is an efficient key-value data storage system that aims to making simultaneous writing with multithreaded. 

## Features
- Multithread Support
- Simultaneous Writing
- Easy to use
- Easy to integrate
- Easy to deploy


## Installation
You can install Keypact by pip3:

```console
pip3 install keypact
```

## Usage
Keypact is aimed to be used in Python and command line as well. You can use it in your Python code or in command line.


### In Python

```python
import keypact

my_keypact = keypact.KeyPact("client_addresses")

my_keypact.set("Onur", "Sivas")

print(my_keypact.get("Onur"))
```

### Console

```console	
keypact --name=client_addresses set Onur Sivas
```
```console
keypact --name=client_addresses get Onur
```


## Contributing
Contributions to Keypact are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
Keypact is released under the MIT License.
