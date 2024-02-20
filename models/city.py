#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
# from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship
# from models.base_model import BaseModel, Base


class City(BaseModel):
    """ The city class, contains state ID and name """
    
    name = ''
    state_id = ''