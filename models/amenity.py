#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Mapped[str] = mapped_column(String(128), nullable=False)
