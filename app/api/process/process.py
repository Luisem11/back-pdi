
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

import cv2
import numpy as np
import io

router = APIRouter()

@router.get("")
async def get_basic_information():
    return "hello world"


@router.post("")
async def process_image(files: UploadFile= File(...)):
    image_str = np.fromstring(files.file.read(), np.uint8)
    content_type = files.content_type
    extention = content_type.split("/")[1] if content_type else 'png'
    image = cv2.imdecode(image_str, flags=cv2.COLOR_RGB2BGR)
    # Process image


    # enconde data
    flag, encode = cv2.imencode(f".{extention}", image)    
    
    return StreamingResponse(io.BytesIO(encode.tobytes()), media_type=content_type)

