import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('linear_gradient.png', 0) # 0 for read image as gray scal
ret, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, threshold2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, threshold3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, threshold4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, threshold5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BRNARY_INV', 'TRUNC', 'TOZERO', 'TPZERO_INV']
images = [img, threshold1, threshold2, threshold3, threshold4, threshold5]

for i in xrange(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
