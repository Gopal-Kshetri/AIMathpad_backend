from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import base64
import cv2

from predict import make_prediction
import numpy as np
from pydantic import BaseModel
import io
from munch import Munch

import tensorflow as tf
from tensorflow import keras

# For pix2tex
# import pix2tex
from pix2tex.cli import LatexOCR, get_model, in_model_path
from PIL import Image
# import pix2tex.convert as p2t

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
    nparr = np.fromstring(base64.b64decode(img_64), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    black_mask = image[:,:,-1]>0
    image[black_mask] = [255,255,255,255]

    image_path = 'hellohi.jpg'
    
    cv2.imwrite(image_path, image)
    # result = make_prediction('hellohi.jpg')

    # Implementing pix2tex    
    image = Image.open(image_path)
    

    #Load Model
    import os
    checkpoint_path = os.path.join(os.getcwd(),"models/weights3.pth")
    arguments = Munch({'config': 'settings/config.yaml', 'checkpoint': checkpoint_path, 'no_cuda': True, 'no_resize': False})
    # model = keras.models.load_model(checkpoint_path)
    model = LatexOCR(arguments=arguments)
    # Result
    result = model(image)

    # result = make_prediction(image_path)

    print("-->",result)
    return {"message": result}
    
@app.post("/uploadfile/")
async def create_upload_file(data: Data):
    return {"filename": data.img_file}


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
async def homePage(request:Request,response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request})
