import cv2 as cv
import numpy as np

num_in_roll = 101;  # 一行有的小方块数量
# 仿射变换
S_size = 505  # 变换后的二维码大小
S_out_Size = 600  # 二维码输出大小


def affine_transformation(points):
    ptr1 = points
    ptr2 = np.float32([[0, 0], [S_size, 0], [S_size, S_size], [0, S_size]])
    M = cv.getPerspectiveTransform(ptr1, ptr2)
    res = cv.warpPerspective(input_img, M, (S_out_Size, S_out_Size))
    return res


def pixel2binary(res):  # 读取图片信息
    stance = S_size / num_in_roll  # 每一个小方块的边长#取指尽量将变长转换成整数
    # cv.imshow("res",res)
    center = (int)(stance / 2)  # 每个小像素是5x5取中点值读取rgb值
    #pixel = [[0 for x in range(num_in_roll)] for y in range(num_in_roll)]
    pixel = []
    # pixel=np.arange(41*41).reshape((41,41))
    # for i in range(num_in_roll):  # 行读取
    #     i_x = center + i * stance
    #     for j in range(num_in_roll):
    #
    #         j_y = center + j * stance
    #         rgb = res[(int)(i_x), (int)(j_y)]
    #         print(rgb)
    #
    #         if rgb[2] > 150:  # 白色
    #             pixel[i][j] = 0
    #         else:
    #             pixel[i][j] = 1
    for x in range(num_in_roll):
        i_x = center + x * stance
        for y in range(num_in_roll):
            j_y = center + y * stance
            rgb = res[(int)(i_x), (int)(j_y)]
            if x < 8 and y < 8:
                continue
            elif x > 92 and y < 8:
                continue
            elif x < 8 and y > 92:
                continue
            elif x > 92 and y > 92:
                continue
            else:

                # print(rgb)
                for m in range(3):
                    #print(res[m].si)
                    if (rgb[m] <255/2):
                        pixel.append(0)
                    else:
                        pixel.append(1)
    return pixel


def Write(pixel):
    file = open("001.txt", "w", encoding='utf-8')
    for i in pixel:
        file.write(str(i))
        # file.write('\n')
    file.close()

def solve(pixel):
    n = len(pixel)
    p = 25
    ou = open("out.txt", "w", encoding="utf-8")
    bu = open("vout.txt", "w", encoding="utf-8")
    right, s = "", ""
    for i in range(0, n-3, 12):
         two = 2048
         sum = 0
         for j in range(12):
             sum = sum + two * pixel[i+j]
             print(i, j, i + j, pixel[i+j])
             two = two // 2
         if (sum % p == 0):
             right = right + '1'
         else:
             right = right + '0'
         sum = sum // 16
         s += chr(sum)
    bu.write(right)
    ou.write(s)
    bu.close()
    ou.close()




if __name__ == "__main__":
    filename = "img/1(5).png"
    input_img = cv.imread(filename)
    gray_img = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)  # 将图片通过库转换成灰度图像
    ret, binary_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)  # 将图片转换成黑白二值化
    # cv.imshow("show2", gray_img)
    contours, hierarchy = cv.findContours(binary_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.imshow("as",binary_img)

    ## 函数变换
    points = []
    qrcoder = cv.QRCodeDetector()
    ret, points = qrcoder.detect(binary_img)
    # print(points)
    # cv.imshow("show",input_img)
    # 仿射变换
    res = affine_transformation(points)
    # print(res)
    # 转换成二进制文件
    # cv.imshow("asd", res)
    pixel = []
    pixel = pixel2binary(res);  # 图片转二进制
    # print(pixel)
    Write(pixel);
    # np.savetxt("001.txt",pixel)
    solve(pixel)

    cv.waitKey(0)
    cv.destroyAllWindows()
