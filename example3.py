"""
1. build library
    - for example(gfortran in linux): "gfortran -fpic -shared -o example3.so example3.f90"
    - for example(ifort in windows): "ifort /dll example3.f90"
2. run this script
    - python example3.py

Python : 3.6.3
GNU Fortran : 5.4.0
"""
import ctypes
import os

if (os.name == "nt"):
    lib = ctypes.CDLL("./example3.dll")
else:
    lib = ctypes.CDLL("./example3.so")

# 構造体
class day_type(ctypes.Structure):
    _fields_ = [("month", ctypes.c_int), ("date", ctypes.c_int)]
input_day = day_type(month=6, date=20)

# スカラー
input_val = ctypes.c_int(3)

# 配列
array_length = 10
input_arr_shape = ctypes.c_int * array_length
input_arr = input_arr_shape(*range(array_length))

# プロトタイプ宣言
lib.input.restype = None
lib.input.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), \
                    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(day_type)]

if __name__=="__main__":

    print ("--- input ---")
    input_arr_pointer = ctypes.cast(input_arr, ctypes.POINTER(ctypes.c_int))
    lib.input(ctypes.byref(input_val), ctypes.byref(ctypes.c_int(array_length)), \
              input_arr_pointer, ctypes.byref(input_day))
