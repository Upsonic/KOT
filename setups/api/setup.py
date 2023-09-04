#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()


setup(
    name="kot_api",
    version="0.37.0",
    description="""This is API package for KOT""",
    url="https://github.com/onuratakan/KOT",
    author='Onur Atakan ULUSOY',
    author_email='atadogan06@gmail.com',
    license='MIT',
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)

