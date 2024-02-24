from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}?charset=utf8mb4",
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)()

    def all(self, cls=None):
        if cls:
            return {str(cls.__name__) + '.' + str(obj.id): obj for obj in self.__session.query(cls).all()}
        else:
            return {str(cls.__name__) + '.' + str(obj.id): obj for cls in Base._decl_class_registry.values() for obj in self.__session.query(cls).all()}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
        self.__session.commit()

    def reload(self):
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)()
