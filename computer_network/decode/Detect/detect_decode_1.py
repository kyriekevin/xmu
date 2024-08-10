import cv2 as cv
import numpy as np
import os
import struct
# from gensim.models import KeyedVectors
num_in_roll = 101  # 一行有的小方块数量
# 仿射变换
S_size = 505  # 变换后的二维码大小
S_out_Size = 600  # 二维码输出大小

class detect_decode_1:
    def affine_transformation(self,points,input_img):
        ptr1 = np.float32(points)
        ptr2 = np.float32(
            [[2 + 3 * 5, 2 + 3 * 5], [2 + 97 * 5, 2 + 3 * 5], [2 + 95 * 5, 2 + 95 * 5], [2 + 3 * 5, 2 + 97 * 5]])
        M = cv.getPerspectiveTransform(ptr1, ptr2)
        res = cv.warpPerspective(input_img, M, (S_out_Size, S_out_Size))
        return res
    def pixel2binary(self,res):  # 读取图片信息
        stance = S_size / num_in_roll  # 每一个小方块的边长#取指尽量将变长转换成整数
        center = (int)(stance / 2)  # 每个小像素是5x5取中点值读取rgb值
        pixel = []
        version = ""
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
                    if (rgb[2] > 150):
                        version += "0"
                    else:
                        version += "1"
                else:

                    # print(rgb)
                    for m in range(3):
                        # print(res[m].si)
                        if (rgb[m] < 255 / 2):
                            pixel.append(0)
                        else:
                            pixel.append(1)
        ver1, ver2, ver3 = "", "", ""
        for i in range(5, 8):
            for j in range(3):
                ver1 += version[8 * i + j]
        for i in range(5, 8):
            for j in range(5, 8):
                ver3 += version[8 * i + j]
        for i in range(3):
            for j in range(5, 8):
                ver2 += version[8 * i + j]

        if ver1 != ver2 or ver1 != ver3:
            return -1, pixel
        sum = 0
        two = 1
        summ = int(ver1)
        while(summ!=0):
            sum = sum + (summ%10) * two
            two *= 2
            summ = summ // 10
        return sum, pixel


    def Write(self,pixel):
        file = open("detect_txt.txt", "w", encoding='utf-8')
        for i in pixel:
            file.write(str(i))
            # file.write('\n')
        file.close()

    def jointfile(self,count,ou_sum,vou_sum,code_index):

        cur_dir = os.getcwd()
        for i in range(1,count+1):
            if(i<10):
                c = 'out0' + str(i) + '.bin'
                e = 'vout0' + str(i) + '.bin'
            else:
                c = 'out' + str(i) + '.bin'
                e = 'vout' + str(i) + '.bin'
            if (os.path.exists(c)==False or os.path.exists(e)==False) :
                continue
            # ou=open(c,"rb",encoding="utf-8")
            # vout=open(e,"rb",encoding="utf-8")
            ou = open(c, "rb")
            vout = open(e, "rb")
            # data=ou.read()

            # if(data[0:5]=='ERROR'):
            #     continue
            #
            #ou.seek(9,0)
            data= ou.read()
            ou_sum.write(data)
            data=vout.read()
            vou_sum.write(data)

    def solve(self,pixel,count,out_name):
        n = len(pixel)
        p = [1, 1, 0, 0, 1]
        c='out'+out_name+".bin"
        e="vout"+out_name+".bin"

        ou = open(c, "wb+")
        bu = open(e, "wb+")
        for i in range(0, n - 12, 12):
            two = 2048
            sum = 0
            for j in range(12):
                if (i + j >= len(pixel)):
                    break
                sum = sum + two * pixel[i + j]
                two = two // 2
            for j in range(8):
                if pixel[i + j] == 1:
                    for k in range(5):
                        pixel[i + j + k] = pixel[i + j + k] ^ p[k]
            flag = True
            for j in range(12):
                if pixel[i + j] != 0:
                    bu.write(struct.pack('B', 0))
                    flag = False
                    break
            if flag:
                bu.write(struct.pack('B', 255))
            sum = sum // 16
            ou.write(struct.pack('B',sum))

        bu.close()
        ou.close()

    # 改变的内容
    def avg(self,rgb):
        sum = 0
        n = len(rgb)
        for i in range(n):
            sum += rgb[i]
        return sum / n

    def find_center(self,con1, con2):
        centers = []
        flag=True
        for i in range(4):
            M1 = cv.moments(con1[i])
            if(M1['m00']==0):
                flag=False
                break
            cx1 = (M1['m10'] / M1['m00'])
            cy1 = (M1['m01'] / M1['m00'])
            # print(cx1,cy1,end=' ')
            M2 = cv.moments(con2[i])
            cx2 = (M2['m10'] / M2['m00'])
            cy2 = (M2['m01'] / M2['m00'])

            centers.append([((cx1 + cx2) / 2), ((cy1 + cy2) / 2)])
        if flag:
            temp = []
            max_idx, min_idx = 0, 0
            for i in range(4):
                sum = centers[i][0] + centers[i][1]
                if sum > centers[max_idx][0] + centers[max_idx][1]:
                    max_idx = i
                if sum < centers[min_idx][0] + centers[min_idx][1]:
                    min_idx = i

            gt_x_idx, lt_x_idx = 0, 0
            first = True
            for i in range(4):
                if i == max_idx or i == min_idx:
                    continue
                if first:
                    temp1 = i
                    first = False
                else:
                    if centers[temp1][0] > centers[i][0]:
                        gt_x_idx = temp1
                        lt_x_idx = i
                    else:
                        gt_x_idx = i
                        lt_x_idx = temp1
            temp.append(centers[min_idx])
            temp.append(centers[gt_x_idx])
            temp.append(centers[max_idx])
            temp.append(centers[lt_x_idx])
            centers = temp

        return flag,centers

    def find_points(self,input_img):
        img_temp = input_img
        # 将图片通过库转换成灰度图像
        gray_img = cv.cvtColor(img_temp, cv.COLOR_BGR2GRAY)
        # 中值滤波
        # gray_img = cv.blur(gray_img, (1, 1), 0)
        # gray_img=cv.medianBlur(gray_img,5)
        # gray_img=cv.bilateralFilter(gray_img,7,50,50)
        gray_img = cv.GaussianBlur(gray_img, (3, 3), 0, 0)
        # 将图片转换成黑白二值化
        ret, binary_img = cv.threshold(gray_img, 60, 255, cv.THRESH_BINARY)
        # cv.imwrite("gray2.jpg", binary_img)
        # cv.imwrite("gray.jpg",binary_img)
        # 获得层级关系
        contours, hierarchy = cv.findContours(binary_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        level = 0
        con1 = []
        con2 = []
        con3 = []
        for i in range(len(hierarchy[0])):
            hie = hierarchy[0][i]
            if hie[2] != -1:
                level += 1
                pass
            elif hie[2] == -1 and level != 0:
                level += 1
                if level == 3:
                    con1.append(contours[i - 0])
                    con2.append(contours[i - 1])
                    con3.append(contours[i - 2])
                    pass
                level = 0
                pass
            else:
                level = 0
                pass
            pass
        t = 2
        # cv.drawContours(input_img, con2, -1, (0, 0, 255), 10)
        if(len(con1)==4):
            flag,points = self.find_center(con1, con2)
        else:
            flag=False
            points=0
        # print(points)
        # cv.imwrite("gray_findpoints.jpg", input_img)

        return flag,points



    def __init__(self):

        img_root = os.getcwd()  # 获取当前路径
        imgPath =img_root+"\\output\\"  # 保存图片路径
        count = 0
        code_index=[]
        for i in range(10000):
            code_index.append(0)
        for filename in os.listdir(imgPath):

            count+=1
            out_name=filename[0:2]
            input_img = cv.imread(imgPath+filename)


            flag,points = self.find_points(input_img)
            if not flag:
                continue
            input_img = cv.GaussianBlur(input_img, (3, 3), 0, 0)
            input_img = cv.medianBlur(input_img, 5)

            res = self.affine_transformation(points, input_img)
            version, pixel = self.pixel2binary(res)
            if (version>9):
                continue
            if (code_index[version] == 1):
                continue
            else :
                code_index[version]=1
         # 解码
            if (version != -1):
                self.solve(pixel, count,out_name)  # 解码
        ou = open("out_sum.bin", "ab+")
        bu = open("vout_sum.bin", "ab+")
        self.jointfile(count,ou,bu,code_index)
        ou.close()
        bu.close()
        cv.waitKey(0)
        cv.destroyAllWindows()

if __name__ == "__main__":
    detect_decode_1()





