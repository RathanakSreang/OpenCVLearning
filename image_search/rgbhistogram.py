import cv2
import numpy as np

class RGBHistogram:
    def __init__(self, bins):
        #store the number of bids where histograme will use
        self.bins = bins

    def describe(self, image):
        # compute a 3d histogram in the RGB colorspace.
        # then normalize the histogram so that image with the same content
        # ,but either scale largeror smaller will have (roughly) the same histogram
        hist = cv2.calcHist([image],[0,1,2], None, self.bins, [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist)

        # return a 3d histogram as a flattened array
        return hist.flatten()
