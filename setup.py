#!/usr/bin/env python

from distutils.core import setup

setup(name='caldwellpy',
      version='1.4.9',
      description='Python Utilities Collection',
      author='Matt Caldwell',
      author_email='matt.caldwell@gmail.com',
      url='https://github.com/mattcaldwell/pyutil',
      packages=['pyutil', 'pyutil.django', 'pyutil.django.templatetags'],
      install_requires=[
          'Django==1.4.5',
          'contextdecorator==0.10.0',
          'mock==1.0.1',
          'requests==1.2.3',
          'wsgiref==0.1.2',
      ]
)
