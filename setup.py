# coding=utf-8
"""Handle the package management of the module"""
from setuptools import setup

setup(
    name='magic',
    version='1.0',
    description='Test',
    long_description='s',
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    install_requires=[],
)
