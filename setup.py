from setuptools import setup, find_packages

setup(
    name="sqlconn",
    version="0.0.1",
    author="Kamel Saadi",
    author_email="saadi.kamel@gmail.com",
    url="https://github.com/QuantField/sql_conn/", 
    license="MIT",
    packages=find_packages(),    
    package_dir={"sqlconn": "sqlconn"},
    package_data={"sqlconn": ["data/*.csv"]},
    description="Wrapper for Sqlite",
    long_description="Wrapper for Sqlite",
    install_requires=['pandas'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)

