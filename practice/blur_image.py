import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The Image path")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=400)

blurred = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (5,5)),
    cv2.blur(image, (7,7)),
    cv2.blur(image,(101,101))
    ])

cv2.imshow("Average", blurred)

blurred = np.hstack([
    cv2.GaussianBlur(image, (3,3), 0),
    cv2.GaussianBlur(image, (5,5), 0),
    cv2.GaussianBlur(image, (7,7), 0),
    cv2.GaussianBlur(image, (101,101),0)
    ])
cv2.imshow("Gaussian", blurred)

blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7),
    cv2.medianBlur(image, 101)
    ])
cv2.imshow("Median Blur", blurred)

blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41,41),
    cv2.bilateralFilter(image, 101, 121,121)
    ])
cv2.imshow("bilateralFilter", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
