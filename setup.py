#!/usr/bin/end python

#
#  setup.py
#  
#  Copyright (C) 2019, Universidade Federal de Santa Catarina
#  
#  This file is part of FloripaSat-Decoder.
#
#  FloripaSat-Decoder is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-Decoder is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-Decoder; if not, see <http://www.gnu.org/licenses/>.
#  
#

__author__      = "Gabriel Mariano Marcelino - PU5GMA"
__copyright__   = "Copyright (C) 2019, Universidade Federal de Santa Catarina"
__credits__     = ["Gabriel Mariano Marcelino - PU5GMA"]
__license__     = "GPL3"
__version__     = "0.1.12"
__maintainer__  = "Gabriel Mariano Marcelino - PU5GMA"
__email__       = "gabriel.mm8@gmail.com"
__status__      = "Development"


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name                            = "fsat-decoder",
    version                         = "0.1.0",
    author                          = "Gabriel Mariano Marcelino",
    author_email                    = "gabriel.mm8@gmail.com",
    description                     = "FloripaSat-I packet decoder",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    license                         = "GPLv3",
    url                             = "https://github.com/floripasat/fsat-decoder",
    packages                        = setuptools.find_packages(),
    install_requires                = ['gi','scipy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
