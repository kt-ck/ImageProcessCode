import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("coffeeBean.jpg", 0)
width, height = img.shape
rect1 =  [0] * 255

for x in range(width):
    for y in range(height):
        rect1[img[x][y]] += 1
 
total = 0
for i in range(len(rect1)):
    rect1[i] = total + rect1[i] / (width  * height)
    total = rect1[i]
    rect1[i] *= 255

img_process = img.copy()

for x in range(width):
    for y in range(height):
        img_process[x][y] = int(rect1[img_process[x][y]])


plt.hist(img.ravel(), 256, [0, 256])
plt.hist(img_process.ravel(), 256, [0, 256])
plt.show()

cv.namedWindow("show")
cv.imshow("show", img)
cv.waitKey(0)

cv.imshow("show", img_process)
cv.waitKey(0)
cv.destroyAllWindows()
