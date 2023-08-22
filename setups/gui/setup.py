#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup
import os


with open(os.path.join(os.path.dirname(__file__), "..", "..","requirements",'gui.txt')) as fp:
    install_requires = fp.read()


setup(
    name="kot_gui",
    version="0.28.1",
    description="""This is GUI package for KOT""",
    url="https://github.com/onuratakan/KOT",
    author='Onur Atakan ULUSOY',
    author_email='atadogan06@gmail.com',
    license='MIT',
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)

