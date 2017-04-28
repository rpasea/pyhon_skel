# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='skeleton',
    version='0.1.0',
    description='Skeleton python package',
    long_description=readme,
    author='Radu Pasea',
    author_email='radu@changeme.com',
    url='https://github.com/rpasea/pyhon_skel',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['flask'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
