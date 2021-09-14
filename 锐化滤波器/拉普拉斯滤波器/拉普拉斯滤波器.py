import cv2 as cv
import numpy as np

img = cv.imread("../../img/face.jpg", 0)

c = -1

img_process = np.pad(img, ((1, ),(1, )), 'constant', constant_values=0)

new_img = img.copy()
for x in range(1, img_process.shape[0] - 1):
    for y in range(1, img_process.shape[1] - 1 ):
        temp = new_img[x - 1][y-1] + c * (img_process[x][y-1] + img_process[x][y+1]+img_process[x-1][y]
                                          +img_process[x+1][y] - img_process[x][y])
        
        if temp > 255:
            temp = 255
        elif temp < 0:
            temp = 0
        new_img[x-1][y-1] = temp
        

cv.namedWindow("show")
cv.imshow("show", new_img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("processedImg_c_{}.png".format(c), new_img)