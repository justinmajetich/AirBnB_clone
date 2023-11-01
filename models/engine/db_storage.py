from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Represents a db storage engine
    Attributes:
    __engine: working engine
    __session: working session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of dbstorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects on the current database session
        Return: returns dictionary
        """
        objdict = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for object in query:
                objkey = "{}.{}".format(type(object).__name__, object.id)
                objdict[objkey] = object
        else:
            objtypes = [User, State, City, Amenity, Place, Review]
            for objects in objtypes:
                query = self.__session.query(objects)
                for object in query:
                    objkey = "{}.{}".format(type(object).__name__, object.id)
                    objdict[objkey] = object
        return (objdict)

    def new(self, obj):
        """add object to curent db"""
        self.__session.add(obj)

    def save(self):
        """commit changes to current db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates tables and sessions in the db"""
        Base.metadata.create_all(self.__engine)
        sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessions)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
