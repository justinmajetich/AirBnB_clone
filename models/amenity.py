from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Amenity class that creates amenities table"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
