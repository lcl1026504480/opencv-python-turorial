# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-16 21:29:31
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-16 21:29:31
from distutils.core import setup, Extension
module1 = Extension(name=' cmodule', sources=['cfun.cpp'], language='c++')
setup(name='PackageName',
      version='1.0',
      description='This is a demo package',
      ext_modules=[module1])
