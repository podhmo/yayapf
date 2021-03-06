# -*- coding:utf-8 -*-
import os
import sys
import fastentrypoints

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'yapf',
]

docs_extras = []

tests_require = []

testing_extras = tests_require + []

setup(
    name='po-yayapf',
    version='0.0.2',
    description='yet another individual yapf',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords='yapf, style format, pep8',
    author="podhmo",
    author_email="ababjam61+github@gmail.com",
    url="https://github.com/podhmo/yayapf",
    packages=find_packages(exclude=["yayapf.tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
    },
    tests_require=tests_require,
    test_suite="yayapf.tests",
    entry_points="""
      [console_scripts]
      yayapf=yayapf:main
"""
)
