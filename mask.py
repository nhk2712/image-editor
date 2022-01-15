import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/Admin/Downloads/chemtech.jpg', 1)

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1], # no3: black, no4: b&w, no5: sharpended, no6: lightened
                   [0, -1, 0]], np.float32)

kernel2 = np.array([[1, -2, 1],
                   [2, -4, 2],
                   [1, -2, 1]], np.float32)

kernel3 = np.ones((3,3),np.float32)/10

out = cv.filter2D(img,-1, kernel3)
blur = cv.blur(img, (19,19)) 
gaus = cv.GaussianBlur(img,(19,19),0)
median = cv.medianBlur(img,5)

cv.imshow('Output', gaus)

cv.waitKey(0)
cv.destroyAllWindows()
