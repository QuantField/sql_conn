from distutils.core import setup
from setuptools import find_packages

setup(
    name="sqlconn",
    version="0.0.1",
    author="Kamel Saadi",
    author_email="saadi.kamel@gmail.com",
    url="https://https://github.com/QuantField/sql_conn/",
    license="MIT",
    packages=find_packages(),    
    description="Wrapper for Sqlite",
    long_description=open("README.rst").read(),
    install_requires=['pandas'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)