# This is purely the result of trial and error.

import sys
import codecs

from setuptools import setup, find_packages

import pdds


install_requires = [
    'requests[socks]>=2.22.0',
    'Pygments>=2.5.2',
    'requests-toolbelt>=0.9.1',
]
install_requires_win_only = [
    'colorama>=0.2.4',
]

# Conditional dependencies:

# sdist
if 'bdist_wheel' not in sys.argv:

    if 'win32' in str(sys.platform).lower():
        # Terminal colors for Windows
        install_requires.extend(install_requires_win_only)


# bdist_wheel
extras_require = {
    # https://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    ':sys_platform == "win32"': install_requires_win_only,
}


def long_description():
  return 'Long description'


setup(
    name='pdds',
    download_url='https://github.com/diogodutra/pandas_dataset/archive/main.tar.gz',
    packages=find_packages(),
    python_requires='>=3.6',
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
    project_urls={
        'GitHub': 'https://github.com/diogodutra/pandas_dataset',
    },
)
