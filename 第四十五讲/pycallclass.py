# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-14 21:38:54
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-14 21:38:54
import ctypes
so = ctypes.cdll.LoadLibrary
lib = so("./libpycallclass.so")
print('display()')
lib.display()
print('display(100)')
lib.display_int(100)
