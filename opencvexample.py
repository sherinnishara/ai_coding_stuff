import cv2
img = cv2.imread(r'C:\Users\NEWUSER\Downloads\tony-hand-C9Ni6Gh_gWk-unsplash.jpg')
cv2.imshow('image',img)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray img', gray_img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
