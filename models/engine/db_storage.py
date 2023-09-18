#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage(BaseModel):
    """ DBStorage class """
    __engine = None
    __session = None

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    def __init__(self):
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(getenv('HBNB_MYSQL_USER'),
                        getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST', 'localhost'),
                        getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            self.__engine.drop_all()

        def all(self, cls=None):
            from models import base_model

            session = self.__session
            objects = {}

            if cls is None:
                classes = [base_model.State,
                           base_model.City,
                           base_model.User,
                           base_model.Amenity,
                           base_model.Place,
                           base_model.Review]
                for cs in classes:
                    objects.update({obj.id: obj for obj in session.query(cl).all()})
            else:
                objects.update({obj.id: obj for obj in session.query(cls).all()})

            return objects

        def new(self, obj):
            self.__session.add(obj)

        def save(self):
            self.__session.commit()

        def delete(self, obj=None):
            if obj:
                self.__session.delete(obj)

        def reload(self):
            Base.metadata.create_all(self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine,
                                                expire_on_commit=False))
            self.__session = Session()
