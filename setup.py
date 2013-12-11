#!/usr/bin/env python

from distutils.core import setup

setup(name='hypchat',
      version='0.1',
      description="Package for HipChat's v2 API",
      author='James Bliss',
      author_email='james@ridersdiscount.com',
      url='https://github.com/RidersDiscountCom/HypChat',
      packages=['hypchat'],
      requires=['requests'],
      classifiers=[ # https://pypi.python.org/pypi?%3Aaction=list_classifiers
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            #FIXME: License
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2 :: Only',
            'Topic :: Communications :: Chat',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
      ]
     )