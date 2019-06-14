# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-13 09:42:36
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-13 09:42:37
import cv2
from matplotlib import pyplot as plt
src = cv2.imread('src.jpg')  # 默认的彩色图(IMREAD_COLOR)方式读入原始图像
mask = cv2.imread('mask.jpg', cv2.IMREAD_GRAYSCALE)  # 灰度图(IMREAD_GRAYSCALE)方式读入水印蒙版图像

# 参数：目标修复图像; 蒙版图（定位修复区域）; 选取邻域半径; 修复算法(包括INPAINT_TELEA/INPAINT_NS， 前者算法效果较好)
dst1 = cv2.inpaint(src, mask, 7, cv2.INPAINT_TELEA)
dst2 = cv2.inpaint(src, mask, 7, cv2.INPAINT_NS)
plt.subplot(221), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title("src")
plt.subplot(222), plt.imshow(mask, cmap="gray"), plt.title("mask")
plt.subplot(223), plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)), plt.title("TELEA")
plt.subplot(224), plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB)), plt.title("NS")
plt.show()
