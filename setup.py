#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='test-api',
    version='0.2',
    description='Python Test Api',
    long_description=readme,
    author='Raphael Lehmann',
    author_email='kontakt@rleh.de',
    url='https://github.com/rleh/python-test-api',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'falcon',
        'cython',
        'simplejson'
    ]
)