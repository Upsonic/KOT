#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="kot",
    version="0.42.1",
    description="""Flexible, secure and scalable database and your python cloud.""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/KOT-database/KOT",
    author="Onur Atakan ULUSOY",
    author_email="atadogan06@gmail.com",
    license="MIT",
    packages=["kot", "kot.core", "kot.interfaces", "kot.remote"],
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["KOT=kot.core.kot:main"],
    },
    python_requires=">= 3",
    zip_safe=False,
)

