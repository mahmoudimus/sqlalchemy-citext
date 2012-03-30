import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


PATH_TO_FILE = os.path.dirname(__file__)


with open(os.path.join(PATH_TO_FILE, 'README.md')) as f:
    long_description = f.read()


VERSION = (1, 0, 1)


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
    author='Mahmoud Abdelkader',
    author_email='mabdelkader@gmail.com',
    url='https://github.com/mahmoudimus/sqlalchemy-citext',
    install_requires=[
        'SQLAlchemy>=0.6',
        'psycopg2==2.4.5',
    ],
    setup_requires=[],
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
