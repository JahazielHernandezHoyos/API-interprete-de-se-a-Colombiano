import cv2
import os
from fastapi import Request
input_images_path = "utils/abc"
files_names = os.listdir(input_images_path)

def processing_text(String: str, request: Request):
    text = String.upper()
    text = list(text)
    array = []
    for x in text:
        for file_name in files_names:
            image_path = input_images_path + "/" + file_name
            letter = ''.join(map(str, x))
            letter_image = file_name.split(".")[0]
            if letter == letter_image:
                host = request.headers["host"]
                url = "http://" + host + "/static/" + file_name
                array.append(url)
    return array