#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)
from models import storage
import os

""" Setting env variables """
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_ENV = os.getenv('HBNB_ENV')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "state"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ returns the list of City instances with state_id
        == the current State.id """

        """ Since this is working with file storage, we're assuming that this is
        not using the db """
        """engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        places = session.query(State, City).filter(
            State.id, State.id == City.state_id).order_by(City.id)
        print(places)"""

        #check city id where state_id == self.id
        allcities = storage.all(State)
        print(allcities)
        """ statecities = []"""
        """for key, value in allcities:
            if (i.id == self.id)
                statecities.append(i)"""

