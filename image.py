import cv2
img = cv2.imread("F:\\py\\2.jpg",1)
#print(img)
fcascade=cv2.CascadeClassifier()
resize=cv2.resize(img,(200,200))
cv2.imshow("1",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
