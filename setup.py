import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
  README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name='django-eventlog',
  version='0.1',
  packages=['eventlog'],
  include_package_data=True,
  license='Non free software',
  description='A custom made non stable event logging package for Django.',
  long_description=README,
  url='',
  author='Jean-Daniel Michaud',
  author_email='jean.daniel.michaud@gmail.com',
  classifiers=[
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
#    'License :: OSI Approved :: BSD License', # example license
    'License :: Non Free',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    # Replace these appropriately if you are stuck on Python 2.
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
  ],
)
