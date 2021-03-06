from rgbhistogram import RGBhistogram
from searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2

#contruct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
        help = "Path    to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required = True,
        help = "Path to where we stored our indexx")
ap.add_argument("-q", "--query", required = True,
        help = "Path to     query image")
args = vars(ap.parse_args())

# load the query image and show it
queryImage = cv2.imread(args["query"])
cv2.imshow("Query", queryImage)
print "query: %s" % (args["query"])

# describe the query in the same way that we did in
# index.py -- a 3D RGB histogram with 8 bins per
# channel
desc = RGBHistogram([8, 8, 8])
queryFeatures = desc.describe(queryImage)

# load the index perform the search
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)
results = searcher.search(queryFeatures)

# initialize the two montages to display our results --
# we have a total of 25 images in the index, but let's only
# display the top 10 results; 5 images per montage, with
# images that are 400x166 pixels
montageA = np.zeros((166 * 5, 400, 3), dtype = "uint8")
montageB = np.zeros((166 * 5, 400, 3), dtype = "uint8")

# loop over the top ten results
for j in xrange(0, 10):
    # grab the result (we are using row-major order) and
    # load the results image
    (score, imageName) = results[j]
    path = args["dataset"] + "/%s" % (imageName)
    result = cv2.imread(path)
    print "\t%d. %s : %.3f" % (j + 1, imageName, score)

    # check to see if the first montage should bute used
    if j < 5:
        montageA[j * 166:(j + 1) * 166, :] = result
        # otherwise, the second montage should be used
    else:
        montageB[(j - 5) * 166:((j - 5) + 1) * 166, :] = result

# show the results
cv2.imshow("Results 1-5", montageA)
cv2.imshow("Results 6-10", montageB)
cv2.waitKey(0)
