#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
name="kot_api",
version='0.24.1',
description="""This is API package for KOT""",
url="https://github.com/onuratakan/KOT",
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
install_requires="""
flask==2.0.0
waitress==2.1.2
""",
python_requires=">= 3",
zip_safe=False,
)

