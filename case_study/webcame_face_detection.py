from packages import imutils
from packages.facedetector import FaceDetector
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="Path to face detector")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)
# height = cv2.get(cv2.CAP_PROP_FRAME_HEIGHT)
# width = cv2.get(cv2.CAP_PROP_FRAME_WIDTH)
print "Init face detector"
fd = FaceDetector(args["face"])

print "Start webcame"
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    frame = imutils.resize(frame, height=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceRects = fd.detect(gray, scaleFactor =1.1, minNeighbors =3, minSize =(30,30))
    # print "Found %d face(s)" % (len(faceRects))
    for (x,y,w,h) in faceRects:
      cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

print "Stop webcame"
cap.release()
cv2.destroyAllWindows()
