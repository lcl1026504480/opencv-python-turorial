# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-14 15:26:11
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-14 15:26:12
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Loading exposure images into a list
img_fn = ["img0.jpg", "img1.jpg", "img2.jpg", "img3.jpg"]
img_list = [cv.imread(fn) for fn in img_fn]
exposure_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)
# Merge exposures to HDR image
merge_debevec = cv.createMergeDebevec()
merge_robertson = cv.createMergeRobertson()
# Estimate camera response function (CRF)
cal_debevec = cv.createCalibrateDebevec()
crf_debevec = cal_debevec.process(img_list, times=exposure_times)
hdr_debevec = merge_debevec.process(img_list, times=exposure_times.copy(), response=crf_debevec.copy())
cal_robertson = cv.createCalibrateRobertson()
crf_robertson = cal_robertson.process(img_list, times=exposure_times)
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy(), response=crf_robertson.copy())

# Tonemap HDR image
tonemap1 = cv.createTonemapDurand(gamma=2.2)
res_debevec = tonemap1.process(hdr_debevec.copy())
tonemap2 = cv.createTonemapDurand(gamma=1.3)
res_robertson = tonemap2.process(hdr_robertson.copy())

# Convert datatype to 8-bit and save
res_debevec_8bit = np.clip(res_debevec * 255, 0, 255).astype('uint8')
res_robertson_8bit = np.clip(res_robertson * 255, 0, 255).astype('uint8')
# res_mertens_8bit = np.clip(res_mertens * 255, 0, 255).astype('uint8')
cv.imwrite("ldr_debevec1.jpg", res_debevec_8bit)
cv.imwrite("ldr_robertson1.jpg", res_robertson_8bit)
# cv.imwrite("fusion_mertens.jpg", res_mertens_8bit)
crf_debevec.shape = 256, 3
crf_robertson.shape = 256, 3
plt.subplot(121), plt.plot(crf_debevec)
plt.subplot(122), plt.plot(crf_robertson)
plt.show()
