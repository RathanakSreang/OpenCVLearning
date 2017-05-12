from zernike_moments import ZernikeMoments
import numpy as np
import argparse
import cPickle
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sprites", required=True, help="Path to where sprites image was stored")
ap.add_argument("-i", "--index", required=True, help="Path to where index file will stored")
args = vars(ap.parse_args())

desc = ZernikeMoments(21)
index = {}

#print glob.glob(args["sprites"] + "/*.png")

for spritePath in glob.glob(args["sprites"] + "/*.png"):
    pokemon = spritePath[spritePath.rfind("/") + 1:].replace(".png", "")
    image = cv2.imread(spritePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # add image padding 15px
    image = cv2.copyMakeBorder(image, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value = 255)
    thresh = cv2.bitwise_not(image)
    thresh[thresh > 0] = 255

    outline = np.zeros(image.shape, dtype = "uint8")
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    cv2.drawContours(outline, [cnts], -1, 255, -1)

    moments = desc.describe(outline)
    index[pokemon] = moments
    #print moments.shape, moments

    #cv2.imshow("image", image)
    #cv2.imshow("thresh", thresh)
    #cv2.imshow("outline", outline)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()
