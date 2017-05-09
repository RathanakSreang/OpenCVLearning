from packages.searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2

# constructure and parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="Path to directory where contain images we just index")
ap.add_argument("-i", "--index", required=True, help="Path to where we store index")

args = vars(ap.parse_args())

#load index and init search
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)
#loop over images in the index -- we will use each one as a query image
print(dir(index))
for (query, queryFeatures) in index.items():
    #get the search result
    results = searcher.search(queryFeatures)

    #load the query image and display
    path = args["dataset"] + "/%s" % (query)
    queryImage = cv2.imread(path)
    cv2.imshow("Query", queryImage)
    print("query is: %s", query)

    #initialize the two montages to display the result we have 25 total images but
    # display only top 10 result  and 5 images per montages
    montageA = np.zeros((166 * 5, 400, 3), dtype = "uint8")
    montageB = np.zeros((166 * 5, 400, 3), dtype = "uint8")

    #loop over top result
    for j in xrange(0, 10):
        # grabe the result and load the result images
        (score, imageName) = results[j]
        path = args["dataset"] + "/%s" % (imageName)
        result = cv2.imread(path)
        print "\t%d. %s : %.3f" % (j + 1, imageName, score)

        #check to see if the first montage should be used
        if j < 5:
            montageA[j * 166:(j + 1) * 166, :] = result
        else:
            montageB[(j-5) * 166:((j-5)+1)*166, :] = result
    #show the result
    cv2.imshow("Result1-5", montageA)
    cv2.imshow("Result6-10", montageB)
    cv2.waitKey(0)




