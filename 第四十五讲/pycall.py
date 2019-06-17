# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-14 21:18:15
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-14 21:18:16
import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("./libpycall.so")
lib.foo(1, 3)
print('***finish***')
