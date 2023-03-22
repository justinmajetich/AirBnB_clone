#!/usr/bin/python3
""" class City """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ class City """
    __tablename__ = 'cities'

    # if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    name = Column(
        String(128),
        nullable=False)
    state_id = Column(
        String(60),
        ForeignKey('states.id'),
        nullable=False)
    places = relationship(
        'Place', backref='cities', cascade='delete')
    # else:
    #     name = ""
    #     state_id = ""

