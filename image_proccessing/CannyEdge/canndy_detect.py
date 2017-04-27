import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('testing.jpg', 0)
edges = cv2.Canny(img, 0, 255, False)
edges2 = cv2.Canny(img, 0, 255, True)

#plt.subplot(121), plt.imshow(img, cmap = 'gray')
#plt.title('Orignal Image'), plt.xticks([]), plt.yticks([])
plt.subplot(121), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image Default'), plt.xticks([]), plt.yticks([])
plt.subplot(120), plt.imshow(edges2, cmap = 'gray')
plt.title('Edge Image Edge Gradient'), plt.xticks([]), plt.yticks([])


plt.show()
