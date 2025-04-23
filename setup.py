import os
import sys

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(PROJECT_DIR, 'src'))
from wagtail_marketing import get_version  # noqa isort:skip

docs_require = [
    'mkdocs',
    'pymdown-extensions'
]

tests_require = [
    # Required for test and coverage
    'pytest',
    'pytest-cov',
    'pytest-django',
    'pytest-pythonpath',
    'coverage',
    'factory-boy',
    'psycopg==3.1.18',
    'tox',

    # Linting
    'flake8',
    'isort',
]

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='wagtail-marketing-addons',
    version=get_version().replace(' ', '-'),
    description='A Wagtail add-on for supporting marketeer\'s in daily activities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Lukkien BV',
    author_email='support@lukkien.com',
    url='https://www.lukkien.com/',
    install_requires=[
        'wagtail-modeladmin>2.0.0'
    ],
    extras_require={
        'test': tests_require,
        'doc': docs_require,
    },
    tests_require=tests_require,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 5',
        'Framework :: Wagtail :: 6',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
