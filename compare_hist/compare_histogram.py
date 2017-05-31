from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help = "Dataset path")
args = vars(ap.parse_args())

index = {}
images = {}

for imagePath in glob.glob(args["dataset"] + "/*.png"):
    fileName = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    images[fileName] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0, 256,0,256,0,256])
    hist = cv2.normalize(hist, hist).flatten()
    index[fileName] = hist

# # Method 1: UTILIZE Opencv
# # init array of opencv methods
# OPENCV_METHODS = (
#         ("Correlation", cv2.HISTCMP_CORREL),
#         ("Chi-squared", cv2.HISTCMP_CHISQR),
#         ("Intersection", cv2.HISTCMP_INTERSECT),
#         ("Bhatta", cv2.HISTCMP_BHATTACHARYYA),
#         ("Hellinger", cv2.HISTCMP_HELLINGER)
#         )
# # loop over methos
# for (methodName, method) in OPENCV_METHODS:
#     results = {}
#     reverse = False
#     if methodName in ("Correlation", "Intersection"):
#         reverse = True
#     for (k, hist) in index.items():
#         d = cv2.compareHist(index["dog.png"], hist, method)
#         results[k] = d

#     results = sorted([(v,k) for (k,v) in results.items()], reverse = reverse)

#     print(methodName)
#     print(results)
#     # show the query image
#     fig = plt.figure("Query")
#     ax = fig.add_subplot(1,1,1)
#     ax.imshow(images["dog.png"])
#     plt.axis("off")

#     fig = plt.figure("Result: %s" % methodName)
#     fig.suptitle(methodName, fontsize= 20)

#     #loop over the result
#     for (i, (v, k)) in enumerate(results):
#         # show the result
#         ax = fig.add_subplot(1, len(images), i + 1)
#         #ax.set_title("%s: %.2f" %(k,v))
#         plt.imshow(images[k])
#         plt.axis("off")

# plt.show()

# # print(index.items())
# print(images.items())
# # method 2: scipy distance
# SCIPY_METHODS = (
#         ("Eucliden", dist.euclidean),
#         ("Manhattan", dist.cityblock),
#         ("Chebysev", dist.chebyshev)
#         )
# for (methodName, method) in SCIPY_METHODS:
#     results = {}

#     print(index.items())
#     for (k, hist) in index.items():
#         d = method(index["dog.png"], hist)
#         results[k] = d

#     results = sorted([(v, k) for (k, v) in results.items()])

#     # show the query image
#     fig = plt.figure("Query")
#     ax = fig.add_subplot(1, 1, 1)
#     ax.imshow(images["dog.png"])
#     plt.axis("off")

#     # initialize the results figure
#     fig = plt.figure("Results: %s" % (methodName))
#     fig.suptitle(methodName, fontsize = 20)

#     # loop over the results
#     for (i, (v, k)) in enumerate(results):
#         # show the result
#         ax = fig.add_subplot(1, len(images), i + 1)
#         ax.set_title("%s: %.2f" % (k, v))
#         plt.imshow(images[k])
#         plt.axis("off")

# # show the SciPy methods
# plt.show()


# METHOD #3: ROLL YOUR OWN
def chi2_distance(histA, histB, eps = 1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])

    # return the chi-squared distance
    return d

# initialize the results dictionary
results = {}

# loop over the index
for (k, hist) in index.items():
    # compute the distance between the two histograms
    # using the custom chi-squared method, then update
    # the results dictionary
    d = chi2_distance(index["dog.png"], hist)
    results[k] = d

# sort the results
results = sorted([(v, k) for (k, v) in results.items()])

# show the query image
fig = plt.figure("Query")
ax = fig.add_subplot(1, 1, 1)
ax.imshow(images["dog.png"])
plt.axis("off")

# initialize the results figure
fig = plt.figure("Results: Custom Chi-Squared")
fig.suptitle("Custom Chi-Squared", fontsize = 20)

# loop over the results
for (i, (v, k)) in enumerate(results):
    # show the result
    ax = fig.add_subplot(1, len(images), i + 1)
    ax.set_title("%s: %.2f" % (k, v))
    plt.imshow(images[k])
    plt.axis("off")

# show the custom method
plt.show()
