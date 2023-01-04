#!/usr/bin/python3
""" Defines a DBStorage engine, an alternative to FileStorage """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Place': Place, 'Amenity': Amenity, 'Review': Review}


class DBStorage:
    """ Defines the attributes and methods connect to database """
    # private class attributes
    __engine = None
    __session = None

    # public class methods
    def __init__(self):
        """ Instantiates the class by:
        1. creating an engine (self.__engine) which must be linked to the
        MySQL db and user created before (in setup)
        2. retrieve details (user, pwd, database & host) via environmental
        variables
        3. drop all tables if the environment variable HBNB_ENV is not test """
        # create an engine
        from models.base_model import Base
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER',
                                                        None),
                                              os.getenv(
                                                  'HBNB_MYSQL_PWD', None),
                                              os.getenv('HBNB_MYSQL_DB',
                                                        None)),
                                      pool_pre_ping=True)
        # check that HBNB_ENV is set to test, else drop all tables
        env_val = os.getenv('HBNB_ENV', None)
        if (env_val and env_val == 'test'):
            pass
        else:
            # drop all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries the current database session (self.__session) for
        all objects depending on class name if provided """
        # self.__session =  Session()
        # query database based on whether a cls is provided
        if cls and cls in classes.values():
            # return objects of cls
            objs = self.__session.query(cls).all()
        else:
            # return all objects
            objs = []
            per_cls1 = self.__session.query(State).all()
            per_cls2 = self.__session.query(City).all()
            objs.extend(per_cls1)
            objs.extend(per_cls2)
        return objs

    def new(self):
        """ adds the object to the current database session
        (self.__session) """
        # self.__session =  Session()
        # add this (self) object to current db session
        self.__session.add(self)

    def save(self):
        """  commits all changes of the current session (self.__session) """
        # self.__session =  Session()
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from current db session if obj is not None """
        # check that object is defined and delete it
        if obj:
            # self.__session =  Session()
            _id = obj.id
            _cls = obj.to_dict()['__class__']
            # query for the obj from db
            to_del = self.__session.query(classes[_cls]).get(_id)
            # to_del = self.__session.query(classes[_cls])
            # .filter(classes[_cls].id == _id)
            self.__session.delete(to_del)
            self.save()  # save the changes

    def reload(self):
        """ Creates all tables in the database as well as a current session
        from the engine (self.__engine) by using sessionmaker & scoped session
        to make sure it's (the session) thread-safe """
        # create all tables
        Base.metadata.create_all(self.__engine)
        # create a pre-configured session that is thread-local scoped
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        # create a session from the factory, to use
        self.__session = Session()
