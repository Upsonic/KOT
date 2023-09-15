#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name="kot_web",
    version="0.42.1",
    description="""This is WEB package for KOT""",
    url="https://github.com/KOT-database/KOT",
    author='Onur Atakan ULUSOY',
    author_email='atadogan06@gmail.com',
    license='MIT',
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)


