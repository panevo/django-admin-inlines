#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8
import os

from setuptools import find_packages, setup

# Get description from Readme file
readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme_file).read()

# Define requirements for the app
REQUIRES = [
    'django>=3.2,<5.3',
]

setup(
    name='django-admin-inlines',
    version="1.1.0",
    description='django-admin-inlines adds actions to each row of the ModelAdmin or InlineModelAdmin. (A fork of django-inline-actions)',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Karlo Krakan',
    author_email='karlo.krakan@panevo.com',
    url='https://github.com/Panevo/django-admin-inlines',
    download_url='https://pypi.python.org/pypi/django-admin-inlines',
    license='BSD',
    packages=find_packages(
        exclude=[
            'test_proj',
        ]
    ),
    include_package_data=True,
    keywords="Django ModelAdmin inline actions",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Internet',
    ],
    install_requires=REQUIRES,
    zip_safe=False,
)
