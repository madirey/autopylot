#!/usr/bin/env python

from distutils.core import setup

setup(name='caldwellpy',
      version='1.4.1',
      description='Python Utilities Collection',
      author='Matt Caldwell',
      author_email='matt.caldwell@gmail.com',
      url='https://github.com/mattcaldwell/pyutil',
      packages=['pyutil', 'pyutil.django', 'pyutil.django.templatetags']
)
