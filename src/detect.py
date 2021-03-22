import cv2 as cv
import numpy as np

filename="img/9.png"
input_img=cv.imread(filename)

gray_img=cv.cvtColor(input_img,cv.COLOR_BGR2GRAY)#将图片通过库转换成灰度图像

ret,binary_img=cv.threshold(gray_img,127,255,cv.THRESH_BINARY)#将图片转换成黑白二值化
#cv.imshow("binary_img",binary_img)

#thresholdImage=cv.Canny(binary_img,100,200)#通过hierarchy层级关系判断定位点
contours,hierarchy=cv.findContours(binary_img,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

#print(hierarchy)
points= []#存的是二维码的四个顶点
qrcoder = cv.QRCodeDetector()
ret,points=qrcoder.detect(binary_img)

print(points)
#cv.drawContours(input_img, [np.int32(points)], -1, (0, 0, 255), 2)#将二维码圈出


#print("GRAY:", gray_img[500, 500])#输出某点的灰度值 0是黑色，255是白色

#cv.circle(input_img,(500,500),1,(0, 0, 255),1)#在原图中圈出定位点

#仿射变换
ptr1=points
ptr2=np.float32([[0,0],[205,0],[205,205],[0,205]])
print(ptr1)
print(ptr2)
M=cv.getPerspectiveTransform(ptr1,ptr2)
res=cv.warpPerspective(input_img,M,(300,300))

stance=5
center_x=2#每个小像素是5x5取中点值读取rgb值
center_y=2

#a=res[100, 100]
#print(a)

pixel=np.arange(41*41).reshape((41,41))
for i in range(41):#行读取
    i_x=center_x+i*5
    for j in range(41):
        j_y=center_y+j*5
        rgb=res[i_x,j_y]
        if rgb[2]>150:#白色
            pixel[i][j]=0
        else:
            pixel[i][j]=1



print(pixel)
#cv.imshow("input_img",res)
#cv.imwrite("img/a.jpg",res)

cv.waitKey(0)
cv.destroyAllWindows()