# Signify Python Wrapper
Simple Python wrapper for [OpenBSD's signify tool](https://man.openbsd.org/signify).

## Setup
Start by adding this repository as a submodule in your own:
```
$ git clone --recurse-submodules git@github.com:deni/python-signify-wrapper.git signify_wrapper
$ git submodule -b abranch -- /url/of/submodule/repo
$ git submodule update --remote --recursive
$ git submodule add -b main git@github.com:deni/python-signify-wrapper.git signify_wrapper
```

This will add the wrapper into your project as ``signify_wrapper``. This will make it possible to import the module into another project.

The signify binary is required for the wrapper to function. Installation using common package managers:
apt: ``# apt install signify-openbsd``
brew: ``$ signify-osx``

The environment variable ``SIGNIFY_BINARY`` has to point to the binary.

Location of the newly installed binary:
```
$ which signify-openbsd
```
```
$ which signify-osx
```

Then you can make a variable and set it as an environment variable using the following commands: *(Replace x with location from previous command)*
```
SINGNIFY_BINARY=/usr/local/bin/signify
export SINGNIFY_BINARY
```

Then it can be imported in Python using:
```
import signify_wrapper
```

## Functions
This wrapper has two functions: `sign` and `signed`.

### sign
This function is used to sign data input.

Input parameters are:
* `data`, which is a byte object to be signed.
* `privatekey`, which is a string object containing the privatekey used to sign the data object.

If it succeeds in signing then the function will return the signature, and if not, then the return will be `None`.

#### Example of usage:

*TODO*

### signed
This function is used to verify if the signed information is correct.

Input parameters are:
* `data`, which is a byte object to be signed.
* `publickey`, which is a string object containing the publickey of the keypair used to sign the data object.
* `signature`, which is a string object of the signature from the signing of the data.

If it is a correct match for the signature then it will return `True`, and if not, then the return will be `False`.

#### Example of usage:

*TODO*
