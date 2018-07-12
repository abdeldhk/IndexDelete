#!/usr/bin/env python

import os
from setuptools import setup, find_packages
import ConfigParser

config = ConfigParser.RawConfigParser()
#config.read(os.path.join(os.path.dirname(__file__), "app.properties"))
version = config.get('package', 'version')

setup(name='PurgeIndex',
      version=version,
      author='Abdelhamid DAHAK',
      author_email='abdelhamid.dahak@amadeus.com',
      packages=find_packages(),
      description='Purging Index ', 
      package_data={'resources': ['*.xsd', '*.xml', '*.properties']},
      include_package_data=True,
      install_requires=['pyxb',
            'python-dateutil',
            'nose2',
            'PyInstaller',
            'httpretty',
            'glob2'],
      )
