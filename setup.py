#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="kot",
    version="0.37.2",
    description="""Flexible, secure and scalable database.""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/onuratakan/KOT",
    author="Onur Atakan ULUSOY",
    author_email="atadogan06@gmail.com",
    license="MIT",
    packages=["kot"],
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["KOT=kot.kot:main"],
    },
    python_requires=">= 3",
    zip_safe=False,
)
