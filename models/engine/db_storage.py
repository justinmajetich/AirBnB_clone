#!/usr/bin/python3
""" engine DBStorage """
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base



class DBStorage:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    """ Manage storage in bd """
    __engine = None
    __session = None

    def __init__(self):
        """ init engine ro sqlalchemist """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(os.environ["HBNB_MYSQL_USER"], os.environ["HBNB_MYSQL_PWD"],
                           os.environ["HBNB_MYSQL_HOST"], os.environ["HBNB_MYSQL_DB"],
                           pool_pre_ping=True))
        
        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        if os.environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)
        print("###################-------############")
        Base.metadata.create_all(self.__engine)
        print("###################-------############")
        
    
    def all(self, cls=None):
        """ call all """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if cls is not None:
            query = self.__session.query(State)
            return (query)
        else:
            classes = [User, State, City, Amenity, Place, Review]
            repuesta = {}
            for clas in classes:
                query = self.__session.query(clas)
                respuesta.update[query]
            return (query)
        
    
    
    def new(self, obj):
        # from models.state import State
        # Base.metadata.create_all(self.__engine)
        # classes = {'BaseModel':BaseModel}
        # atributes = {}
        # for key, val in obj.to_dict().items():
        #     # if key is not '__class__':
        #         atributes.update({key:val})
        # new = State(**atributes)
        print(obj)
       
        self.__session.add(obj)
        self.__session.commit
        
    def save(self):
        self.__session.commit

    def delete(self, obj=None):
        pass

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False )
        Session = scoped_session(session_factory)
        self.__session = Session()
        


