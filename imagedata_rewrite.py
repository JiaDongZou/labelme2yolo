import base64
import json
import os
from PIL import Image


def add_image_data(json_dir, image_dir):
    json_files = os.listdir(json_dir)
    # image_files = os.listdir(image_dir)

    for json_file in json_files:
        json_path = os.path.join(json_dir, json_file)
        image_name = os.path.splitext(json_file)[0] + ".jpg"
        image_path = os.path.join(image_dir, image_name)

        if os.path.isfile(json_path) and os.path.isfile(image_path):
            with open(json_path, 'r') as f:
                json_data = json.load(f)

            with open(image_path, 'rb') as f:
                image_data = f.read()
                encoded_image_data = base64.b64encode(image_data).decode('utf-8')

            json_data['imageData'] = encoded_image_data

            with open(json_path, 'w') as f:
                json.dump(json_data, f)


# 使用示例：
json_dir = '/home/dong/dataset/date_topic/camera4_pic/labelnew'
image_dir = '/home/dong/dataset/date_topic/camera4_pic/2023-06-02_15-13-46_4_0'
add_image_data(json_dir, image_dir)
