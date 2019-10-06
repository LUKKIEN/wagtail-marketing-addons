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

install_requires = [
    'wagtail>=2.0',
    'xlrd>=1.2.0',
]

tests_require = [
    # Required for test and coverage
    'pytest',
    'pytest-cov',
    'pytest-django',
    'pytest-pythonpath',
    'coverage',
    'factory-boy',
    'psycopg2>=2.5.4',
    'tox',
    'xlwt==1.2.0',

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
    extras_require={
        'test': tests_require,
        'doc': docs_require,
    },
    install_requires=install_requires,
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
