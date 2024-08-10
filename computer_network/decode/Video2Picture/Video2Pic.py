import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from PIL import Image
from encode1 import QR_code
import sys

img_root = os.getcwd()  # 获取当前路径





def Video2Pic(videopath):

    videoPath = img_root + '/' + videopath  # 读取视频路径
    folder_name = 'output'  # 定义新建文件夹名
    if os.path.isdir(img_root):
        os.mkdir(os.path.join(img_root, folder_name))  # 新建文件
    imgPath = img_root + "/output/"  # 保存图片路径
    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    if not cap.isOpened():  # 是否成功打开
        print("Please check the path.")
    frame_interval =9
    frame_count = 0
    cnt = 0
    while 1:
        suc, frame = cap.read()
        cnt += 1
        frame_count += 1
        if not suc:
            break
        cv2.imwrite(imgPath + "%02d.png" % frame_count, frame)
        cv2.waitKey(1)
    print("视频转图片成功")
    cap.release()




if __name__ == '__main__':
    a = QR_code()
    Video2Pic()
