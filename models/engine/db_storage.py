from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ as env
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine(f"mysql+mysqldb://
                                      {env['HBNB_MYSQL_USER']}:
                                      {env['HBNB_MYSQL_PWD']}@
                                      {env['HBNB_MYSQL_HOST']}/
                                      {env['HBNB_MYSQL_DB']}", 
                                      pool_pre_ping=True)

        if env.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        from models import storage
        classes = [User, State, City, Amenity, Place, Review]
        if cls is not None:
            classes = [cls]
        ret = {}
        for _class in classes:
            for obj in self.__session.query(_class).all():
                key = f"{obj.__class__.__name__}.{obj.id}"
                ret[key] = obj
        return ret

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
