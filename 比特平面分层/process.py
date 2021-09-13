import cv2 as cv
import numpy as np
img = cv.imread("face.jpg", 0)

width = img.shape[0]
height = img.shape[1]
img_list = [np.where(img >= 128, 1, 0),
            np.where(np.logical_and(128>img, img >= 64), 1, 0),
            np.where(np.logical_and(64>img, img >= 32), 1, 0),
            np.where(np.logical_and(32>img, img >= 16), 1, 0)]

cv.namedWindow("show")
for each in img_list:
    # print(each.shape)
    show_img = np.where(each == 1, 255, 0).astype(np.uint8)
    cv.imshow("show", show_img)
    cv.waitKey(0)
    

p = 128
img_combine = (img_list[0] * p).astype(np.uint8)

for i in range(1, len(img_list)):
    p = p / 2
    img_combine += (img_list[i] * p).astype(np.uint8)

cv.imshow("show", img_combine)
cv.waitKey(0)

cv.imshow("show", img)
cv.waitKey(0)
cv.destroyAllWindows()




