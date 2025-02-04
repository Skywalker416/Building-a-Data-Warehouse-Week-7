from pydantic import BaseModel

class DetectionSchema(BaseModel):
    id: int
    image_name: str
    detected_data: str

    class Config:
        orm_mode = True
