from fastapi import FastAPI, File, UploadFile
from model_load import model_load
from predict import make_prediction
import numpy as np
import cv2
app = FastAPI()


from fastapi import FastAPI, File, UploadFile
import cv2

app = FastAPI()

@app.post("/process-image")
async def process_image(file: UploadFile):
    image = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), -1)
    result = make_prediction(image)
    return {"message": result}
