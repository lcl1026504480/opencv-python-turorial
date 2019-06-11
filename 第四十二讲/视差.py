# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-11 11:04:51
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-11 11:14:50
import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread('1.png', 0)  # queryimage # left image
img2 = cv2.imread('16.png', 0)  # trainimage # right image

stereo = cv2.StereoBM.create(numDisparities=16, blockSize=15)
disparity = stereo.compute(img1, img2)
plt.subplot(131)
plt.imshow(img1, 'gray')
plt.subplot(132)
plt.imshow(img2, 'gray')
plt.subplot(133)
plt.imshow(disparity, 'gray')
print(disparity)
plt.show()
