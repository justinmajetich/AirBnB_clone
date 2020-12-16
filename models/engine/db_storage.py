from sqlalchemy import create_engine
from sqlalchemy import *


class DBStorage:
    """ DB_Storage """
    __engine = None
    __session = None

    def __init__(self):

        """init 
        user is the SQL User
        Password is the SQL Password
        host is the host
        db is the database
        """

        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, password, host, db),
                                      pool_pre_ping=True
    
     Base.metadata.create_all(self.__engine)
     if os.getenv("HBNB_ENV") = test:
        Base.metadata.drop_all(self.__engine)

        def new(self, obj):
            """ add the object to the current database session"""
            self.__session.add(obj)
        
        def save(self):
            """ commit all changes of the current database session """
            self.__session.save()
        
        def delete(self, obj=None):
            """ delete from the current database session """
            self.__session.delete(obj)

        


