# -*- codeing = utf-8 -*-
# @Time : 2021/3/21 12:41
# @Author : zyz
# @File : QR_code.py
# @Software : PyCharm

import cv2
import numpy as np
import random
import string


# 编码
def encode(data):
    return ' '.join([bin(ord(ch)).replace('0b', '') for ch in data])


# 解码
def decode(data):
    return ''.join([chr(i) for i in [int(b, 2) for b in data.split(' ')]])


# 随机字符生成
def ranstr(num):
    file = open("text.txt", "w")
    data = ""
    for i in range(10):
        data += ''.join(random.sample(string.ascii_letters + string.digits, num))
    file.write(data)
    file.close()


# 读取文件信息
def get_data():
    ranstr(62)
    binfile = open("text.txt", "r")
    data = binfile.read()
    data = encode(data)
    cur = ''
    last = ''
    Data = []
    cnt = 0
    for i in data:
        if i == ' ':
            while len(cur) < 8:
                cur = '0' + cur
            if cnt % 2:
                Data.append(last + cur)
                last = ''
            else:
                last = cur
            cur = ''
            cnt += 1
        else:
            cur += i
    while len(cur) < 16:
        cur += '0'
    Data.append(cur)
    binfile.close()
    return Data


# 初始化定位码
def init():
    # 前期辅助线
    # cv2.line(dst, (100, 100), (100, 510), (0, 0, 1))
    # cv2.line(dst, (100, 100), (510, 100), (0, 0, 1))
    # cv2.line(dst, (510, 100), (510, 510), (0, 0, 1))
    # cv2.line(dst, (100, 510), (510, 510), (0, 0, 1))
    #
    # cv2.line(dst, (180, 100), (180, 510), (0, 0, 1))
    # cv2.line(dst, (100, 180), (510, 180), (0, 0, 1))
    #
    # cv2.line(dst, (430, 100), (430, 510), (0, 0, 1))
    # cv2.line(dst, (100, 430), (510, 430), (0, 0, 1))
    #
    # cv2.line(dst, (230, 180), (230, 430), (0, 0, 1))
    # cv2.line(dst, (280, 180), (280, 430), (0, 0, 1))
    # cv2.line(dst, (330, 180), (330, 430), (0, 0, 1))
    # cv2.line(dst, (380, 180), (380, 430), (0, 0, 1))
    #
    # cv2.line(dst, (100, 230), (510, 230), (0, 0, 1))
    # cv2.line(dst, (100, 280), (510, 280), (0, 0, 1))
    # cv2.line(dst, (100, 330), (510, 330), (0, 0, 1))
    # cv2.line(dst, (100, 380), (510, 380), (0, 0, 1))
    #
    # cv2.line(dst, (230, 100), (230, 510), (0, 0, 1))
    # cv2.line(dst, (280, 100), (280, 510), (0, 0, 1))
    # cv2.line(dst, (330, 100), (330, 510), (0, 0, 1))
    # cv2.line(dst, (380, 100), (380, 510), (0, 0, 1))
    #
    # cv2.line(dst, (180, 140), (430, 140), (0, 0, 1))
    # cv2.line(dst, (180, 470), (430, 470), (0, 0, 1))
    #
    # cv2.line(dst, (140, 180), (140, 430), (0, 0, 1))
    # cv2.line(dst, (470, 180), (470, 430), (0, 0, 1))

    # 左上定位码
    cv2.rectangle(dst, (100, 100), (170, 170), (0, 0, 1), -1)
    cv2.rectangle(dst, (110, 110), (160, 160), (255, 255, 255), -1)
    cv2.rectangle(dst, (120, 120), (150, 150), (0, 0, 1), -1)

    # 右上定位码
    cv2.rectangle(dst, (440, 100), (510, 170), (0, 0, 1), -1)
    cv2.rectangle(dst, (450, 110), (500, 160), (255, 255, 255), -1)
    cv2.rectangle(dst, (460, 120), (490, 150), (0, 0, 1), -1)

    # 左下定位码
    cv2.rectangle(dst, (100, 440), (170, 510), (0, 0, 1), -1)
    cv2.rectangle(dst, (110, 450), (160, 500), (255, 255, 255), -1)
    cv2.rectangle(dst, (120, 460), (150, 490), (0, 0, 1), -1)

    # 右下
    cv2.rectangle(dst, (430, 430), (480, 480), (0, 0, 1), -1)
    cv2.rectangle(dst, (440, 440), (470, 470), (255, 255, 255), -1)
    cv2.rectangle(dst, (450, 450), (460, 460), (0, 0, 1), -1)


# 绘制3x3模块
def draw33(data, x, y):
    row, col = [0, 0, 0], [0, 0, 0]
    flagr, flagc = False, False
    if x > y:
        flagr = True
    elif x < y:
        flagc = True
    for i in range(3):
        for j in range(3):
            if data[i * 3 + j] == '0':
                continue
            else:
                cv2.rectangle(dst, (y + 10 * j, x + 10 * i), (y + 10 * (j + 1), x + 10 + 10 * i), (0, 0, 1), -1)
                col[j] += 1
                row[i] += 1

    if flagr:
        for i in range(3):
            if row[i] % 2:
                continue
            else:
                cv2.rectangle(dst, (y + 30, x + 10 * i), (y + 50, x + 10 + 10 * i), (0, 0, 1), -1)

    if flagc:
        for i in range(3):
            if col[i] % 2:
                continue
            else:
                cv2.rectangle(dst, (y + 10 * i, x + 30), (y + 10 + 10 * i, x + 50), (0, 0, 1), -1)


# 绘制4x5模块
def draw45(data, x, y):
    for line in range(4):
        cnt = 0
        for i in range(5):
            if i < 4:
                if line * 4 + i >= len(data) or data[line * 4 + i] == '0':
                    continue
                else:
                    cnt += 1
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)
            else:
                if cnt % 2:
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)


# 绘制5x5模块
def draw55(data, x, y):
    col = [0, 0, 0, 0, 0]
    for line in range(5):
        row = 0
        for i in range(5):
            if i < 4 and line < 4:
                if line * 4 + i >= len(data) or data[line * 4 + i] == '0':
                    continue
                else:
                    row += 1
                    col[i] += 1
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)
            elif i == 4 and line < 4:
                if row % 2:
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)
                    col[i] += 1
            else:
                if i == 4:
                    pass
                elif col[i] % 2:
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)
                    col[i] += 1


# 绘制5x4模块
def draw54(data, x, y):
    col = [0, 0, 0, 0]
    for line in range(5):
        for i in range(4):
            if line < 4:
                if line * 4 + i >= len(data) or data[line * 4 + i] == '0':
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)
                    col[i] += 1
            else:
                if col[i] % 2:
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)


# 绘制4x5模块组
def Draw45(data, x, y):
    global idx

    for i in range(2):
        for j in range(5):
            Data = data[idx]
            draw45(Data, y + 40 * i, x + 50 * j)
            idx += 1


# 绘制5x4模块组
def Draw54(data, x, y):
    global idx

    for i in range(5):
        for j in range(2):
            Data = data[idx]
            draw54(Data, y + 50 * i, x + 40 * j)
            idx += 1


# 绘制5x5模块组
def Draw55(data, x, y):
    global idx

    for i in range(5):
        for j in range(5):
            Data = data[idx]
            draw55(Data, y + 50 * i, x + 50 * j)
            idx += 1


# 获取当前二维码编号
def get_id(num):
    id = ""
    if num == 0:
        id = 9 * '0'
        return id
    temp = []
    while num:
        temp.append(num % 2)
        num //= 2
    while temp:
        id += str(temp.pop())
    while len(id) < 9:
        id = '0' + id
    return id


# 绘制版本模块
def Drawenv(id):
    draw33(id, 430, 480)
    draw33(id, 480, 430)
    draw33(id, 480, 480)


# 绘制二维码
def Draw(id):
    Draw45(data, 180, 100)
    Draw54(data, 100, 180)
    Draw55(data, 180, 180)
    Draw54(data, 430, 180)
    Draw45(data, 180, 430)

    Drawenv(id)
    init()


if __name__ == "__main__":
    id = []
    for i in range(10):
        id.append(get_id(i))
    for i in range(10):
        newImg = (620, 620, 3)
        dst = np.zeros(newImg, np.uint8)
        dst.fill(255)
        idx = 0
        data = get_data()
        Draw(id[i])
        file_img = 'code' + str(i) + '.png'
        cv2.imwrite(file_img, dst)
