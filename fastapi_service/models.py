from database import Base
from sqlalchemy import Column, Integer, String, Text

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    detected_data = Column(Text)  # Stores JSON object as text
