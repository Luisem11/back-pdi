from cv2 import imdecode, COLOR_RGB2BGR
from numpy import fromstring, uint8


def decode_image(file):
    image_str = fromstring(file.file.read(), uint8)
    content_type = file.content_type
    extention = content_type.split("/")[1] if content_type else 'png'
    image = imdecode(image_str, flags=COLOR_RGB2BGR)

    return content_type, extention, image
