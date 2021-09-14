import cv2 as cv
import numpy as np

img = cv.imread("../../img/face.jpg", 0)

kernel_size = 3
kernel = np.array([[1,2,1],[2,4,2],[1,2,1]])

padding_width = int(kernel_size / 2)
img_process = np.pad(img, ((padding_width,),(padding_width,)), 'constant', constant_values=0)
new_img = img.copy()

for x in range(padding_width, img_process.shape[0] - padding_width):
    for y in range(padding_width , img_process.shape[1] - padding_width):
        new_img[x - padding_width][y - padding_width] = int(np.sum(img_process[x - padding_width: x + padding_width + 1,y - padding_width: y + padding_width +1] * kernel) / 16)
        

template = img - new_img
cv.imwrite("template.png", template)

img_process = img + template
cv.imwrite("ans.png", img_process)