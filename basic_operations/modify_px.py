import cv2
import numpy as np
img = cv2.imread('boy.jpg')
px = img[100,100]
print px
blue = img[100,100,0]
print blue
print 'item=',img.item(10,10,2)
print img.shape
print img.size
print img.dtype
angkor = img[500:600, 600:700]
print "cut:", angkor
img[10:110,110:210] = angkor
print "red color", img[:,:,2]
print "blue clumn:", img[:,:,0]
print "green column:", img[:,:,1]
img[:,:,2] = 125 #set all color red to 0
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    print "Close window"
    cv2.destroyAllWindows()
