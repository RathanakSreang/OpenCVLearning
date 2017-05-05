import cv2
import numpy as np

# Read images
tree = cv2.imread('images/Big_Tree_with_Red_Sky_in_the_Winter_Night.jpg')
plane = cv2.imread('images/Japan.airlines.b777-300.ja733j.arp.jpg')

#creae a rough mask around airplane
mask = np.zeros(plane.shape, plane.dtype)
poly = np.array([ [4, 80], [30, 54], [151, 63], [254,37], [298, 90], [272, 134],[43,122]], np.int32)
cv2.fillPoly(mask, [poly], (255,255,255))

x = 653
i = 1
print(plane.shape)
print(tree.shape)
while(True):
    # This is where the center of the airplane will be placed
    center = (x, 50)
    print(x)
    x += i * 10
    if x >= 653:#tree.shape[1] - plane.shape[1]:
        i = -1
        x = 653
    elif x <= 150:
        i = 1
        x = 150

    # clone seamlessly
    result = cv2.seamlessClone( plane, tree, mask, center, cv2.NORMAL_CLONE)

    #cv2.imshow('mash', mask)
    cv2.imshow('plane', plane)
    cv2.imshow('seamless clone', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
