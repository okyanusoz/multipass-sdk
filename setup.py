from setuptools import setup

setup(name='multipass-sdk',
version='0.2',
description='UNOFFICIAL Multipass Python SDK',
url='https://github.com/okyanusoz/multipass-sdk',
author='okyanusoz',
license='MIT',
py_modules=["multipass"],
scripts=["multipass.py"],
install_requires=["haikunator"],
zip_safe=False)