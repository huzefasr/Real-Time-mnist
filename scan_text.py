import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    key = cv2.waitKey(1)
    flip = cv2.flip(frame,1)
    cv2.rectangle(flip,(50,50),(200,200),(0,0,255),1)
    cv2.imshow("frame",flip)
    if key == ord('x'):
        break

cam.release()
cv2.destroyAllWindows()
