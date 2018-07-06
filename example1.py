"""
1. build library
    - for example(gfortran in linux): "gfortran -fpic -shared -o example1.so example1.f90"
    - for example(ifort in windows): "ifort /dll example1.f90"
2. run this script
    - python example1.py

Python : 3.6.3
GNU Fortran : 5.4.0
"""
import ctypes
import os

if (os.name == "nt"):
    lib = ctypes.CDLL("./example1.dll")
else:
    lib = ctypes.CDLL("./example1.so")

lib.print_hello()
