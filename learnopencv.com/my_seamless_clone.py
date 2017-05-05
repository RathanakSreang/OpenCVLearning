import cv2
import numpy as np

#read image
bg = cv2.imread('images/Big_Tree_with_Red_Sky_in_the_Winter_Night.jpg')
car = cv2.imread('images/car.jpg')

mask = np.zeros(car.shape, car.dtype)
poly = np.array([[60,10], [60,290], [250, 290], [250, 10]])
cv2.fillPoly(mask, [poly], (255,255,255))

center = (600, 200)

result = cv2.seamlessClone(car, bg, mask, center, cv2.NORMAL_CLONE)

cv2.imshow('mask', mask)
cv2.imshow('car', car)
cv2.imshow('bg', bg)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
