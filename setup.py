# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='richard',
    version='0.2dev',
    author='Will Kahn-Greene and contibutors',
    author_email='willkg@mozilla.com',
    packages=find_packages(),
    url='https://github.com/willkg/richard',
    license='AGPLv3',
    description="video indexing site",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
