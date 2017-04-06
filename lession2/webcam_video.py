# # show video
# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# # if not cap.isOpened():
# #   cap.open()
# while(cap.isOpened()):
#   # Capture frame by frame
#   ret, frame = cap.read()

#   # conver color frame image into gray
#   gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

#   # display frame
#   cv2.imshow('frame', gray)

#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()

# Record video
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT);
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 15.0, (int(w),int(h)))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4',fourcc, 15.0, (int(w),int(h)))

print "Start record video"
while(cap.isOpened()):
  ret, frame = cap.read()

  if ret == True:
    frame = cv2.flip(frame, 1)

    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break
print "Video recorded"
cap.release()
out.release()
cv2.destroyAllWindows()
