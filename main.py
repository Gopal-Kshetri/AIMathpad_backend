from fastapi import FastAPI, File, UploadFile
from model_load import model_load
from predict import make_prediction
import numpy as np
import cv2
import base64
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    image = cv2.imread("./hello.png")
    result = make_prediction(image)
    return {"message": result}
    