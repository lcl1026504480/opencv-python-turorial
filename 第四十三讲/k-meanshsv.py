# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-12 13:17:42
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-12 13:17:43
import numpy as np
import cv2 as cv
img = cv.imread('1.png')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
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
res2 = cv.cvtColor(res2, cv.COLOR_HSV2BGR)
cv.imshow('res2', res2)
cv.waitKey(0)
cv.destroyAllWindows()
