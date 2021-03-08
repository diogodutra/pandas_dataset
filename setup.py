
from setuptools import setup, find_packages

setup(name='pdds',
    version='0.0.1',
    description='Pandas expansion to analyze dataset for classifier',
    author='diogodutra',
    url='https://github.com/diogodutra/pandas_dataset',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib'
    ]
)
