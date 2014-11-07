#!/usr/bin/env python

from setuptools import setup

description = "Wrapper around Openstack Nova and Paramiko"

setup(
    name="novamiko",
    version="0.0.1",
    author="Andrew Melton",
    author_email="andrew.melton@rackspace.com",
    description=description,
    long_description=description,
    license="Apache",
    keywords="openstack nova paramiko",
    url="https://github.com/ramielrowe/paramiko",
    py_modules=['novamiko'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    requires=(
        'netaddr',
        'paramiko',
        'novaclient',
    ),

)