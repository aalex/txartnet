#!/usr/bin/env python
"""
txartnet installation script
"""
from setuptools import setup
import txartnet

setup(
    name = "txartnet",
    version = txartnet.__version__,
    author = "Alexandre Quessy",
    author_email = "txartnet@toonloop.com",
    url = "http://github.com/aalex/txartnet",
    description = "Art-Net Protocol for Twisted",
    scripts = [
        "scripts/artnet-receive", 
        "scripts/artnet-send"
        ],
    license="MIT/X",
    packages = ["txartnet", "artnet/test"],
    long_description = """Art-Net is DMX512 over IP.
  """,
    classifiers = [
        "Framework :: Twisted",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
        ]
    )

