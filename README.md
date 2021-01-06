# UNOFFICIAL Multipass Python SDK

This is a Multipass CLI wrapper for Python 3.

## Installation

You need Multipass to use this SDK.

Simply run:
```
pip install multipass-sdk
```

Or, to install from source:


Clone this repo:

```
git clone --depth=1 https://github.com/okyanusoz/multipass-sdk # or gh clone okyanusoz/multipass-sdk if you have the Github CLI installed
```


Then run:
```
python setup.py install
```

## Usage

Usage is really simple:

```python
from multipass import MultipassClient
client = MultipassClient()
# or client = MultipassClient("<multipass command>") if your Multipass CLI name is diffrent
# Launch a VM(uses haikunator to generate VM names if you don't specify the name)
vm = client.launch(image="ubuntu-lts")
# Get info about the VM
print(vm.info())
# Run something in the VM(returns the response back in bytes)
vm.exec("<your command here>")
# Delete the VM
vm.delete()
client.purge()
# List VMs
print(client.list())
# Get a VM Object
vm = client.get_vm("<VM name>")
# For even more commands, see multipass.py
```

## Contributing

To contribute, simply send a pull request. The tests will run. If they succeed, then I will be happy to merge your PR.
