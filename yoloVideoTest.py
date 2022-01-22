from PIL import Image
from yolo import YOLO
from yolo import detect_video

yolo = YOLO(model_path = 'model_data/yolo_weights.h5', classes_path = 'model_data/coco_classes.txt')

detect_video(yolo, 'video/z.mp4', 'video/detect.mp4')

# detect_video(yolo, 0, 'video/detect.mp4')





