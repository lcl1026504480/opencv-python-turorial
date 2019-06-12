# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-12 13:13:12
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-12 13:14:07
import numpy as np
import cv2 as cv
img = cv.imread('1.png')
Z = img.reshape((-1, 3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv.imshow('res2', res2)
cv.waitKey(0)
cv.destroyAllWindows()
