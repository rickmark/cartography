#!/usr/bin/env python3

from setuptools import setup

setup(
    name='cartography',
    version='1.0.0',
    url='https://github.com/rickmark/cartography',
    license='MIT',
    author='rickmark',
    author_email='rickmark@outlook.com',
    description='Example Geo-coding Service',
    install_requires=[
        'flask-restful',
        'flask',
        'redis',
        'python-consul',
        'googlemaps',
        'censusgeocode'
    ]
)



## Test for consul, redis, that they are started, register redis in consul