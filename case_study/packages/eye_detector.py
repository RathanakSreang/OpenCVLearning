import cv2

class EyeDetector:
  def __init__(self, faceCascadePath, eyeCascadePath):
    self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
    self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

  def track(self, image):
    faceRect = self.faceCascade.detectMultiScale(image, scaleFactor = 1.1,
      minNeighbors = 3, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)
    rects = []

    for (x,y,w,h) in faceRect:
      faceROI = image[y:y+h, x:x+w]
      rects.append((x,y,x+w,y+h))

      eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor=1.1,
        minNeighbors=5, minSize=(10,10), flags = cv2.CASCADE_SCALE_IMAGE)

      for (eX,eY,eW,eH) in eyeRects:
        rects.append((x + eX, y + eY, x + eX + eW, y + eY + eH))

    return rects
