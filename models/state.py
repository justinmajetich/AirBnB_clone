#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, nullable=Flase)
    name = Column(String(128), nullable=False,)
