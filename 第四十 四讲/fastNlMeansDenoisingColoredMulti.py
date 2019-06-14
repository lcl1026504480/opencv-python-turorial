# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-12 15:36:42
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-12 15:37:31
import numpy as np
import cv2
from matplotlib import pyplot as plt
import imnoise
img = [cv2.imread(str(i) + ".png") for i in range(1, 4)]
noisy = [imnoise.gauss(i, 0, 10) for i in img]
# 下面是加椒盐噪声
# noisy = [imnoise.sp(i) for i in img]
dst = cv2.fastNlMeansDenoisingColoredMulti(noisy, 1, 3, None, 4, 7, 35)
noisy = [cv2.cvtColor(i, cv2.COLOR_BGR2RGB) for i in noisy]
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.subplot(221), plt.imshow(noisy[0])
plt.subplot(222), plt.imshow(noisy[1])
plt.subplot(223), plt.imshow(noisy[2])
plt.subplot(224), plt.imshow(dst)
plt.show()
