#!/usr/bin/env python

from distutils.core import setup

setup(
    name="django-auth-ldap",
    version="1.0b3",
    description="Django LDAP authentication backend",
    long_description="""This is a Django authentication backend that authenticates against an LDAP service. Configuration can be as simple as a single distinguished name template, but there are many rich configuration options for working with users, groups, and permissions.
    
This package requires Python 2.3, Django 1.0, and python-ldap. Suggestions and feature requests are welcome.
    """,
    url="http://packages.python.org/django-auth-ldap/",
    author="Peter Sagerson",
    author_email="psagers@ignorare.net",
    license="BSD",
    packages=["django_auth_ldap"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["django", "ldap", "authentication"],
)
