import cv2
import numpy as np

#img = np.zeros([height, width, 3], dtype=np.uint8)
img = np.zeros([300,300, 3], dtype="uint8")
#image[startY:EndY, StatX:EndX] = (B,G,R) color code
img[:50,:50] = [0,0,0]
img[50:100,0:50] = [255,255,255]
img[100:150,0:50] = [255,0,0]
img[150:200,0:50] = [0,255,0]
img[200:250,0:50] = [0,0,255]
img[250:300,0:50] = [0,255,255]

img[:50,50:100] = [0,255,255]
img[50:100,50:100] = [0,0,255]
img[100:150,50:100] = [0,255,0]
img[150:200,50:100] = [255,0,0]
img[200:250,50:100] = [255,255,0]
img[250:300,50:100] = [255,255,255]

cv2.imshow("The color", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
