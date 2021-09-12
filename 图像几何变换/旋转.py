import cv2 as cv
import math
import numpy as np
import sys
img = cv.imread('T.png', 0)

print(img.shape)


angle = math.pi / 6

#顺时针
# rotate = np.array([[math.cos(angle), -math.sin(angle), 0],[math.sin(angle), math.cos(angle), 0], [0,0,1]])
#逆时针
rotate = np.array([[math.cos(angle), math.sin(angle), 0],[-math.sin(angle), math.cos(angle), 0], [0,0,1]])

# ans = img.copy();
ans = np.zeros([img.shape[0] * 4, img.shape[1] * 4])

basex = img.shape[0] - 1
basey = (img.shape[1] - 1) * 2

for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        r, c, _ = np.array([x, y, 1]) @ rotate

        ans[basex + int(r)][basey + int(c)] = img[x][y]

cv.namedWindow("show")
cv.imshow("show", ans)
cv.waitKey(0)
cv.destroyAllWindows()


