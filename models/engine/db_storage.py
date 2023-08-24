#!/usr/bin/python3
""" module define New engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os


class DBStorage:
    """
    Intialise Class that represents DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Public instance method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Method to retrieve all objects"""
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import BaseModel
        from models.place import Place

        clas = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review}
        if cls:
            new_d = {}
            allC_obj = self.__session.query(cls).all()
            for o in allC_obj:
                k = type(o).__name__ + "." + o.id
                new_d[key] = o
            return (new_d)
        else:
            all_d = {}
            dic_l = []
            State = self.all('State')
            City = self.all('City')
            dic_l.append(State)
            dic_l.append(City)
            for d in dic_l:
                all_d.update(d)
            return(all_d)

    def new(self, obj):
        """add ibjet to db"""
        self.__session.add(obj)

    def save(self):
        """
        commit change of database"""
        self.__session.commit()

    def delete(self, obj=None):
        """method the delete from db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reloandig database"""
        Base.metadata.create_all(self.__engine)
        ss_f = sessionmaker(bind=self.__engine,
                            expire_on_commit=False)
        Session = scoped_session(ss_f)
        self.__session = Session()

    def close(self):
        """
        Method close session"""
        self.__session.close()
