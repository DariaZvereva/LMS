#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

requirements = map(str.strip, open("requirements.txt").readlines())

setup(
    name="LMS",
    version="0.0.0",
    author="Daria Zvereva",
    author_email="zverevads@gmail.com",
    url="https://github.com/DariaZvereva/LMS",
    license="MIT",
    packages=[
        "lms",
    ],
    install_requires=requirements,
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
        "Flask-SQLAlchemy",
        "Flask-Migrate",
        "SQLAlchemy"
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
