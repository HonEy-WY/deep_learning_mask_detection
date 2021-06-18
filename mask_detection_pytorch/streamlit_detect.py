import cv2
import time
from yolo import YOLO
from PIL import Image
import streamlit as st
import os
import torch
import config
import numpy as np
yolo = YOLO()
torch.cuda.current_device()
#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
def detect_image(image_path):
    print('Start detect!')
    try:
        image = Image.open(image_path)
    except:
        print('Open Error! Try again!')
        pass
    else:
        r_image = yolo.detect_image(image)
#         r_image.show()
        r_image.save(image_path.split('.')[0] + '_test.jpg')
    print('Finish detect!')

#-------------------------------------#
#       对一段视频进行检测
#-------------------------------------#
def detect_video(video_path):
    st.write(f"Start detect!")
    #print('Start detect!')
    capture = cv2.VideoCapture(video_path)
    writer = None
    fps = 0.0
    FRAME_WINDOW = st.image([])
    while True:
        t1 = time.time()
        # 读取某一帧
        grabbed, frame = capture.read()
        if not grabbed:
            # cv2.imshow('image_win',frame)
            break
        # opencv读取的是BGR，格式转变，BGRtoRGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))
        # 进行检测
        frame = np.array(yolo.detect_image(frame))
        # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        fps  = (fps + (1. / (time.time() - t1))) / 2
        print("FPS: %.2f" % (fps))
        frame = cv2.putText(frame, "FPS: %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        FRAME_WINDOW.image(frame[:, :, ::-1])
        # if writer is None:
        #     fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        #     writer = cv2.VideoWriter(video_path.split('.')[0] + '_result.mp4', fourcc, 30, (frame.shape[1], frame.shape[0]), True)
        # writer.write(frame)
    # writer.release()
    capture.release()
    st.write(f"Finish detect!")
    #print('Finish detect!')

def run():
    st.title('Object Detection in Video')
    option = st.radio('', ['Choose a test video', 'Upload your own video (.mp4 only)', 'Camera'])
    st.sidebar.title('Parameters')
    confidence_slider = st.sidebar.slider('Confidence Threshold', 0.0, 1.0, 0.5, 0.05)
    nms_slider = st.sidebar.slider('Non-Max Suppression Threshold', 0.0, 1.0, 0.3, 0.05)

    if option == 'Choose a test video':
        test_videos = os.listdir(config.INPUT_PATH)
        test_video = st.selectbox('Please choose a test video', test_videos)
    elif option == 'Camera':
        test_video = None
    else:
        test_video = st.file_uploader('Upload a video', type=['mp4'])
        st.video(test_video)
        if test_video is not None:
            #stringio = StringIO(test_video.decode("utf-8"))
            #test_video = test_video.read()
            #st.video(test_video)
            pass
        else:
            st.write('** Please upload a test video **')

    #end_video_path=''
    if test_video is not None:
        video = config.VIDEO_PATH + test_video
    else:
        video=0
    if st.button ('Detect Objects'):
        time.sleep(3)
        detect_video(video)
if __name__ == '__main__':
    run()
