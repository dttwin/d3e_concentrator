# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Traffic data concentrator - OpenAPI 3.0",
    author_email="d3e@fd.cvut.cz",
    url="",
    keywords=["Swagger", "Traffic data concentrator - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is a development Swagger-supported server based on the OpenAPI 3.0 specification. You can find out more about Swagger at  [https://swagger.io](https://swagger.io).
    """
)
