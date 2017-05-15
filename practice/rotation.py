import numpy as np
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image Path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

#(h,w) = image.shape[:2]
#center = (w/2,h/2)

#M = cv2.getRotationMatrix2D(center, 45, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
rotated = imutils.rotate(image, 90, scale=0.3)
cv2.imshow("Rotated by 45 degree", rotated)

#M = cv2.getRotationMatrix2D(center, -90, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
rotated = imutils.rotate(image, 45, scale= 0.5)
cv2.imshow("Rotated by -90 degree", rotated)

print "CV add", cv2.add(np.uint8([200]), np.uint8([100]))
print "CV sub", cv2.subtract(np.uint8([50]), np.uint8([100]))

print "NP add", str(np.uint8([200]) +  np.uint8([100]))
print "NP sub", str(np.uint8([50]) - np.uint8([100]))

cv2.waitKey(0)
cv2.destroyAllWindows()

