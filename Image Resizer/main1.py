import cv2
source="./cat.png"
destination="./cat.png"
scale_percent=50

image=cv2.imread("cat.png",cv2.IMREAD_UNCHANGED)

width=int(image.shape[1]*scale_percent/100)
height=int(image.shape[0]*scale_percent/100)

dsize=(width,height)

output=cv2.resize(image,dsize)

cv2.imwrite(destination,output)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()