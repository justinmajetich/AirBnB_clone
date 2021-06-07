#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60),  ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60),  ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
