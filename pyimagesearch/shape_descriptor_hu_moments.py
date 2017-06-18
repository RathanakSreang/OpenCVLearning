import cv2

image = cv2.imread("images/diamond.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

arrShapeDes = cv2.HuMoments(cv2.moments(image)).flatten()
print(arrShapeDes)
cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
