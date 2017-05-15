import cv2
import numpy as np

#img = np.zeros([height, width, 3], dtype=np.uint8)
img = np.zeros([300,300, 3], dtype="uint8")

# line((startY,StartX), (EndY,EndX),(B,G,R), size)
cv2.line(img, (0,0), (300, 300), (0,255,0))
cv2.line(img, (0,300), (300, 0), (0,255,0), 3)

cv2.rectangle(img, (10,10),(60,60), (255,0,0))
cv2.rectangle(img, (150,10),(260,105), (255,0,0), 3)
cv2.rectangle(img, (3,250),(50,297), (255,0,0), 3, 1)
cv2.imshow("The color", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
