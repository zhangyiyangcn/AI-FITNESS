# AI-FITNESS
**Project**: Fitness counter using human key point detection

**Usage:**

```bash
git clone git@github.com:ZHENGYANG-QIAN/Human-body-key-point-detection.git
```

### Human pose estimation

This repository is the implementation of the paper [BlazePose: On-device Real-time Body Pose tracking](https://arxiv.org/pdf/2006.10204v1.pdf) [1], which is a lightweight, on-device single person-specific human pose estimation model. The inference pipeline is shown in Figure 1.

![11b070cb-0ae3-4ba9-9d62-196c207c33ed](README.assets/11b070cb-0ae3-4ba9-9d62-196c207c33ed.png)

![00c94594-2eba-4522-830a-be0173b0ec63](README.assets/00c94594-2eba-4522-830a-be0173b0ec63.png)

The code is available at: [Human-body-key-point-detection](https://github.com/1zeryu/Human-body-key-point-detection/tree/master/models).

### Mediapipe and Installation

In this project, I am calling the already trained BlazePose model from mediapipe for **human keypoint detection**.

You can configure the required environment by:

```python
pip install mediapipe==0.9.1.0 opencv-python numpy
```

You can click on the following links for more information:  [Pose-mediapipe](https://google.github.io/mediapipe/solutions/pose) 

You can also quickly learn how to detect key points in the human body by looking at my [tutorial](https://github.com/1zeryu/Human-body-key-point-detection/tree/master/tutorial).

### Movement classification
For common exercise movements such as squats and push-ups, one up and one down is the completion of one movement, and we need to train a classifier to identify whether the stance is up or down at this point.

A common approach is to use the kNN algorithm. You can click on this URL to read the [relevant code](https://github.com/1zeryu/Human-body-key-point-detection/blob/master/models/SquatCounter.ipynb).

You can add the required toolkit with the following code.

```python
pip install opencv-python==4.7.0.72
pip install mediapipe==0.9.1.0
pip install matplotlib==3.7.1
pip install numpy==1.24.2
pip install tqdm==4.65.0
pip install pillow==9.4.0
pip install requests==2.28.2
```

### Deploy

I chose to deploy the fitness counter to **Android**,Use Google's Android application template (ML kit):  [Pose Detection  | ML Kit  | Google Developers](https://developers.google.com/ml-kit/vision/pose-detection) 

You need to modify, debug and generate apk file in professional Android development tool - Android Studio:  [Download Android Studio & App Tools - Android Developers](https://developer.android.com/studio) 

<img src="README.assets\QQ图片20230614220914.jpg" alt="QQ图片20230614220914" style="zoom: 50%;" />

### Reference

\[1\]:Bazarevsky, Valentin, et al. "Blazepose: On-device real-time body pose tracking." *arXiv preprint arXiv:2006.10204* (2020). 

#### Some Useful Technical Links

 [基于BlazePose算法的机器人人体姿势识别与模仿)](https://github.com/TYZQ/graduation_project_2022) 

[Videos on Bilibili](https://www.bilibili.com/video/BV1dL4y1h7Q6?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click)

[人体姿态识别](https://blog.csdn.net/jieqiang3/article/details/122195209) 

[人体关键点的动作分类](https://blog.csdn.net/chenpy/article/details/121466383) 

[MediaPipe](https://mediapipe.dev/) 

[Pose Detection  | ML Kit  | Google Developers](https://developers.google.com/ml-kit/vision/pose-detection) 