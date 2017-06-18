import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="The image path")

args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# find the black shape in the image
lower = np.array([0,0,0])
upper = np.array([15,15,15])
shapeMask = cv2.inRange(image, lower, upper)

cv2.imshow("shapeMask", shapeMask)

#find contours in the mask
(_,cnts,_) = cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
print("I found %d blacks shape" % (len(cnts)))

#loop over the contours
for c in cnts:
    #draw the contours
    cv2.drawContours(image, [c], -1, (0,255,0), 2)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destoryAllWindows()
