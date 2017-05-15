import argparse
import cv2
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)
cv2.waitKey(0)
cv2.destroyAllWindows()

