from app.process.select_elements import selectElements
from app.process.decode import decode_image
from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import StreamingResponse

import cv2
import numpy as np
import io
from base64 import b64encode

router = APIRouter()


@router.get("")
async def get_basic_information():
    return "hello world"


@router.post("/type2")
async def process_image1(
    file: UploadFile = File(...)
):

    print("Getting image information...")
    content_type, extention, image = decode_image(file)
    print(content_type, extention)
    # Process image
    print("processing image")
    img_c, img_cH, img_center, img_kmeans, img_cseg = selectElements(image)

    # enconde data
    print("encoding images")
    _, encode_c = cv2.imencode(f".png", img_c)
    _, encode_cH = cv2.imencode(f".png", img_cH)
    _, encode_center = cv2.imencode(f".png", img_center)
    _, encode_kmeans = cv2.imencode(f".png", img_kmeans)
    _, encode_cseg = cv2.imencode(f".png", img_cseg)

    dato_c = b64encode(encode_c).decode('utf-8')
    dato_cH = b64encode(encode_cH).decode('utf-8')
    dato_center = b64encode(encode_center).decode('utf-8')
    dato_kmeans = b64encode(encode_kmeans).decode('utf-8')
    dato_cseg = b64encode(encode_cseg).decode('utf-8')
    data = {
        "contourns": {
            "data": dato_c,
            'type': 'image/png'
        },
        "convexHull": {
            "data": dato_cH,
            'type': 'image/png'
        },
        "centers": {
            "data": dato_center,
            'type': 'image/png'
        },
        'kmeans':  {
            "data": dato_kmeans,
            'type': 'image/png'
        },
        'colorSeg':  {
            "data": dato_cseg,
            'type': 'image/png'
        }
    }

    return data


@router.post("/base")
async def process_image(file: UploadFile = File(...)):
    print("Getting image information...")
    content_type, extention, image = decode_image(file)
    # Process image

    # enconde data
    flag, encode = cv2.imencode(f".{extention}", image)
    # return StreamingResponse(io.BytesIO(encode.tobytes()), media_type=content_type)

    dato = b64encode(encode).decode('utf-8')
    data = [
        {
            "data": dato,
            'type': content_type
        },
        {
            "data": dato,
            'type': content_type
        },
        {
            "data": dato,
            'type': content_type
        }
    ]

    return data
