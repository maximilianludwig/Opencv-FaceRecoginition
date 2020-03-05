import cv2

face_cascade = cv2.CascadeClassifier('/home/kevin/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
cv2.namedWindow("InputGUI")
img_counter = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("InputGUI", img)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 27: # ESC pressed, closing the window
        break
    elif k%256 == 32: # SPACE pressed, save image as input 
        cv2.imwrite("InputGUI{}.png".format(img_counter), img)
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
