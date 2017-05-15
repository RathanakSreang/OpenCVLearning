import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(h,w) = image.shape[:2]
mask = np.zeros((h,w), dtype="uint8")
mask1 = np.zeros((h,w), dtype="uint8")
m_w = int(w * 0.4)
m_h = int(h *0.3)
mask[100:m_h,100:m_w] = 255
cv2.circle(mask1, (w/2,h/2), 200, 255, -1)

image_mask = cv2.bitwise_and(image, image, mask = mask)
image_mask1 = cv2.bitwise_and(image, image, mask = mask1)

cv2.imshow("Orignal", image)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Image", image_mask)
cv2.imshow("Mask Image 1", image_mask1)
cv2.waitKey(0)
cv2.destroyAllWindows()

