#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
#    state = []
#    from models.engine.db_storage import DBStorage
#    from models import storage
#    if isinstance(storage, DBStorage):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
#        state = relationship("State", backref="cities")
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
