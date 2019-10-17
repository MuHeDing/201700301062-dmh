# 201700301062-dmh
my homework of Artificial Intelligence patience

## 工作进展
* 学习实用dlib库进行人脸检测，使用 shape_predictor_68_face_landmarks.dat 来进行人脸检测，已经成功实现功能
* 学习实用 opencv视频读取，读取视频或者图片，进行实时获取，然后调用dlib进行多人脸检测





## 论文一：
Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks

### 知识点：
* 任务进行人脸检测 和 对齐，提高人脸检测的精度
* 使用了 deep cascaded multi-task framework
包括三个精心设计的深度卷积网络，这些网络能够从粗到精地预测人脸和地标位置。

## 论文二：
FaceNet: A Unified Embedding for Face Recognition and Clustering

### 知识点：
* 任务是 进行人脸验证，识别，聚类 
* 在这篇论文中，我们提出了一个系统，称为FaceNet，它直接学习从人脸图像到紧凑的欧几里德空间的映射，其中距离直接对应于人脸相似性的度量。

## 论文三：
Improved Selective Refinement Network for Face Detection
### 知识点：
* 任务 进行人脸检测
* 使用了选择性精细网络(SRN)人脸检测将两步分类和回归操作有选择地引入基于锚点的人脸检测中，以减少误报和同时改善定位和精度。
