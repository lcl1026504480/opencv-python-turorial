import numpy as np
import cv2
from matplotlib import pyplot as plt
#这个imnoise是我自己封装起来的一个库
import imnoise
# img = cv2.imread('die.png')
img = cv2.imread('1.png')
img = imnoise.gauss(img, 0, 20)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()
