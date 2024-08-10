#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="kot",
    version="0.1.1",
    description="""special database for python lovers""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/KOT/KOT",
    author="KOT",
    author_email="onur@upsonic.co",
    license="MIT",
    packages=["kot", "kot.core"],
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["kot=kot.core.kot:main"],
    },
    python_requires=">= 3",
    zip_safe=False,
)

