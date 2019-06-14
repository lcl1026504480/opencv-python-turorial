# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-14 14:53:51
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-14 15:06:46
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
a = cv.imread("img3.jpg")
plt.subplot(121)
plt.imshow(cv.cvtColor(a, cv.COLOR_BGR2RGB))
b = cv.cvtColor(a, cv.COLOR_BGR2HSV)
h, s, v = cv.split(b)
v1 = cv.equalizeHist(v)
c = cv.merge([h, s, v1])
c = cv.cvtColor(c, cv.COLOR_HSV2RGB)
plt.subplot(122)
plt.imshow(c)
plt.show()
