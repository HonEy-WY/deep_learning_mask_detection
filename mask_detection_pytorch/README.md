#                           口罩检测DEMO

### 实现的内容

- 对单张图片进行检测
- 对一段视频进行检测
- 在streamlit上形成DEMO对视频检测或者调用摄像头检测

### 数据集

本项目image数据集：[链接](https://pan.baidu.com/s/1Q4QMq9pugNpgV_kT5ms51w)  提取码：pwqi

本项目label数据集：[链接](https://pan.baidu.com/s/1Voqx7-xxUnymQhe4MoUa6A)  提取码：3eqh

### 依赖库

- Python >= 3.7
- PyTorch >= 1.4.0
- opencv-python >= 4.2.0.32
- Pillow >= 7.0.0

### 模型

  -  本项目训练模型：[链接](https://pan.baidu.com/s/1_NQgoDnz-F3q7zH2A0eFHA)  提取码：au2c

### 训练步骤

1. 本文使用**VOC**格式进行训练。  
2. 训练前将label文件放在**VOCdevkit**文件夹下的**VOC2007**文件夹下的**Annotation**中。  
3. 训练前将image文件放在**VOCdevkit**文件夹下的**VOC2007**文件夹下的**JPEGImages**中。  
4. 在训练前利用**voc2yolo4.py**文件生成对应的txt。  
5. 再运行根目录下的**voc_annotation.py**

6. 此时会生成对应的2007_train.txt，每一行对应其**图片位置**及其**真实框的位置**。  
7. 运行train.py即可开始训练。

### 预测步骤

#### **预测准备：**

- 需要在网盘下载模型后解压到**model_data**目录下
- 如果是CPU运行需要将**yolo.py**文件中的cuda改为**False**
- 在**yolo.py**文件中更改自己的**模型**，**mask_classes.txt**等数据存放位置
- 更改**config.py**文件中**DIR_PATH**为自己的数据存放位置所在的**目录**

#### **python文件下运行**：

**预测单张图片**:

​	将path改为图片的路径然后调用函数**detect_image()**即可

**预测一段视频：**

​	将path改为视频的路径然后调用函数**detect_video()**即可

<font color='orange'>注：</font>以上生成的预测文件均会在原目录上出现，且命名格式为原名后+_result

例如：test.mp4-->test_result.mp4

#### 在streamlit上形成demo运行:

- 在**YOLO4_mask_detection**目录下按shift右键打开**Powershell**窗口并在其中输入**streamlit run streamlit_detect.py**，等待程序启动

- 然后选择放在data目录里的文件开始检测即可
- 预测后生成的文件都在data目录下，如果有需要改的，可以在**config.py**文件上更改