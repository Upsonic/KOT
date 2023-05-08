from setuptools import setup


setup(name='keypact',
version='0.2.4',
description="""Efficient Key-Value Data Storage with Multithreaded Simultaneous Writing""",
long_description="".join(open("README.md", encoding="utf-8").readlines()),
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/KeyPact',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["keypact"],
package_dir={'':'src'},
install_requires=[
    "fire==0.5.0"
],
entry_points = {
    'console_scripts': ['keypact=keypact.keypact:main'],
},
python_requires=">= 3",
zip_safe=False)