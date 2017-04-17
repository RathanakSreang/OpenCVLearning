import cv2
import numpy as np

#img1 = cv2.imread('ml.png')
#img2 = cv2.imread('opencv.jpg')

#dst = cv2.addWeighted(img1, 0.7, img2, 0.3,0)
#cv2.imshow('dst', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv-logo.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
