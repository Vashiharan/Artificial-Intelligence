# Blur image

import cv2
img = cv2.imread('img.jpg')

gaussianImg= cv2.GaussianBlur(img,(41,41),50)
gaussianImg1= cv2.GaussianBlur(img,(21,21),50)

cv2.imshow('Original Image',img)
cv2.imshow('Gaussian Blur',gaussianImg)
cv2.imshow('Gaussian Blur 1',gaussianImg1)

cv2.imwrite('Blur.jpg',gaussianImg)

cv2.waitKey(6000)
cv2.destroyAllWindows()
