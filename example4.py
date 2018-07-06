"""
1. build library
    - for example(gfortran in linux): "gfortran -fpic -shared -o example4.so example4.f90"
    - for example(ifort in windows): "ifort /dll example4.f90"
2. run this script
    - python example4.py

Python : 3.6.3
GNU Fortran : 5.4.0
"""
import ctypes
import os

if (os.name == "nt"):
    lib = ctypes.CDLL("./example4.dll")
else:
    lib = ctypes.CDLL("./example4.so")

# プロトタイプ宣言
lib.sum_all_sub.restype = None
lib.sum_all_sub.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), \
                               ctypes.POINTER(ctypes.c_int)]

lib.sum_all_func.restype = ctypes.c_int
lib.sum_all_func.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

lib.shift_all_sub.restype = None
lib.shift_all_sub.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), \
                              ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

lib.shift_all_func.restype = ctypes.POINTER(ctypes.c_int)
lib.shift_all_func.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), \
                               ctypes.POINTER(ctypes.c_int)]

lib.delete_array.restype = None
lib.delete_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

if __name__=="__main__":
    offset = 3
    array_length = 10
    input_arr_shape = ctypes.c_int * array_length
    input_arr = input_arr_shape(*range(array_length))
    input_arr_pointer = ctypes.cast(input_arr, ctypes.POINTER(ctypes.c_int))

    result_arr = input_arr_shape()
    result_arr_pointer = ctypes.cast(result_arr, ctypes.POINTER(ctypes.c_int))

    print ("--- sum_all_sub ---")
    result_val = ctypes.c_int()
    lib.sum_all_sub(ctypes.byref(ctypes.c_int(array_length)), \
                    input_arr_pointer, ctypes.byref(result_val))
    print ("input : ", end="")
    for item in input_arr: print (item, end=" ")
    print ("\nresult : ", result_val.value, end="\n\n")

    print ("--- sum_all_func ---")
    result_val = lib.sum_all_func(ctypes.byref(ctypes.c_int(array_length)), \
                                  input_arr_pointer)
    print ("input : ", end="")
    for item in input_arr: print (item, end=" ")
    print ("\nresult : ", result_val, end="\n\n")

    print ("--- shift_all_sub ---")
    lib.shift_all_sub(ctypes.byref(ctypes.c_int(offset)), ctypes.byref(ctypes.c_int(array_length)), \
              input_arr_pointer, result_arr_pointer)
    print ("inputs : ")
    print ("  offset : ", offset)
    print ("  array : ", end="")
    for item in input_arr: print (item, end=" ")
    print ("\nresult : ", end="")
    for item in result_arr: print (item, end=" ")
    print ("\n")

    print ("--- shift_all_func ---")
    result_arr = lib.shift_all_func(ctypes.byref(ctypes.c_int(offset)), \
        ctypes.byref(ctypes.c_int(array_length)), input_arr_pointer)
    print ("inputs : ")
    print ("  offset : ", offset)
    print ("  array : ", end="")
    for item in input_arr: print (item, end=" ")
    print ("\nresult : ", end="")
    for i in range(array_length): print (result_arr[i], end=" ")
    print ("\n")

    print ("--- delete_array ---")
    lib.delete_array(ctypes.byref(ctypes.c_int(array_length)), result_arr)
