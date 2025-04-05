from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from PIL import Image
import os
from image_utils import process_image

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/process-image/")
async def process_image_api(
    file: UploadFile = File(...),
    width: int = Form(...),
    height: int = Form(...),
    rotate: int = Form(...),
    flip: str = Form(...),
    crop_x: int = Form(...),
    crop_y: int = Form(...),
    crop_w: int = Form(...),
    crop_h: int = Form(...)
):
    input_path = os.path.join(UPLOAD_DIR, "input.png")
    output_path = os.path.join(UPLOAD_DIR, "output.png")

    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    process_image(input_path, output_path, width, height, rotate, flip, crop_x, crop_y, crop_w, crop_h)

    return FileResponse(output_path, media_type="image/png")
