from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from base_model import Base
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )

    def all(self, cls=None):
        from models import classes

        objects = {}
        if cls:
            query = self.__session.query(classes[cls]).all()
            for obj in query:
                key = f'{obj.__class__.__name__}.{obj.id}'
                objects[key] = obj
        else:
            for cls in classes.values():
                query = self.__session.query(cls).all()
                for obj in query:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objects[key] = obj

        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
