import numpy as np
import cv2
from matplotlib import pyplot as plt
import time
import os
path = './chess'
objp = np.zeros((6 * 4, 3), np.float32)
objp[:, :2] = np.mgrid[0:6, 0:4].T.reshape(-1, 2) * 10
op = []
imgpoints = []
for i in os.listdir(path):
    file = '/'.join((path, i))
    a = cv2.imread(file)
    b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(a, (6, 4), None)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    if ret == True:
        corners2 = cv2.cornerSubPix(b, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        op.append(objp)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(op, imgpoints, b.shape[::-1], None, None)
tot_error = 0
for i in range(len(op)):
    imgpoints2, _ = cv2.projectPoints(op[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    tot_error += error
# print(ret, (tot_error / len(op))**0.5)
# cv2.namedWindow('winname', cv2.WINDOW_NORMAL)
# cv2.imshow('winname', a)
# cv2.waitKey(0)
"""下面是校正部分"""
h, w = a.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (h, w), 1)
dst = cv2.undistort(a, mtx, dist, None)
# undistort
mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 4)
dst = cv2.remap(a, mapx, mapy, cv2.INTER_LINEAR)
# crop the image
# x, y, w, h = roi
# dst = dst[y:y + h, x:x + w]
print(mapx.shape)
print(mapy)
a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
# print(roi)
plt.subplot(121), plt.imshow(a), plt.title('source')
plt.subplot(122), plt.imshow(dst), plt.title('undistorted')
plt.show()
