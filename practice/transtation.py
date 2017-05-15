import argparse
import cv2
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
## shift down and right
#M = np.float32([[1,0,350], [0,1,50]])
##shift up and left
#M1 = np.float32([[1,0,-350], [0,1,-50]])
#shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
##shifted1 = cv2.warpAffine(image, M1, (image.shape[1]/2, image.shape[0]/2))
#shifted1 = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
shifted = imutils.translate(image,11111111111100, 350)
shifted1 = imutils.translate(image, 0, -350)
cv2.imshow("Original", image)
cv2.imshow("Shifted image", shifted)
cv2.imshow("Shifted image 1", shifted1)
cv2.waitKey(0)
cv2.destroyAllWindows()
