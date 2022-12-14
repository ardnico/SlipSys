#!/usr/bin/env python3

from setuptools import setup
import setuptools


from os import path
here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SlipSys',
    version='1.0.0',
    author='Ardnico',
    author_email='leaf.sun2@gmail.com',
    description='',
    install_requires=["django"],
    long_description=long_description,
    url='https://github.com/ardnico',
    packages=setuptools.find_packages(),
    license='Apache 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            ""
        ]
    },
    python_requires='>=3.5',
)