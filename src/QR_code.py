# -*- codeing = utf-8 -*-
# @Time : 2021/3/21 12:41
# @Author : zyz
# @File : QR_code.py
# @Software : PyCharm

import cv2
import numpy as np

# 编码
def encode(str):
    return ' '.join([bin(ord(ch)).replace('0b', '') for ch in str])

# 解码
def decode(str):
    return ''.join([chr(i) for i in [int(b, 2) for b in str.split(' ')]])

# 读取文件信息
def get_data():
    binfile = open('text.txt', "r")
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
    while len(cur) < 8:
        cur = '0' + cur
    while len(cur) < 16:
        cur += '0'
    Data.append(cur)
    binfile.close()
    return Data

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

def draw45(str, x, y):
    for line in range(4):
        cnt = 0
        for i in range(5):
            if i < 4:
                if line * 4 + i >= len(str) or str[line * 4 + i] == '0':
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

def draw55(str, x, y):
    col = [0, 0, 0, 0, 0]
    for line in range(5):
        row = 0
        for i in range(5):
            if i < 4 and line < 4:
                if line * 4 + i >= len(str) or str[line * 4 + i] == '0':
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

def draw54(str, x, y):
    col = [0, 0, 0, 0]
    for line in range(5):
        for i in range(4):
            if line < 4:
                if line * 4 + i >= len(str) or str[line * 4 + i] == '0':
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1), -1)
                    col[i] += 1
            else:
                if col[i] % 2:
                    continue
                else:
                    cv2.rectangle(dst, (y + 10 * i, x + 10 * line), (y + 10 * (i + 1), x + 10 + 10 * line), (0, 0, 1),
                                  -1)

def Draw45(data, x, y):
    global idx

    for i in range(2):
        for j in range(5):
            str = data[idx]
            draw45(str, y + 40 * i, x + 50 * j)
            idx += 1

def Draw54(data, x, y):
    global idx

    for i in range(5):
        for j in range(2):
            str = data[idx]
            draw54(str, y + 50 * i, x + 40 * j)
            idx += 1

def Draw55(data, x, y):
    global idx

    for i in range(5):
        for j in range(5):
            str = data[idx]
            draw55(str, y + 50 * i, x + 50 * j)
            idx += 1

def get_id():
    num = int(input("请输入当前二维码编号:"))
    temp = []
    id = ""
    while num:
        temp.append(num % 2)
        num //= 2
    while temp:
        id += str(temp.pop())

    return id

def Drawenv(id):
    pass

def Draw():
    str = get_data()
    id = get_id()
    print(id)
    Draw45(str, 180, 100)
    Draw45(str, 180, 430)
    Draw54(str, 100, 180)
    Draw54(str, 430, 180)
    Draw55(str, 180, 180)
    Drawenv(id)
    init()

if __name__ == "__main__":
    newImg = (620, 620, 3)
    dst = np.zeros(newImg, np.uint8)
    dst.fill(255)
    idx = 0
    Draw()
    cv2.imshow('test0', dst)
    cv2.waitKey(0)
