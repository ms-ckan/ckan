from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-faq',
    version=version,
    description="Frequently Asked Questions",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='sion.qi',
    author_email='sion.qi@missionsky.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.faq'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        faq=ckanext.faq.plugin:FAQPlugin
    ''',
)
