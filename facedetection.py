import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
i=cv2.imread("img.jpg",1)
img=cv2.resize(i,(500,500))

#searching coordinates on img
faces=face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)

for i,j,w,h in faces:
	img=cv2.rectangle(img,(i,j),(i+w,j+h),(0,255,0),2)

cv2.imshow("illi",img)
cv2.waitKey(20000)
cv2.destroyAllWindows()
