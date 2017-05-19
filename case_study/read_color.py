import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image part")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(B,G,R) = cv2.split(image)
print B[0]
