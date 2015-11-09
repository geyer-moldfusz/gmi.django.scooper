from setuptools import setup, find_packages
import sys, os

version = '0.1'

requires = [
    'Django',
    'PyYAML',
    'githubpy',
    'setuptools',
]

setup(name='gmi.django.scooper',
      version=version,
      description="Collects posting from various external sources.",
      long_description="""\
xxx long description""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django scooper',
      author='Stefan Walluhn',
      author_email='stefan@neuland.io',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['gmi', 'gmi.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
