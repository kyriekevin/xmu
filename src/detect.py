import cv2 as cv
import numpy as np


# 仿射变换
def affine_transformation(points):
    ptr1 = points
    ptr2 = np.float32([[0, 0], [205, 0], [205, 205], [0, 205]])
    M = cv.getPerspectiveTransform(ptr1, ptr2)
    res = cv.warpPerspective(input_img, M, (300, 300))
    return res


def pixel2binary():
    stance = 5
    center_x = 2  # 每个小像素是5x5取中点值读取rgb值
    center_y = 2
    pixel = [[0 for x in range(41)] for y in range(41)]

    # pixel=np.arange(41*41).reshape((41,41))
    for i in range(41):  # 行读取
        i_x = center_x + i * 5
        for j in range(41):
            j_y = center_y + j * 5
            rgb = res[i_x, j_y]
            if rgb[2] > 150:  # 白色
                pixel[i][j] = 0
            else:
                pixel[i][j] = 1
    return pixel


def Write(pixel):
    file = open("001.txt", "w")
    for i in range(41):
        for j in range(41):
            file.write(str(pixel[i][j]) + ' ')
        file.write('\n')
    file.close()


if __name__ == "__main__":
    filename = "img/9.png"
    input_img = cv.imread(filename)
    gray_img = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)  # 将图片通过库转换成灰度图像
    ret, binary_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)  # 将图片转换成黑白二值化
    contours, hierarchy = cv.findContours(binary_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # 函数变换
    points = []
    qrcoder = cv.QRCodeDetector()
    ret, points = qrcoder.detect(binary_img)
    # 仿射变换
    res = affine_transformation(points)
    # 转换成二进制文件
    pixel = []
    pixel = pixel2binary();
    Write(pixel);
    # np.savetxt("001.txt",pixel)

    cv.waitKey(0)
    cv.destroyAllWindows()
