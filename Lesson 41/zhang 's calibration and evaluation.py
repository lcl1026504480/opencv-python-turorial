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
    print(file)
    a = cv2.imread(file)
    b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(a, (6, 4), None)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    if ret == True:
        corners2 = cv2.cornerSubPix(b, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        op.append(objp)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(op, imgpoints, b.shape[::-1], None, None)
print(ret)
print(mtx)
print(len(rvecs), rvecs[0])
print(len(tvecs), rvecs[0])
tot_error = 0
for i in range(len(op)):
    imgpoints2, _ = cv2.projectPoints(op[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)
    tot_error += error
print(tot_error / 24)
# cv2.namedWindow('winname', cv2.WINDOW_NORMAL)
# cv2.imshow('winname', a)
# cv2.waitKey(0)
