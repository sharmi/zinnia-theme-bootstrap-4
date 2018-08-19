"""Setup script for zinnia-theme-bootstrap4"""
from setuptools import setup
from setuptools import find_packages

import zinnia_bootstrap4

setup(
    name='zinnia-theme-bootstrap-4',
    version=zinnia_bootstrap4.__version__,

    description='Bootstrap 4 theme for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, theme, skin, bootstrap, bootstrap 4',

    author=zinnia_bootstrap4.__author__,
    author_email=zinnia_bootstrap4.__email__,
    url=zinnia_bootstrap4.__url__,

    packages=find_packages(exclude=['demo_zinnia_bootstrap']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_bootstrap4.__license__,
    include_package_data=True,
    zip_safe=False
)
