from fastapi import FastAPI, File, UploadFile
from api.endpoints import processing_images

app = FastAPI()

@app.post("/processing_images")
async def processing_images(iamge: UploadFile):
    content = await image.read()
    result = processing_images(content)
    return {"prediction": result}