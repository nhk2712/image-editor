import cv2

img = cv2.imread('C:/Users/Admin/Downloads/chemtech.jpg', 1)

White = (255,255,255)
Black = (0,0,0)
Blue = (255,0,0)
Green = (0,255,0)
Red = (0,0,255)
Yellow = (0,255,255)
Pink = (255,0,255)
Cyan = (255,255,0)

print('Info:')
(h, w, d) = img.shape # Get image size
print("width={}, height={}, depth={}".format(w, h, d))

center = (w // 2, h // 2) 
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, M, (w, h)) # Rotate image

rotated[:,:,2] = 0 # Remove red color
cv2.line(rotated,(0,0),(100,100),Red,5) # Draw a line
cv2.circle(rotated,(200,100),20,White,-1,8) # Draw a filled circle

cv2.imshow('example', rotated) # Show image
# cv2.imwrite('chemtech_edited.jpg',rotated) # Save edited image

cv2.waitKey(0)
cv2.destroyAllWindows()