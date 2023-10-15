#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()


setup(
    name="upsonic_api",
    version="0.0.0",
    description="""This is API package for Upsonic""",
    url="https://github.com/Upsonic/Upsonic",
    author='Onur Atakan ULUSOY',
    author_email='atadogan06@gmail.com',
    license='MIT',
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)


