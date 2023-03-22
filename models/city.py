#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

=======
from sqlalchemy import Column, String, ForeignKey
from models import storage_type
>>>>>>> be257265eea6d7fed27d027438956c90f1af5b86


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
=======
    __tablename__ = 'cities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
>>>>>>> be257265eea6d7fed27d027438956c90f1af5b86
    else:
        state_id = ""
        name = ""
