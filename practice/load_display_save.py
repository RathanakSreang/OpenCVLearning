import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The Image path")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Show the image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
