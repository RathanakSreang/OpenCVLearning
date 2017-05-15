import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
img2 = img.copy()
h_w = img2.shape[1] / 2
h_h = img2.shape[0] / 2
img2[0:h_h,0:h_w] = (255,255,255)

cv2.imshow("original", img)
cv2.imshow("Updated", img2)
cv2.imshow("Croop", img[0:h_h, 0:h_w])


cv2.waitKey(0)
cv2.destroyAllWindows()
