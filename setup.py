#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="upsonic",
    version="0.0.0",
    description="""magic cloud layer""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/Upsonic/Upsonic",
    author="Upsonic",
    author_email="onur.atakan.ulusoy@upsonic.co",
    license="MIT",
    packages=["upsonic", "upsonic.core", "upsonic.interfaces", "upsonic.remote"],
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["upsonic=upsonic.core.upsonic:main"],
    },
    python_requires=">= 3",
    zip_safe=False,
)

