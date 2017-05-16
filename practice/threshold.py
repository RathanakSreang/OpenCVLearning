import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The Image path")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=400)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

# threshold(image_SRC, MAX_COLOR_desityly_value, color_set_to_if_value_greater_then_max,mode)
(T, thresh) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold binary", thresh)
(T, threshInv) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold binary inv", threshInv)

thresh = cv2.adaptiveThreshold(blurred, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Adptive thresh MEAN", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 15,3)
cv2.imshow("Adptive thresh Gaussian", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
