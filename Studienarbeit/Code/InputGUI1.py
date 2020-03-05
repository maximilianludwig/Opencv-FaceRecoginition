import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("InputGUI1")
img_counter = 1
while True:
    ret, img = cam.read()
    cv2.imshow("InputGUI1", img)
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