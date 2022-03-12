#!/usr/bin/python3
""" Amenities Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
	""" The amenity class, contains name of amenities """
	__tablename__ = 'amenities'
	name =  Column(String(128), nullable=False)
	place_amenities = relationship("Place", secondary = association_table, back_populates = 'amenities')
