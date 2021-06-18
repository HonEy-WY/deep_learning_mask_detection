import time
import cv2
import numpy as np
from PIL import Image
from yolo import YOLO

yolo=YOLO()
def detect_image(image_path):
    try:
        image = Image.open(image_path)
    except:
        print('Open Error! Try again!')
        pass
    else:
        r_image = yolo.detect_image(image)
        r_image.show()
        r_image.save(image_path.split('.')[0] + '_test.jpg')
    print('Finish detect!')

def detect_video(video_path):
    print('Start detect!')
    capture = cv2.VideoCapture(video_path)
    writer = None
    fps = 0.0
    while True:
        t1 = time.time()
        # 读取某一帧
        grabbed, frame = capture.read()
        if not grabbed:
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
        if writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'MP4V')
            writer = cv2.VideoWriter(video_path.split('.')[0] + '_result.mp4', fourcc, 30, (frame.shape[1], frame.shape[0]), True)
        writer.write(frame)
    # writer.release()
    capture.release()
    print('Finish detect!')

if __name__ == "__main__":
    path='D://Pycharm/yolov4-pytorch-master/data/1.jpg'
    # detect_video(path)
    detect_image(path)