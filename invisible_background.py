import cv2
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread("./image.jpg")
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        red=np.uint8([[[0,0,255]]])
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        # threshold red value
        #lower hue:10,100,100 upper: h+10,255,255

        l_red=np.array([0,0,255])
        u_red=np.array([5,250,255])
        mask=cv2.inRange(hsv,l_red,u_red)
        # cv2.imshow('hsv',mask)
        part1=cv2.bitwise_and(back,back,mask=mask)
        mask=cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("part2",part2)
        cv2.imshow("clock",part1+part2)

        if cv2.waitKey(5)==ord('q'):

            break
cap.release()
cv2.destroyAllWindows()
