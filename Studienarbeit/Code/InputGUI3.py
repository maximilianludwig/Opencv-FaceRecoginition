import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
cam = cv2.VideoCapture(0)
cv2.namedWindow("InputGUI")
img_counter = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("InputGUI")
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 27: # ESC pressed, closing the window
        break
    elif k%256 == 32: # SPACE pressed, save grayscale face as input 
        gray = gray[y:y + h, x:x + w]  # Cut the frame to size
        try:
            cv2.imwrite("InputGUI{}.png".format(img_counter), cv2.resize(gray, (350, 350)))
            img_counter += 1
        except:
            pass

cam.release()
cv2.destroyAllWindows()
