"""
1. build library
    - for example(gfortran in linux): "gfortran -fpic -shared -o example2.so example2.f90"
    - for example(ifort in windows): "ifort /dll example2.f90"
2. run this script
    - python example2.py

Python : 3.6.3
GNU Fortran : 5.4.0
"""
import ctypes
import os

if (os.name == "nt"):
    lib = ctypes.CDLL("./example2.dll")
else:
    lib = ctypes.CDLL("./example2.so")

# スカラー
int_val = ctypes.c_int(3)

# 配列
array_length = 10
int_arr_shape = ctypes.c_int * array_length
int_arr = int_arr_shape(*range(array_length))

# 構造体
class day(ctypes.Structure):
    _fields_ = [("month", ctypes.c_int), ("date", ctypes.c_double)]
today = day(month=6, date=20)

# プロトタイプ宣言
lib.add.restype = ctypes.c_int
lib.add.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

# キャスト
print ("array object type: ", type(int_arr))
for item in int_arr:
    print (item, end=" ")
else:
    print ()

int_arr_casted = ctypes.cast(int_arr, ctypes.POINTER(ctypes.c_int))
print ("casted object type: ", type(int_arr_casted))
for i in range(array_length):
    print (int_arr_casted[i], end=" ")
else:
    print ()
