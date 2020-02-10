#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


PATH_TO_FILE = os.path.dirname(__file__)


with open(os.path.join(PATH_TO_FILE, 'README.rst')) as f:
    long_description = f.read()


VERSION = (1, 5, 0)


# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]


version = str_version


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
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
