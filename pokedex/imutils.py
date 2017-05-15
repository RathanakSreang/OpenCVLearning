import cv2

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # get image dimotion
    (h,w) = image.shape[:2]
    dim = None

    if width == None and height == None:
        return image

    if width == None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h *r))

    resize = cv2.resize(image, dim, interpolation = inter)
    return resize
