from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-api',
    version=version,
    description="ckan extra apis",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='sion.qi',
    author_email='sion.qi@missionsky.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        api = ckanext.api.plugin:APIPlugin

        [paste.paster_command]
        initdb = ckanext.api.command:InitDB
    ''',
)
