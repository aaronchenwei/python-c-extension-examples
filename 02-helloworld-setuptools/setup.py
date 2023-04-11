#!/usr/bin/env python3

from setuptools import setup, Extension

setup(
	name = "helloworld",
	version = "1.0",
    description='A simple example of a Python C-extension',
	ext_modules = [Extension("helloworld", ["bind.c", "libmypy.c"])]
)

