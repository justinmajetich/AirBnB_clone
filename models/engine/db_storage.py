#!/usr/bin/python3
"""
"""

import os
from models.base_model import Base


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        from sqlalchemy import create_engine
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects"""
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User

        objects = {}
        if cls:
            object_list = self.__session.query(cls).all()
            for obj in object_list:
                objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                    }
            # loop each class to query for its table
            for class_name, class_ in classes.items():
                # returns a list of obj of the queried class
                object_list = self.__session.query(class_).all()
                print(object_list)
                for obj in object_list:
                    objects[f"{class_name}.{obj.id}"] = obj
        return objects

    def new(self, obj):
        """Add an object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
