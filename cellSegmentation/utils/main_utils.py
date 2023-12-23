import os.path
import sys
import yaml
import base64

from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise AppException(e, sys) from e
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)
    

def decode_image(imgstring, filename):
    imgData = base64.b64decode(imgstring)
    with open("./data/" + filename, "wb") as file_obj:
        file_obj.write(imgData)
        file_obj.close()

def encode_image_base_64(cropped_image_path):
    with open(cropped_image_path, "rb") as file_obj:
        return base64.b64encode(file_obj.read( ))