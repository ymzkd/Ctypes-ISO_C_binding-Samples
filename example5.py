"""
1. build library
    - for example(gfortran in linux): "gfortran -fpic -shared -o example5.so example5.f90"
    - for example(ifort in windows): "ifort /dll example5.f90"
2. run this script
    - python example5.py

Python : 3.6.3
GNU Fortran : 5.4.0
"""
import numpy as np
import ctypes
import os

if (os.name == "nt"):
    lib = ctypes.CDLL("./example5.dll")
else:
    lib = ctypes.CDLL("./example5.so")

class result(ctypes.Structure):
    _fields_ =[("len", ctypes.c_int), ("arr", ctypes.POINTER(ctypes.c_int))]

# プロトタイプ宣言: ndpointerの利用
lib.extruct_plus.restype = result
lib.extruct_plus.argtypes = [ctypes.POINTER(ctypes.c_int), np.ctypeslib.ndpointer(dtype=np.int32, ndim=1)]

lib.delete_array.restype = None
lib.delete_array.argtypes = [ctypes.POINTER(ctypes.c_int), np.ctypeslib.ndpointer(dtype=np.int32, ndim=1)]

if __name__=="__main__":
    array_length = 10
    arr_np = np.random.randint(low=-100, high=100, size=array_length, dtype=np.int32)

    print ("--- extruct_plus ---")
    result = lib.extruct_plus(ctypes.byref(ctypes.c_int(array_length)), arr_np)

    # 返り値のCポインタからas_arrayによりNumpy配列作成
    result_len = result.len
    result_vec = np.ctypeslib.as_array(result.arr, shape=(result_len,))
    print ("inputs : ", end="")
    for i in arr_np: print (i, end=" ")

    print ("\nresult : ", end="")
    for i in result_vec: print (i, end=" ")
    print ("\n")

    print ("--- delete_array ---")
    lib.delete_array(ctypes.byref(ctypes.c_int(result_len)), result_vec)
