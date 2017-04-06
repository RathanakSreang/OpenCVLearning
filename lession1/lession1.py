# read and show image 1
import numpy as np
import cv2

img = cv2.imread('boy.jpg', 0)
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
  print "Close window"
  cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
  print "Saving image"
  cv2.imwrite('messigray.png',img)
  print "File saved"
  cv2.destroyAllWindows()

# # read and show image 2
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('boy.jpg', 0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # hide x,y
# plt.show()
