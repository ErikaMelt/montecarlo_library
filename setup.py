#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Erika Ortiz",
    author_email='erikapaolaortiz@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Booststrapping and Permutations testing",
    entry_points={
        'console_scripts': [
            'montecarlo=montecarlo.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='montecarlo',
    name='montecarlo',
    packages=find_packages(include=['montecarlo', 'montecarlo.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ErikaMelt/montecarlo_library',
    version='0.1.0',
    zip_safe=False,
)
