import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,back=cap.read()# ret is True when we are able to capture from webcam and false else
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5)==ord('q'):
            cv2.imwrite('image.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()
