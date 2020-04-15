#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()


with open('citext/__init__.py') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='sqlalchemy-citext',
    version=version,
    description="A sqlalchemy plugin that allows postgres use of CITEXT.",
    long_description=long_description,
    author=', '.join([
        'Mahmoud Abdelkader',
        'Davide Setti',
    ]),
    url='https://github.com/mahmoudimus/sqlalchemy-citext',
    install_requires=[
        'SQLAlchemy>=0.6',
    ],
    test_suite='tests',
    license='BSD',
    setup_requires=[],
    zip_safe=False,
    packages=['citext'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
