from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = 'localhost'
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
            pool_pre_ping=True
        )
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        all_objects = {}
        if cls is not None:
            select = self.__session.query(cls)
        else:
            select = self.__session.query()
        objects = select.all()
        for objct in objects:
                all_objects["{}.{}"
                            .format(
                                objct.__class__.__name__, objct.id
                                )] = objct
        
        """
        if cls is None:
            for a_class in classes:
                objects = self.__session.query(classes[a_class])
                for objct in objects:
                    key = "{}.{}".format(objct.__class__.__name__, objct.id)
                    all_objects[key] = objct
        else:
            if type(cls) is str:
                cls = eval(cls)()
            objects = self.__session.query(cls)
            for objct in objects:
                key = "{}.{}".format(objct.__class__.__name__, objct.id)
                all_objects[key] = objct
        """

        return all_objects
    
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
