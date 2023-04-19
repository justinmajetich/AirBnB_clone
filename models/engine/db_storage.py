# model classes
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

# tools
from os import getenv

# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in mysql database"""

    __engine = None
    __session = None

    def __init__(self) -> None:
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """returns a dictionary
            Return:
                returns a dictionary of __object
            """
            objc_dictionary = {}
            if cls:
                """Retriving all object of given class """
                if type(cls) is str:
                    cls = eval(cls)
                result_query = self.__session.result_query(cls)
                for elem in result_query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    objc_dictionary[key] = elem
            else:
                """Retriving all known obejcts"""
                obj_list = [State, City, User, Place, Review, Amenity]
                for class_ in obj_list:
                    result_query = self.__session.result_query(class_)
                    for elem in result_query:
                        key = "{}.{}".format(type(elem).__name__, elem.id)
                        objc_dictionary[key] = elem
            return (objc_dictionary)

    def new(self, obj):
        """ adds new object to table
        """
        self.__session.add(obj)

    def save(self):
        """ save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete table object
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """ reloads the engine
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
