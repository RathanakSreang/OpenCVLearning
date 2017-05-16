import cv2
import argparse
import imutils
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="The Image path")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=400)

chans = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
print colors
print chans
for (chan, color) in zip(chans, colors):
    print color, chan
    hist = cv2.calcHist([chan], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
print "3D histogram shape: %s, with %d values" %(hist.shape, hist.flatten().shape[0])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
