from packages.facedetector import FaceDetector
from packages import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="Path to where face detector locate")
ap.add_argument("-i", "--image", required=True, help="Path to where image locate")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=500)
cv2.imshow("Original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 3, minSize = (30,30))
print "I found %d face(s)" % (len(faceRects))

for (x,y,w,h) in faceRects:
  cv2.rectangle(image, (x,y), (x +w, y +h), (0,255,0), 2)

cv2.imshow("Detected", image)
cv2.waitKey(0)
