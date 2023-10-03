
app = FastAPI()

@app.post("/processing_images")
async def call_processing_images(image: UploadFile = File(...)):
    image_bytes  = await image.read()
    image_path = save_in_disk(image_bytes)
    result = await processing_images.processing_images(image_path)
    return result

@app.post("/processing_text")
def call_processing_text(tex: str, request: Request):
    result = processing_text.processing_text(tex, request)
    return result

app.mount("/static", StaticFiles(directory="utils/abc"), name="static")

@app.get("/")
async def root():
    return {"message": "👋🌎 Hola Mundo! ve a /docs :)"}
