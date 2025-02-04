from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Detection
from schemas import DetectionSchema
from crud import get_detections

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoint: Fetch object detection results
@app.get("/detections", response_model=list[DetectionSchema])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_detections(db, skip=skip, limit=limit)
