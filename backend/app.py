from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from detection import object_detection
from models import db

app = FastAPI(title="Image Recognition Service")

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    detections = object_detection.detect_objects(image_bytes)
    results = []
    for bbox, label, cropped in detections:
        identity = db.search_embedding(cropped, label)
        record = db.save_record(cropped, label, identity)
        results.append(record)
    return JSONResponse({"detections": results})
