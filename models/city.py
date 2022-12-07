#!/usr/bin/python3
"""City module for HBNB project"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class for HBNB project"""

    __tablename__ = 'cities'

    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
        String(60), ForeignKey('states.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='cities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
