#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import sessionmaker, Session, relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref="state", cascade="all, delete")

    @property
    def cities(self):
        """
        returns the list of City instances with state_id
        equals to the current State.id =>
        It will be the FileStorage relationship between State and City
        """
        session = Session()
        return (session.query(City).all())
