import cv2 as cv
import numpy as np

img = cv.imread("face.jpg", 0)


mean_G = np.mean(img)
std_G = np.std(img)

E = 4
k0 = 0.4
k1 = 0.02
k2 = 0.4

img_process = img.copy()

for i in range(img_process.shape[0]):
    for j in range(img_process.shape[1]):
        total = 0
        num = []
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if m >= 0 and m < img_process.shape[0] and 0<= n < img_process.shape[1]:
                    total += img[m][n]
                    num.append(img[m][n])
        
        mean = total / len(num)
        std = 0
        for each in num:
            std += (each - mean)**2
            
        std /= len(num)
        
        if mean <= k0 * mean_G and k1 * std_G <= std <= k2 * std_G:
            img_process[i][j] *= E
                    
cv.namedWindow("show")
cv.imshow("show", img)
cv.waitKey(0)

cv.imshow("show",img_process)
cv.waitKey(0)

cv.destroyAllWindows()