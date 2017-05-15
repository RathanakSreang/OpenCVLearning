import argparse
import imutils
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=400)
(B,G,R) = cv2.split(image)

cv2.imshow("Orignal", image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.imshow("Marges", cv2.merge((B,G,R)))
cv2.imshow("Marges 2", cv2.merge((R,G,B)))
#cv2.imshow("Marges 3", cv2.merge((G,G,B)))
#cv2.imshow("Marges 4", cv2.merge((R,R,B)))
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("images/lala.jpg", cv2.merge([R,G,B]))
#cv2.imwrite("images/lala2.jpg", cv2.merge([B,G,R]))

