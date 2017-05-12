import cv2

def resize(image, height):
    r = image.shape[0] / height
    dim = (height, int(image.shape[0] * r))
    resize = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resize
