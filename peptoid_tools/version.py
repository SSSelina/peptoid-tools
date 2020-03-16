from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = 'dev1'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

with open('README.md') as readme_file:
    README = readme_file.read()

NAME = "peptoid_tools"
MAINTAINER = "Orion Dollar, Sarah Alamdari"
MAINTAINER_EMAIL = "salamda1@uw.edu"
DESCRIPTION = "Tool for building heirarchical assemblies for MD"
URL = "https://github.com/oriondollar/peptoid-tools"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Orion Dollar, Sarah Alamdari"
AUTHOR_EMAIL = "salamda1@uw.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'peptoid-tools': [pjoin('res_lib', '*')]}
REQUIRES = ['pandas', 'numpy']
