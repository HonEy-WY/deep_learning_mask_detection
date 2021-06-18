import numpy as np

DIR_PATH = 'D://Pycharm/yolov4-pytorch-master/'
input_videos = 'data/'
output_video = 'data/output_video.mp4'

OUTPUT_PATH = DIR_PATH + output_video
INPUT_PATH = DIR_PATH + input_videos
VIDEO_PATH = DIR_PATH + input_videos

DEFALUT_CONFIDENCE = 0.5
NMS_THRESHOLD = 0.3