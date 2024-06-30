# converting to gray image
import cv2
image = cv2.imread("img.png")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('original',image)
cv2.imshow('Gray',grayImage)
cv2.imwrite('graynew.jpg',grayImage)

print(image.shape)
print(image.size)
