from packages import imutils
import cv2
import numpy as np
import time
# import argparse

# boundaries = [
#   ([17, 15, 100], [50, 56, 200]), #red
#   ([86, 31, 4], [220, 88, 50]), #blue
#   ([25, 146, 190], [62, 174, 250]), #yellow
#   ([103, 86, 65], [145, 133, 128]) #brown
# ]

colorLower = np.array([17, 15, 100], dtype="uint8")
colorUpper = np.array([50, 56, 200], dtype="uint8")

cap = cv2.VideoCapture(0)
print "Start webcame"
while(cap.isOpened()):
  (ret, frame) = cap.read()

  if ret == True:
    frame = imutils.resize(frame, height = 400)
    color = cv2.inRange(frame, colorLower, colorUpper)
    color = cv2.GaussianBlur(color, (5,5), 0)
    (_,ctns,_) = cv2.findContours(color.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(ctns) > 0:
      cnt = sorted(ctns, key = cv2.contourArea, reverse = True)[0]
      rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
      cv2.drawContours(frame, [rect], -1, (0,255,0),2)
    cv2.imshow("color", color)
    cv2.imshow("frame", frame)

    time.sleep(0.025)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
print "Stop webcame"
