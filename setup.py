#!/usr/bin/env python

import os
from setuptools import setup


if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = '''Python wrapper for the IBM RXN for Chemistry API'''

setup(
    name='RXN4Chemistry',
    version='0.1.0',
    author='RXN for Chemistry team',
    author_email='phs@zurich.ibm.com, tte@zurich.ibm.com',
    py_modules=['RXN4Chemistry'],
    description='Python wrapper for IBM RXN for Chemistry',
    long_description=long_description,
    license='MIT',
    requirements=[
        'requests==2.23.0'
    ],
    url='https://github.com/rxn4chemistry/rxn4chemistry'
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)