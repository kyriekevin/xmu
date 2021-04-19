from encode1 import QR_code
from Video2Picture import Video2Pic
from Picture2Video import Pic2Video
import os
import sys
from Detect import detect_decode_1
sys.path.append(os.path.dirname(sys.path[0]))
cur_dir = os.getcwd() #获取当前路径
if __name__ == "__main__":
    #读取文件，转换为二维码
    QR_code(sys.argv[1])
     #将二维码序列转换为视频
    Pic2Video(sys.argv[2], 10)  # FPS=15

    Video2Pic(sys.argv[3])
    # #获得图片后转为二进制文件
    detect_decode_1()
