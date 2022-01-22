from IPython.display import display
from PIL import Image
from yolo import YOLO


yolo = YOLO(model_path='logs/000/trained_weights_final.h5',
            classes_path='model_data/classes.txt')


image = Image.open('1.jpg')
result_image = yolo.detect_image(image)
display(result_image)