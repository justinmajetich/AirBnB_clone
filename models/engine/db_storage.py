"""
DB Storage
"""
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    """
    mysql database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            f'mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}',
            pool_pre_ping=True)

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query all objs or all objs of a certain class
        """
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        _classes = {"City": City, "State": State, "Amenity": Amenity,
                    "User": User, "Review": Review, "Place": Place}

        new_dict = {}
        for clss in _classes:
            if cls is None or cls is _classes[clss] or cls is clss:
                objs = self.__session.query(_classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        adding new obj to the current session
        """
        self.__session.add(obj)

    def save(self):
        """
        saving the current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.remove(obj)

    def reload(self):
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(fact)
        self.__session = Session()
