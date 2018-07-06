"""
1. build library
    - for example(gfortran in linux): "gfortran -fpic -shared -o example6.so example6.f90"
    - for example(ifort in windows): "ifort /dll example6.f90"
2. run this script
    - python example6.py

Python : 3.6.3
GNU Fortran : 5.4.0
"""
import numpy as np
import ctypes
import os

if (os.name == "nt"):
    lib = ctypes.CDLL("./example6.dll")
else:
    lib = ctypes.CDLL("./example6.so")

class result(ctypes.Structure):
    _fields_ =[("len", ctypes.c_int)]

# プロトタイプ宣言
lib.extruct_plus.restype = result
lib.extruct_plus.argtypes = [ctypes.POINTER(ctypes.c_int), np.ctypeslib.ndpointer(dtype=np.int32, ndim=1)]

lib.get_array.restype = None
lib.get_array.argtypes = [ctypes.POINTER(ctypes.c_int), np.ctypeslib.ndpointer(dtype=np.int32, ndim=1)]

lib.delete_array.restype = None
lib.delete_array.argtypes = []

if __name__=="__main__":
    array_length = 10
    arr_np = np.random.randint(low=-100, high=100, size=array_length, dtype=np.int32)

    print ("--- extruct_plus ---")
    result = lib.extruct_plus(ctypes.byref(ctypes.c_int(array_length)), arr_np)

    result_len = result.len
    result_vec = np.zeros(result_len, dtype=np.int32)
    print ("inputs : ", end="")
    for i in arr_np: print (i, end=" ")
    print ("\n")

    print ("--- get_array ---")
    lib.get_array(ctypes.byref(ctypes.c_int(result_len)), result_vec)

    print ("\nresult : ", end="")
    for i in result_vec: print (i, end=" ")
    print ("\n")

    print ("--- delete_array ---")
    lib.delete_array()
