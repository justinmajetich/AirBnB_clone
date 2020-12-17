#!/usr/bin/python3
"""
It’s time to change your storage engine and use SQLAlchemy
"""
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine path to the JSON files
        __session: objects will be stored
    """
    __engine = None
    __session = None
    __tables = [State, City]

    def __init__(self):
        """ Constructor of the database """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query of object depending of the class name
         if cls=none query of all type of objects
        """
<<<<<<< HEAD
        obj = {}
        if cls:
            session = self.__session.query(cls)
            for row in session.all():
                key = "{}.{}".format(cls.__name__, row.id)
                obj[key] = row
||||||| merged common ancestors
        my_session = self.__session
        dic = {}

        if instance(cls, str):
            class_print = cls
=======
        to_query = []
        new_dict = {}
        if cls is not None:
            results = self.__session.query(eval(cls.__name__)).all()
            for row in results:
                key = row.__class__.__name__ + '.' + row.id
                new_dict[key] = row
>>>>>>> 8e926373d6b88cd89d353d22ec94fe3992150c94
        else:
<<<<<<< HEAD
            for table in self.__talbes:
                session = self.__session.query(table)
                for row in query.all():
                    key = "{}.{}".format(table.__name__, row.id)
                    obj[key] = row
        return(obj)
       # if cls is None:
       #     object1 = self.__session.query(State).all()
       # else:
       #     if type(cls) == str:
       #         cls = eval(cls)
       #     object1 = self.__session.query(cls)
       # return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in object1}
||||||| merged common ancestors
            class_print = cls.__name__

        for x in my_session.query(eval(class_print)).all():
            class_type = x.__class__.__name__

            if class_type == class_print:
                dic[class_type + "." + x.id] = x

        return dic
=======
            for key, value in models.classes.items():
                try:
                    self.__session.query(models.classes[key]).all()
                    to_query.append(models.classes[key])
                except BaseException:
                    continue
            for classes in to_query:
                results = self.__session.query(classes).all()
                for row in results:
                    key = row.__class__.__name__ + '.' + row.id
                    new_dict[key] = row
        return new_dict
>>>>>>> 8e926373d6b88cd89d353d22ec94fe3992150c94

    def new(self, obj):
        """
        Add new obj
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """
        Save to database
        """
        self.__session.commit()

    def reload(self):
        """
        Create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
        Close method on the private session attribute on class Session
        """
        self.__session.close()
