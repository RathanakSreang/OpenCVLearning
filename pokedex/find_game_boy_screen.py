import imutils
from skimage import exposure
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True, help="Path to the query image")
args = vars(ap.parse_args())

image = cv2.imread(args["query"])
orig = image.copy()
ratio = image.shape[0] / 300.0
image = imutils.resize(image, height = 300)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

print screenCnt
pst = screenCnt.reshape(4,2)
print "pst:", pst
print "pst:", pst.reshape(2,4)
rect = np.zeros((4,2), dtype="float32")

s = pst.sum(axis =1)
rect[0] = pst[np.argmin(s)]
rect[2] = pst[np.argmax(s)]

diff = np.diff(pst, axis =1)
rect[1] = pst[np.argmin(diff)]
rect[3] = pst[np.argmax(diff)]

rect *= ratio
(tl, tr, br, bl) = rect
# distance calculation, d = sqr((x2 - x2)^2 + (y2-y1)^2)
widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

maxWidth = max(int(widthA), int(widthB))
maxHeight = max(int(heightA), int(heightB))
print maxWidth
print maxHeight
dst = np.array([
        [0,0],
        [maxWidth -1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight -1]], dtype= "float32")

M = cv2.getPerspectiveTransform(rect,dst)
warp = cv2.warpPerspective(orig, M, (maxWidth,maxHeight))

warp = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
warp = exposure.rescale_intensity(warp, out_range =(0, 255))

(h,w) = warp.shape
(dX, dY) = (int(w * 0.4), int(h * 0.45))
crop = warp[10:dY, w - dX:w - 10]

# save the cropped image to file
cv2.imwrite("cropped.png", crop)

# show our images
cv2.drawContours(image, [screenCnt], -1, (0, 255,0), 3)
cv2.imshow("image", image)
cv2.imshow("edge", edged)
cv2.imshow("warp", imutils.resize(warp, height = 300))
cv2.imshow("crop", imutils.resize(crop, height = 300))
cv2.waitKey(0)
cv2.destroyAllWindows()

