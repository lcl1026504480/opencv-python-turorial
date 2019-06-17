# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-15 16:20:21
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-15 16:22:18
from distutils.core import setup, Extension

MOD = 'Extest'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['Extest.c'])])
