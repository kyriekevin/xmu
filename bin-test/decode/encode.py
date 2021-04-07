from encode1 import QR_code
from Video2Picture import Video2Pic,Pic2Video
import os
import sys

cur_dir = os.getcwd() #获取当前路径
if __name__ == "__main__":
    #读取文件，转换为二维码
    a=QR_code(sys.argv[1])
     #将二维码序列转换为视频
    Pic2Video(sys.argv[2],int(sys.argv[3]))
   
