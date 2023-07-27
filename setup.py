from setuptools import setup


setup(name='kot',
version='0.20.1',
description="""Efficient Key-Value Data Storage with Multithreaded Simultaneous Writing""",
long_description="".join(open("README.md", encoding="utf-8").readlines()),
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/KOT',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["kot"],
package_dir={'':'src'},
install_requires=[
    "fire==0.5.0",
    "mgzip==0.2.1",
    "pycryptodome==3.18.0",
    "flet==0.8.4"
],
entry_points = {
    'console_scripts': ['KOT=kot.kot:main'],
},
python_requires=">= 3",
zip_safe=False)