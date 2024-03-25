#!/usr/bin/python3
""" New engine 'DBStorage' """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """ The class 'DBStorage' """
    __engine = None
    __session = None

    def __init__(self):
        """ initializa the database connection """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query objects from the database """
        dict_objs = {}
        if cls:
            db_list = self.__session.query(cls).all()
            for target in db_list:
                key = target.__class__.__name__ + '.' + target.id
                dict_objs[key] = target
        else:
            for inst in classes.values():
                db_list = self.__session.query(inst).all()
                for target in db_list:
                    key = target.__class__.__name__ + '.' + target.id
                    dict_objs[key] = target
        return dict_objs

    def new(self, obj):
        """ Add a new object to the current session """
        if obj:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as erno:
                self.__session.rollback()
                raise erno

    def save(self):
        """ Commit the current session to save changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the database """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Set up the database tables and session for the current engine """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close the current session """
        if self.__session:
            self.__session.close()
