#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City',
        cascade='all,delete,delete-orphan',
        backref=backref('state', cascade='all,delete'),
        passive_deletes=True,
        single_parent=True)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Man, so tired
            """
            from models import storage
            from models.city import City
            return [v for k, v in storage.all(City).items()
                    if v.state_id == self.id]
