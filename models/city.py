#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, string, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="user", cascade="all, delete-orphan")
else:
    state_id = ""
    name = ""
