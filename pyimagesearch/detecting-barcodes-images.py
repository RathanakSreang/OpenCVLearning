import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image Path")
args = vars(ap.parse_args())

# load the image and convert to gray color
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute the Scharr gradient magnitude representation of the images
# in the x and y direction
gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx=0, dy=1, ksize=-1)

# substract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

# blur and threshold the image
blurred = cv2.blur(gradient, (9,9))
(_, thresh) = cv2.threshold(blurred, 255, 255, cv2.THRESH_BINARY)

# construct a closing kernel and appy it to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21,7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# performing a serial of erosions and dialations
closed = cv2.erode(closed,None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)

#find contours in the threshold image, then sort the contours
# by their area, keeping only the largest one
#(_,cnts,_) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
#        cv2.CHAIN_APPROX_SIMPLE)
#print(cnts)
#c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contours
#rect = cv2.minAreaRect(c)
#box = np.int0(cv2.cv.BoxPoints(rect))

# draw the bounding box arounded the detected barcode nd display the image
#cv2.drawContours(image, [box], -1, (0,0255,0), 3)
cv2.imshow("image", image)
cv2.imshow("Mask", closed)
cv2.waitKey(0)
cv2.destroyAllWindows()

