
from app.process.decode import decode_image
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

import cv2
import numpy as np
import io

router = APIRouter()

@router.get("")
async def get_basic_information():
    return "hello world"


@router.post("/type1")
async def process_image(file: UploadFile= File(...)):
    print("Getting image information...")
    content_type, extention, image = decode_image(file)
    # Process image
    print("Init images process...")
    imagensita = cv2.fastNlMeansDenoisingColored(image, None, 12,12,10,28)
    gray = cv2.cvtColor(imagensita, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,80,200)
    
    kernel_closi = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel_closi, iterations=4)
    img_copy = image.copy()
    contours,hierarchy = cv2.findContours(closing, 1, cv2.CHAIN_APPROX_NONE)

    areas = []
    hull = []
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        areas.append(area)
        convex = cv2.convexHull(contours[i], False)
        hull.append(convex)

    max_val = np.argmax(areas)
    areas[max_val] = 0

    print("Drawing contours...")
    for i in range(len(contours)):
        if i == max_val: continue
        cv2.drawContours(img_copy, contours, i, (0,255,0), 2,cv2.LINE_8, hierarchy, 100)
        cv2.drawContours(img_copy, hull, i, (255,0,0), 3, 8)

    # enconde data
    flag, encode = cv2.imencode(f".{extention}", img_copy)        
    return StreamingResponse(io.BytesIO(encode.tobytes()), media_type=content_type)



@router.post("/base")
async def process_image(file: UploadFile= File(...)):
    print("Getting image information...")
    content_type, extention, image = decode_image(file)
    # Process image


    # enconde data
    flag, encode = cv2.imencode(f".{extention}", image)        
    return StreamingResponse(io.BytesIO(encode.tobytes()), media_type=content_type)