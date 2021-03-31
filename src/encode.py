# -*- codeing = utf-8 -*-
# @Time : 2021/3/31 14:23
# @Author : zyz
# @File : encode.py
# @Software : PyCharm

import cv2
import numpy as np
import random
import string
import CRC


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
    for i in range(50):
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
    Data = []
    cnt = 0
    for i in data:
        if i == ' ':
            while len(cur) < 8:
                cur = '0' + cur
            Data.append(cur)
            cur = ''
            cnt += 1
        else:
            cur += i
    while len(cur) < 8:
        cur += '0'
    Data.append(cur)
    binfile.close()
    return Data


def process_data(Data):
    data = ""
    for x in Data:
        crc = CRC.CRC(x, 4)
        for y in crc.code:
            if y == 1:
                data += "1"
            else:
                data += "0"

    return data


# 初始化定位码
def init():
    # 左上定位码
    cv2.rectangle(dst, (50, 50), (85, 85), (0, 0, 1), -1)
    cv2.rectangle(dst, (55, 55), (80, 80), (255, 255, 255), -1)
    cv2.rectangle(dst, (60, 60), (75, 75), (0, 0, 1), -1)

    # 右上定位码
    cv2.rectangle(dst, (520, 50), (555, 85), (0, 0, 1), -1)
    cv2.rectangle(dst, (525, 55), (550, 80), (255, 255, 255), -1)
    cv2.rectangle(dst, (530, 60), (545, 75), (0, 0, 1), -1)

    # 左下定位码
    cv2.rectangle(dst, (50, 520), (85, 555), (0, 0, 1), -1)
    cv2.rectangle(dst, (55, 525), (80, 550), (255, 255, 255), -1)
    cv2.rectangle(dst, (60, 530), (75, 545), (0, 0, 1), -1)

    # 右下
    cv2.rectangle(dst, (515, 515), (540, 540), (0, 0, 1), -1)
    cv2.rectangle(dst, (520, 520), (535, 535), (255, 255, 255), -1)
    cv2.rectangle(dst, (525, 525), (530, 530), (0, 0, 1), -1)


def draw(data):
    idx = 0
    for x in range(50, 555, 5):
        for y in range(50, 555, 5):
            if (x >= 50 and x <= 85 and y >= 50 and y <= 85):
                continue
            elif (x >= 515 and x <= 555 and y >= 50 and y <= 85):
                continue
            elif (x >= 50 and x <= 85 and y >= 515 and y <= 555):
                continue
            elif (x >= 515 and x <= 555 and y >= 515 and y <= 555):
                continue
            else:
                # c = [0, 0, 0]
                # for i in range(3):
                #     if data[idx] == '1':
                #         c[i] = 1
                #     idx += 1
                # cv2.rectangle(dst, (x, y), (x + 5, y + 5), (0 + 255 * c[0], 0 + 255 * c[1], 0 + 255 * c[2]), -1)
                if data[idx] == "1":
                    cv2.rectangle(dst, (x, y), (x + 5, y + 5), (0, 0, 1), -1)
                idx += 1

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
                cv2.rectangle(dst, (y + 5 * j, x + 5 * i), (y + 5 * (j + 1), x + 5 + 5 * i), (0, 0, 1), -1)
                col[j] += 1
                row[i] += 1

    if flagr:
        for i in range(3):
            if row[i] % 2:
                continue
            else:
                cv2.rectangle(dst, (y + 15, x + 5 * i), (y + 25, x + 5 + 5 * i), (0, 0, 1), -1)

    if flagc:
        for i in range(3):
            if col[i] % 2:
                continue
            else:
                cv2.rectangle(dst, (y + 5 * i, x + 15), (y + 5 + 5 * i, x + 25), (0, 0, 1), -1)


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


# 绘制二维码
def Draw():
    idx = 111
    id = get_id(idx)
    Drawenv(id)
    init()


# 绘制版本模块
def Drawenv(id):
    draw33(id, 515, 540)
    draw33(id, 540, 515)
    draw33(id, 540, 540)


newImg = (720, 720, 3)
dst = np.zeros(newImg, np.uint8)
dst.fill(255)
Draw()
data = get_data()
data = process_data(data)
draw(data)
cv2.imshow("encode", dst)
cv2.waitKey()
# cv2.imwrite("1.png", dst)
