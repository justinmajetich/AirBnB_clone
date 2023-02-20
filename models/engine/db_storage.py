#!/usr/bin/python3
"""This is database storage class for Airbnb
"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from sqlalchemy import create_engine
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import environ, getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:

    """
    A DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        eng = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(eng.format(getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB'),
                                      pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary with objects of cls
        """
        newdict = {}
        if not cls:
            query = self.__session.query(State).all()
            query += self.__session.query(City).all()
            query += self.__session.query(User).all()
            query += self.__session.query(Place).all()
            query += self.__session.query(Review).all()
            query += self.__session.query(Amenity).all()
            for i in query:
                key = i.__class__.__name__ + "." + i.id
                newdict[key] = i
            # print(newdict[key])
        else:
            if isinstance(cls, str):
                s = self.__session.query(eval(cls)).all()
            else:
                s = self.__session.query(cls).all()
            for i in s:
                key = i.__class__.__name__ + "." + i.id
                newdict[key] = i
        return (newdict)

    def new(self, obj):
        """adds the object to the current database session
        """
        self.__session.add(obj)
        self.__session.commit()
        # self.save()

    def save(self):
        """
        commits all changes of the current database session
        """
        # self.__session.flush()
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None
        """
        if obj:
            obj_id = obj.id
            obj_result = self.__session.query(
                type(obj).filter(type(obj).id == obj_id.delete()))
        #    self.__session.commit()

    def reload(self):
        """creates all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        Session_s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_s)
        self.__session = Session()

    def close(self):
        """calls remove() method on the private session attribute
        or close() on the class Session"""
        self.__session.close()
