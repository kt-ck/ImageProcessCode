import cv2 as cv
import numpy as np
img = cv.imread("face.jpg", 0)

width = img.shape[0]
height = img.shape[1]
img_list = [np.where(img & 128 == 128, 1, 0),
            np.where(img & 64 == 64, 1, 0),
            np.where(img & 32 == 32, 1, 0),
            np.where(img & 16 == 16, 1, 0)]

cv.namedWindow("show")
for each in img_list:
    # print(each.shape)
    show_img = np.where(each == 1, 255, 0).astype(np.uint8)
    cv.imshow("show", show_img)
    cv.waitKey(0)
    

p = 128
img_combine = np.zeros((width, height)).astype(np.uint8)

for i in range(len(img_list)):
    img_combine += (img_list[i] * p).astype(np.uint8)
    p /= 2

cv.imshow("show", img_combine)
cv.waitKey(0)

cv.imshow("show", img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("process.png", img_combine)
cv.imwrite("gray.png", img)




