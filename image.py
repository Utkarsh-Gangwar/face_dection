import cv2
#you can get cascade flile on link : https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier("F:\\py\\haarcascade_frontalface_default.xml")#give path of cascade file
img = cv2.imread("F:\\py\\4.jpeg")#give path of image file
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05 , minNeighbors = 5)

for x,y,w,h in faces:
    img - cv2.rectangle (img, (x,y), (x+w,y+h), (255,0,0),2)

#resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
#cv2.imshow("Greay", resize)
cv2.imshow("4", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
