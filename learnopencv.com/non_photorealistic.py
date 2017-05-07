import cv2
import numpy as np

img = cv2.imread('images/my_image.jpg', 1)
# sigma_s = size of effect(0-200)
# sigma_r = range of effect(0-1)
dst = cv2.edgePreservingFilter(img, flags=1, sigma_s=100, sigma_r=0.3)
dst2 = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.25)
# shade_factor = output image intensity(0.0-0.1)
dst3, dst4 = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.05, shade_factor=0.05)
dst5 = cv2.stylization(img, sigma_s=20, sigma_r=0.05)
cv2.imshow('The image', img)
cv2.imshow('Filter1', dst)
cv2.imshow('Filter2', dst2)
cv2.imshow('Filter3', dst3)
cv2.imshow('Filter4', dst4)
cv2.imshow('Filter5', dst5)
cv2.waitKey(0)
cv2.destroyAllWindows()
