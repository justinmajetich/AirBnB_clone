#!/usr/bin/python3
"""New engine DbStorage"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

class DBStorage:
    """Manage DB storage"""

    __engine = None
    __session = None

    def __init__(self):
        # call value in env
        user = os.getenv("HBNB_MYSQL_USER")
        pswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        #create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}}/{}'
        .format(user,
                pswd,
                host,
                db_name),
        pool_pre_ping=True
        )
        # create all table
        Base.metadata.create_all(self.__engine)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session"""
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        if cls is not None:
            q = self.session.query(cls).all()
            return(q)
        else:
            U = self.session.query(User).all()
            S = self.session.query(State).all()
            C = self.session.query(City).all()
            A = self.session.query(Amenity).all()
            P = self.session.query(Place).all()
            R = self.session.query(Review).all()
