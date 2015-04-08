from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-geometry',
    version=version,
    description="Loading GeoJSON Data",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='sion qi',
    author_email='sion.qi@missionsky.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.geometry'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.geometry.plugin:PluginClass
        geometry = ckanext.geometry.plugin:GeoPlugin

        [paste.paster_command]
        initdb = ckanext.geometry.command:InitDB
    ''',
)
