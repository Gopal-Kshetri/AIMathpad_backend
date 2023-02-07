from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import base64
import cv2

from model_load import model_load
from predict import make_prediction
import numpy as np
from pydantic import BaseModel
app = FastAPI()

class Data(BaseModel):
    img_file: str

origins = ['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    img_file:str

@app.post("/process-image")
async def process_image(inp: Data):
    img_64 = inp.img_file
    # with open("imageToSave.jpg", "wb") as fh:
    #     fh.write(base64.decodebytes(img_64.encode()))
    nparr = np.fromstring(base64.b64decode(img_64), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    black_mask = image[:,:,-1]>0

    image[black_mask] = [255,255,255,255]
    
    cv2.imwrite('hellohi.jpg',image)
    
    result = make_prediction(image)
    print(result)
    return {"message": result}
    
@app.post("/uploadfile/")
async def create_upload_file(data: Data):
    return {"filename": data.img_file}