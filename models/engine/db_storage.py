#!/usr/bin/python3
""" DBStorage module """
from models.base_model import BaseModel, Base
from models.user import User
from .. import engine
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    """ DBStorage Class """
    # Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize a DBStorage instance """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        # engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
        #                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        #                        pool_pre_ping=True)
        # Engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, host, db),
                                      pool_pre_ping=True)

        # Drop all tables if env variable HBNB_ENV is 'test'
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries the current database session for all objects depending on the class name. """
        object_dict = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                object_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for class_type in classes:
                query_result = self.__session.query(class_type)
                for obj in query_result:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    object_dict[key] = obj
        return object_dict

    def new(self, obj):
        """ Adding the object to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session. """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database. """

        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
