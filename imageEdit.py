import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/Admin/Downloads/chemtech.jpg', 1)

alpha = 1 # float(input("Alpha:"))
beta = 0 # int(input("Beta:"))

gamma = 0.4
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

# img = cv.LUT(img, lookUpTable)
img = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

#img = cv.rotate(img, cv.cv2.ROTATE_90_CLOCKWISE)
cv.namedWindow('hehe')

def controller(img, brightness=255, contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
 
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
 
    if brightness != 0:
 
        if brightness > 0:
 
            shadow = brightness
 
            max = 255
 
        else:
 
            shadow = 0
            max = 255 + brightness
 
        al_pha = (max - shadow) / 255
        ga_mma = shadow
 
        # The function addWeighted
        # calculates the weighted sum
        # of two arrays
        cal = cv.addWeighted(img, al_pha,
                              img, 0, ga_mma)
 
    else:
        cal = img
 
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv.addWeighted(cal, Alpha,
                              cal, 0, Gamma)
 
    # putText renders the specified
    # text string in the image.
    cv.putText(cal, 'B:{},C:{}'.format(brightness,
                                        contrast),
                (10, 30), cv.cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)
 
    return cal

def BrightnessContrast(brightness=0):
    brightness = cv.getTrackbarPos('Brightness','hehe')
    contrast = cv.getTrackbarPos('Contrast','hehe')
    effect = controller(img,brightness,contrast)
    cv.imshow('hehe',effect)

cv.createTrackbar('Brightness','hehe',255,2*255,BrightnessContrast)
cv.createTrackbar('Contrast','hehe',127,2*127,BrightnessContrast)
BrightnessContrast(0)

cv.waitKey(0)
cv.destroyAllWindows()