import cv2
import numpy as np
from matplotlib import pyplot as plt
n = []


def getcolor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        c = b[y, x][:2]
        c[0] = c[0] / 180 * 5
        c[1] = c[1] / 255
        n.append(c)


a = cv2.imread('x1.png')
b = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
while(1):
    cv2.imshow('x1', a)
    cv2.setMouseCallback('x1', getcolor)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
m = np.array(n).mean(0)
s = []
for i in range(1, 7):
    n = []
    a = cv2.imread('n' + str(i) + '.png')
    while(1):
        cv2.imshow('n' + str(i), a)
        cv2.setMouseCallback('n' + str(i), getcolor)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    k = np.array(n).mean(0)
    s.append(((k - m)**2).sum())

xn = np.array(s).argmin()
print(xn)
r = {0: '一花是天！', 1: '二乃是天！', 2: '三玖是天！！！', 3: '四叶是天！', 4: '五月是天！！', 5: '二乃是天！！'}
print(r[xn])
