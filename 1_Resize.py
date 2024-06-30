# Resizing an image

import cv2
import imutils

img=cv2.imread('img.jpg')
resizedImg=imutils.resize(img,width=400)
cv2.imshow('Image',img)
cv2.imshow("Resized Image",resizedImg)
cv2.imwrite("Resized Image.jpg",resizedImg)

cv2.waitKey(4000)
cv2.destroyAllWindows()
