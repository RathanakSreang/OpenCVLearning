from packages.rgbhistogram import RGBHistogram
import argparse
import cPickle
import glob
import cv2

# constuct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required= True, help="Path to directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True, help="Path to where the compute index will be stored")
args = vars(ap.parse_args())

# initialize the index dictionary to store out our quantifed.
# images, with the 'key' of the dictionary of images
# filename and the value of our computed feature
index = {}

# initialize our image descriptor a 3D histogram with 8 bins per chennel
desc = RGBHistogram([8,8,8])

#use glob to grab the image path and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
    # extract our unique image ID (i.e: file name)
    k = imagePath[imagePath.rfind("/") + 1 :]

    #load the image describe it using our RGB histogram
    image = cv2.imread(imagePath)
    features = desc.describe(image)
    index[k] = features

#we now done the indexing and now we can write our index in to disk
f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()

#show info
print "done... index %d images" % (len(index))
