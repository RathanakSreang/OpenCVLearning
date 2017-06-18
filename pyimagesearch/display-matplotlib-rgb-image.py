import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#image = mpimg.imread("images/cat.png")
image = cv2.imread("images/cat.png")
plt.axis('off')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
