import cv2
import numpy as np
import random as r
def sp(src,p=0.1):
    a=src.copy()
    for i in range(int(a.shape[0]*a.shape[1]*p)):
    	r1=r.randint(0,a.shape[0]-1)
    	r2=r.randint(0,a.shape[1]-1)
    	r3=r.randint(0,1)*255
    	a[r1,r2]=r3
    return a
def gauss(src,means=0,sigma=1):
    a=src.copy()
    rows=a.shape[0]
    cols=a.shape[1]
    for i in range(rows):
        for j in range(cols):
            g=r.gauss(means,sigma)
            r1=np.where((g+a[i,j])>255,255,(g+a[i,j]))
            r2=np.where(r1<0,0,r1)
            a[i,j]=np.round(r2)
    return a