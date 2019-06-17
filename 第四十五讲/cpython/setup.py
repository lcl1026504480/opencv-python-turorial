# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-16 21:51:09
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-16 21:51:15
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/5/8 9:09
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : setup.py
'''
@Description: setup.py for hello.pyx
'''
from Cython.Build import cythonize
from distutils.core import setup

# 编写setup函数
setup(
    name = "Hello",
    ext_modules = cythonize("hello.pyx")
)