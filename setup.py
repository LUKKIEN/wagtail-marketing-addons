import os
import sys

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(PROJECT_DIR, 'src'))
from wagtail_marketing import get_version  # noqa isort:skip

deploy_require = [
    'twine',
]

docs_require = [
    'mkdocs',
]

tests_require = [
    # Required for test and coverage
    'pytest',
    'pytest-cov',
    'pytest-django',
    'coverage',
    'factory-boy',
    'psycopg2>=2.5.4',
    'tox',
    # Linting
    'flake8',
    'isort',
]

setup(
    name='wagtail-marketing-addons',
    version=get_version().replace(' ', '-'),
    description='A Wagtail add-on for supporting marketeers in daily activities',
    author='Lukkien BV',
    author_email='support@lukkien.com',
    url='https://www.lukkien.com/',
    extras_require={
        'test': tests_require,
        'doc': docs_require,
        'deploy': deploy_require,
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
