# -*- codeing = utf-8 -*-
# @Time : 2021/4/7 23:40
# @Author : Sy
# @File : decode.py
# @Software : VSCode
from detect_decode import detect_decode
from Video2Picture import Video2Pic
import os
import sys

if __name__ == "__main__":
     #将视频转换为二维码序列
    Video2Pic(sys.argv[1])
    #读取文件，转换为二维码
    a=detect_decode()