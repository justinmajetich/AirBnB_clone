#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import uuid


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True,
                default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
