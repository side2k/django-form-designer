#!/usr/bin/env python
"""
Django Form Designer

Original code copyright (c) 2009, Samuel Luescher
setup.py added by Thane Thomson (thane@praekelt.com), Praekelt Digital
"""

from setuptools import setup, find_packages

setup(
    name='django-form-designer',
    version='0.1',
    description='Construct Django forms through the Django admin(fork by side2k)',
    author='Praekelt Digital',
    author_email='dev@praekelt.com',
    url='https://github.com/thanethomson/django-form-designer',
    packages = find_packages(),
    include_package_data=True,
)