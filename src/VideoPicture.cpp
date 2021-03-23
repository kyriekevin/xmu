#include <iostream>
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;

// 将视频帧转成图片输出
void VideoToPictures()
{
	// 获取视频文件
	VideoCapture cap("D:\\Program Files\\ffmpeg\\ffmpeg-4.3.1-win64-static\\bin\\1.mp4");

	// 获取视频总帧数
	long totalFrameNumber = cap.get(CAP_PROP_FRAME_COUNT);
	cout << "total frames: " << totalFrameNumber << endl;
	Mat frame;
	bool flags = true;
	long currentFrame = 0;

	while (flags) {
		// 读取视频每一帧
		cap.read(frame);
		stringstream str;	
		cout << "正在处理第" << currentFrame << "帧" << endl;
		printf("\n");
    
		// 设置每10帧获取一次帧
		if (currentFrame % 10 == 0) {
			str << currentFrame /10<< ".jpg";
			imwrite("D:\\Program Files\\VS2019\\Sourse\\CNProject1\\pictures\\" + str.str(), frame);
		}
		if (currentFrame >= totalFrameNumber) {
			flags = false;
		}
		currentFrame++;
	}
}


//图片转换为视频
void PicturesToVideo()
{
	VideoWriter video;  
	video.open("test.avi", video.fourcc('I', '4', '2', '0'), 15.0, Size(1080, 720)); //目标视频，编码格式，帧率，大小

	String img_path = "D:\\Program Files\\ffmpeg\\ffmpeg-4.3.1-win64-static\\bin\\images\\";  //图片所在路径名
	vector<String> img;  
	glob(img_path, img, false);   //获取文件路径下的所有图片
	size_t count = img.size();

	for (size_t i = 1; i <= count; i++)
	{
		stringstream str;
		if (i < 10) str << "00" << i << ".jpg";
		else str << "0" << i << ".jpg";   //图片名
		Mat image = imread(img_path + str.str());
		if (!image.empty())
		{
			resize(image, image, Size(1080, 720));
			video << image;  
			cout << "正在处理第" << i << "帧" << endl;
		}
	}
	cout << "处理完毕！" << endl;
}
