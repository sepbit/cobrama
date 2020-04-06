#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Covid19BR - Report COVID-19 Brasil on Mastodon
Copyright (C) 2020  Sepbit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup

with open('README.md', 'r') as f:
    README = f.read()

setup(
    name='sepbit.covid19br',
    version='1.0.0',
    description='Report COVID-19 Brasil on Mastodon',
    long_description=README,
    license='GPL-3.0-or-later',
    keywords='Sepbit COVID-19 Mastodon',
    author='Vitor Guia',
    maintainer='Sepbit',
    maintainer_email='contato@sepbit.com',
    author_email='contato@vitor.guia.nom.br',
    url='https://gitlab.com/sepbit/covid19br',
    packages=['sepbit.covid19br'],
    python_requires='~=3.7',
    install_requires=['setuptools', 'Mastodon.py'],
    # $ pip install sampleproject[dev]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    test_suite='test',
    entry_points={
        'console_scripts': [
            'covid19br=sepbit.covid19br.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 \
        or later (GPLv3+)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    zip_safe=False,
)
