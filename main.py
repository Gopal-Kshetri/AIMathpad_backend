from fastapi import FastAPI, File, UploadFile
from model_load import model_load
from predict import make_prediction
import numpy as np
import cv2
<<<<<<< HEAD

from pydantic import BaseModel

=======
import base64
from fastapi.middleware.cors import CORSMiddleware
>>>>>>> 270348ee1d2e560fbe7412e893dae51eec917aba
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import cv2

app = FastAPI()


origins = [
    "http://localhost",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import base64

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
    