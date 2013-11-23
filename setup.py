#!/usr/bin/env python

from distutils.core import setup

setup(name='autopylot',
      version='1.9.5',
      description='Put your Python on autopylot.',
      author='Matt Caldwell',
      author_email='matt.caldwell@gmail.com',
      url='https://github.com/mattcaldwell/autopYlot',
      packages=['autopylot', 'autopylot.django', 'autopylot.django.templatetags'],
      install_requires=[
          'Django==1.4.5',
          'coverage==3.6',
          'mock==1.0.1',
          'nose==1.3.0',
          'requests',
          'wsgiref==0.1.2',
      ]
)
