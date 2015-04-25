import os
from setuptools import setup

LONG_DESCRIPTION = """GC-Prometheus

Exports metrics about the Python garbage collector for Prometheus.io.

See https://github.com/korfuri/python-gc-prometheus for usage
instructions.
"""

setup(
    name="gc-prometheus",
    version="0.1.0",
    author="Uriel Corfa",
    author_email="uriel@corfa.fr",
    description=(
        "Exports garbage collection metrics for Prometheus.io."),
    license="Apache",
    keywords="python gc monitoring prometheus",
    url="http://github.com/korfuri/python-gc-prometheus",
    packages=["gc_prometheus"],
    test_suite="tests",
    long_description=LONG_DESCRIPTION,
    install_requires=[
        "prometheus_client>=0.0.9",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: Apache Software License",
    ],
)
