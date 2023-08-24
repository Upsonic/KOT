#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="kot",
    version="0.29.0",
    description="""Efficient Key-Value Data Storage with Multithreaded Simultaneous Writing""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/onuratakan/KOT",
    author="Onur Atakan ULUSOY",
    author_email="atadogan06@gmail.com",
    license="MIT",
    packages=["kot"],
    package_dir={"": "src"},
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["KOT=kot.kot:main"],
    },
    python_requires=">= 3",
    zip_safe=False,
)
