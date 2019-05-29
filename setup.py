"""
Five One One
-------------

A python API to consume transit data from http://511.org.
"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fiveoneone',
    version='0.5.0',
    license='MIT',
    author='Ramiro Berrelleza',
    author_email='rberrelleza@gmail.com',
    description='A python API to consume transit data from http://511.org.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rberrelleza/511-transit',
    packages=['fiveoneone'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['requests>=2.22'],
    entry_points={
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
