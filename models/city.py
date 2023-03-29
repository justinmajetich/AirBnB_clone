#!/usr/bin/python3
"""City class for AirBnb project"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class that creates cities table"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all, delete-orphan",
                          backref="cities")