# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-12 21:15:16
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-12 21:31:47
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi.png')
mask = cv2.imread('mask.png', 0)
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
# dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.imshow(mask, cmap='gray')
plt.subplot(133), plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()
