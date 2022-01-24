import cv2 as cv
import numpy as np
import math
img = cv.imread("../../img/face.jpg", 0)

img_process = np.pad(img, ((1, ),(1, )), 'constant', constant_values=0)

new_img = img.copy()
for x in range(1, img_process.shape[0] - 1):
    for y in range(1, img_process.shape[1] - 1 ):
        temp = abs(img_process[x-1][y-1] + 2*img_process[x][y-1] + img_process[x+1][y-1]-img_process[x][y+1]
                        -2*img_process[x][y+1]-img_process[x+1][y+1]) + abs(img_process[x-1][y-1] + 2*img_process[x-1][y] + img_process[x-1][y+1]-img_process[x+1][y-1]
                        -2*img_process[x+1][y]-img_process[x+1][y+1])
                                         
        if temp > 255:
            temp = 255
            
        new_img[x - 1][y-1] = temp;
        

cv.imwrite("process.png", new_img)

