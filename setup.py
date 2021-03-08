import os
from setuptools import setup

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('requirements.txt').splitlines()

setup(name='pdds',
      version='0.0.1',
      description='Pandas extension for analysis of dataset for classification',
      url='https://github.com/diogodutra/pandas_dataset',
      author='Diogo Dutra',
      author_email='diogodutra@gmail.com',
      license='Apache License, Version 2.0',
      packages=['pdds'],
      package_data={
        'pyAudioAnalysis': ['dataset.py']
      },
      zip_safe=False,
      install_requires=requirements,
      )
