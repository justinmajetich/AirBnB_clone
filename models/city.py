#!/usr/bin/env python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, id_generator
from sqlalchemy import ForeignKey, Column, String, CheckConstraint

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__  = 'cities'
    id = Column(String(60), primary_key=True, default=id_generator)
    state_id = Column(ForeignKey('states.id'), nullable=False)
    name = Column(String(128), CheckConstraint("name > \'\'"), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.state_id = kwargs['state_id']
