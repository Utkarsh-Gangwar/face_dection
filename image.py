import cv2
face_cascade = cv2.CascadeClassifier("F:\\py\\haarcascade_frontalface_default.xml")
img = cv2.imread("F:\\py\\4.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.9 , minNeighbors = 5)

for x,y,w,h in faces:
    img - cv2.rectangle (img, (x,y), (x+w,y+h), (255,0,0),2)

resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
cv2.imshow("Gray", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()