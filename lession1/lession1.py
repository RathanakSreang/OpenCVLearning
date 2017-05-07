# read and show image 1
import numpy as np
import cv2

img = cv2.imread('boy.jpg', 0)
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
print('(height,width)',img.shape)

# resize to 100 height
r = 500.0 / img.shape[1]
# resize to 100 width
dim = (500, int(img.shape[0] * r))
print('dim', dim)
# perform resize image
resize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# rotating image
(h, w) = resize.shape[:2]
center = (w/2, h/2)
# rotate the image by 180 degree
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(resize, M, (w,h))

# crop the image
#[startY:ENDY,StatX:EndX]
croped = img[500:1200, 1500:2200]
cv2.imshow('image',img)
cv2.imshow('crop', croped)
cv2.imshow('rotated', rotated)
cv2.imshow('resize', resize)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
#if k == 27:         # wait for ESC key to exit
#  print "Close window"
#  cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#  print "Saving image"
#  cv2.imwrite('messigray.png',img)
#  print "File saved"
#  cv2.destroyAllWindows()

