#!/usr/bin/python
# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8
import os
import sys

from setuptools import find_packages, setup

# Get description from Readme file
readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme_file).read()

# Build a list with requirements of the app
REQUIRES = []
try:
    pass
except ImportError:
    # Because of the strange update behavior of "pip --upgrade package_name"
    # set requierment only if django not avallible.
    REQUIRES.append('django')

if sys.version_info < (3, 8):
    REQUIRES.append('python >= 3.8')


setup(name='django-admin-inlines',
      version=1.0,
      description='django-admin-inlines adds actions to each row of the ModelAdmin or InlineModelAdmin',
      long_description_content_type='text/markdown',
      long_description=long_description,
      author='Karlo Krakan',
      author_email='karlo.krakan@panevo.com',
      url='https://github.com/karlokr-p/django-admin-inlines',
      download_url='https://pypi.python.org/pypi/django-admin-inlines',
      license='BSD',
      packages=find_packages(exclude=['test_proj', ]),
      include_package_data=True,
      keywords="Django ModelAdmin inline actions",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django :: 3.0',
          'Framework :: Django :: 4.0',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Environment :: Console',
          'Natural Language :: English',
          'Intended Audience :: Developers',
          'Topic :: Internet',
      ],
      install_requires=REQUIRES,
      zip_safe=False,
      )
