#!/usr/bin/python3
# KASPER edited @ 10/31 12:55pm
""" database storage engine using SQLAlchemy """
from sqlalchemy import (create_engine, select)
from sqlalchemy import MetaData
from sqlalchemy.orm import (sessionmaker, scoped_session)

import os


class DBStorage:
    """ Database storage engine """

    __engine = None
    __session = None

    def __init__(self):
        un = os.getenv('HBNB_MYSQL_USER')
        pw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        session_info = f"mysql+mysqldb://{un}:{pw}@{host}/{db}"
        self.__engine = create_engine(session_info, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            md = MetaData()
            md.reflect(self.__engine)
            md.drop_all(self.__engine)

    def all(self, cls=None):
        """ TBC """
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        dictionary = {}
        classes = {"State": State, "City": City, "User": User, "Place": Place, "Review": Review}
        if cls is None:
            for clas in classes:
                user_obj = self.__session.query(classes[clas]).all()
                for value in user_obj:
                    key = value.__class__.__name__ + '.' + value.id
                    dictionary[key] = value
        else:
            user_obj = self.__session.query(cls).all()
            print(user_obj)
            for value in user_obj:
                key = value.__class__.__name__ + '.' + value.id
                dictionary[key] = value
        return dictionary

    def save(self):
        """ TBC """
        self.__session.commit()

    def new(self, obj):
        """ TBC """
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        """ TBC """
        self.__session.delete(obj)
        self.save()

    def close(self):
        self.__session.close()

    def reload(self):
        """ TBC """
        from models.base_model import Base
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
