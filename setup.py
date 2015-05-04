#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       $Id: setup.py 71 2010-05-07 10:13:45Z jraedler $   

# withNumPy enables some extensions:
#  * faster adding of contours from NumPy arrays
#  * data style STYLE_NUMPY to get contours and TriStrips
#    as NumPy arrays
withNumPy=True

# if withNumPy is True, set the include path for numpy/arrayobject.h
# the example is for python-x,y on Windows:
# numPyIncludePath='C:\\Python25\\Lib\\site-packages\\numpy\\core\\include'
import numpy
numPyIncludePath=numpy.get_include()

# defaultStyle may be used to set the default style to one of:
#  * STYLE_TUPLE to get tuples of points
#  * STYLE_LIST to get lists of points
#  * STYLE_NUMPY to get points as NumPy array
#    withNumPy must be enabled for this!
defaultStyle='STYLE_LIST'

# ------ no changes below! If you need to change, it's a bug! -------
from distutils.core import setup, Extension
from sys import platform

mac = [('DEFAULT_STYLE', defaultStyle)]
inc = ['src']

if withNumPy:
    try:
        import numpy
        print "Using NumPy extension"
        mac.append(('WITH_NUMPY', 1))
    except:
        print "NumPy extension not found!"

# alloca() needs malloc.h under Windows
if platform == 'win32':
    mac.append(('SYSTEM_WIN32', 1))

if withNumPy and numPyIncludePath:
    inc.append(numPyIncludePath)

longdesc = """THIS IS A VERSION WHICH WORKS WITH PYTHON-2.x ONLY!

Polygon is a python package that simplifies the handling of polygons in 2D. 
It contains Python bindings for gpc, the excellent General Polygon Clipping 
Library by Alan Murta and some extensions written in C and pure Python. With 
Polygon you may handle complex polygonal areas in Python in a very intuitive 
way. Polygons are simple Python objects, clipping operations are bound to 
standard operators like +, -, \|, & and ^. TriStrips can be constructed from 
Polygons with a single statement. Functions to compute the area, center point, 
convex hull and much more are included.

The gpc homepage is located at http://www.cs.man.ac.uk/~toby/alan/software/ .

The wrapping and extension code is free software, but the core gpc library is
free for non-commercial usage only. The author says:

    GPC is free for non-commercial use only. We invite non-commercial users 
    to make a voluntary donation towards the upkeep of GPC.
    
    If you wish to use GPC in support of a commercial product, you must obtain 
    an official GPC Commercial Use Licence from The University of Manchester.

Please respect this statement and contact the author (see gpc homepage) if you
wish to use this software in commercial projects!
"""


args = { 
    'name'            : "Polygon",
    'version'         : "2.0.2.2",
    'description'     : "Polygon eases the handling of 2D-polygons including very fast clipping operations",
    'long_description': longdesc,
    'license'         : "LGPL for Polygon, other for gpc",
    'author'          : "Joerg Raedler",
    'author_email'    : "jr@j-raedler.de",
    'maintainer'      : "Mario Juric",
    'maintainer_email': "mjuric@cfa.harvard.edu",
    'url'             : "http://nebel.rc.fas.harvard.edu/mjuric/lsd/sources/",
    'download_url'    : "http://nebel.rc.fas.harvard.edu/mjuric/lsd/sources/",
    'classifiers'     : ['Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers',
        'Intended Audience :: Science/Research', 
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 
        'License :: Other/Proprietary License', 'Programming Language :: C', 
        'Programming Language :: Python :: 2', 'Programming Language :: Python :: 2.5', 
        'Programming Language :: Python :: 2.6', 'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows', 'Operating System :: MacOS :: MacOS X',
        'Topic :: Scientific/Engineering :: Mathematics', 
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    'packages'        : ['Polygon'],
    'ext_modules'     : [Extension('Polygon.cPolygon', ['src/gpc.c', 'src/cPolygon.c', 'src/PolyUtil.c'],
                        include_dirs=inc, define_macros=mac)]
}

setup(**args)
