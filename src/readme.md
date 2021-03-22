#this file for source files
# 二维码生成
## 环境变量

QR_code requirement:

python 3.7

numpy 1.19.1

opencv-python 4.4.0.44

## 编码方式

定位码借鉴QR码，采用version6形式

存储有效信息采用4X4方块，每两行存储一个字符信息，采用ASCII码转换

信息存储分为4X5方块、5X4方块和5X5方块，第5行和第5列用于存放校验码

校验选择奇偶校验码

暂定将1存储为黑色方块，0存储为白色方块，后期可能会使用RGB来扩充二维码存储的信息

版本信息存储还未完成

# 定位
## 环境变量
detect requirement:

python 3.7

numpy 1.19.4

opencv-python 4.5.1.48
