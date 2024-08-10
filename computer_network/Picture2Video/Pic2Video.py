import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from PIL import Image
from encode1 import QR_code
import sys

img_root = os.getcwd()  # 获取当前路径


def Pic2Video(video_name, set_fps):
    imgPath = img_root + "/outputimg/"  # 读取图片路径
    videoPath = img_root + '/' + video_name  # 保存视频路径
    images = os.listdir(imgPath)
    fps = set_fps
    # VideoWriter_fourcc为视频编解码器 ('I', '4', '2', '0') —>(.avi) 、('P', 'I', 'M', 'I')—>(.avi)、('X', 'V', 'I', 'D')—>(.avi)、('T', 'H', 'E', 'O')—>.ogv、('F', 'L', 'V', '1')—>.flv、('m', 'p', '4', 'v')—>.mp4
    fourcc = VideoWriter_fourcc(*"mp4v")
    size = (620, 620)
    image = Image.open(imgPath + images[0])
    # print(image.size)
    videoWriter = cv2.VideoWriter(videoPath, fourcc, fps, frameSize=image.size)
    # print("开始转视频")
    for im_name in range(len(images)):
        frame = cv2.imread(imgPath + images[im_name])  # 这里的路径只能是英文路径
        # frame = cv2.imdecode(np.fromfile((imgPath + images[im_name]), dtype=np.uint8), 1)  # 此句话的路径可以为中文路径
        # print(im_name)
        videoWriter.write(frame)
    print("图片转视频成功")
    videoWriter.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    a = QR_code(sys.argv[1])
    Pic2Video(sys.argv[2], 9)
