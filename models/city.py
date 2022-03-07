#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class City(BaseModel, Base):
	""" The city class, contains state ID and name """
	__tablename__ = 'cities'
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name =  Column(String(128), nullable=False)
	state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
