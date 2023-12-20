import os
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Query, session, sessionmaker
from sqlalchemy.orm.scoping import scoped_session


HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
HBNB_ENV = os.getenv("HBNB_ENV")


class DBStorage:
    __engine = None
    __session = None
    __accepted_models = {}

    def __init__(self):
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB,
        )
        self.__engine = create_engine(db_url, pool_pre_ping=True, echo=False)

        meta = MetaData()
        if HBNB_ENV == "test":
            meta.drop_all(
                self.__engine,
            )

    def all(self, cls=None):
        if cls is None:
            q_result = {
                "{}.{}".format(model.__class__.__name__, model.id): model
                for model in self.__session.query(
                    *list(self.__accepted_models.values())
                ).all()
            }
            return q_result

        return {
            "{}.{}".format(model.__class__.__name__, model.id): model
            for model in self.__session.query(
                self.__accepted_models[cls],
            ).all()
        }

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        pass

    def reload(self):
        from models.base_model import Base
        from models import user, state, city, amenity, place, review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        )
        self.__accepted_models = {
            "State": state.State,
            "City": city.City,
            # "User": user.User,
            # "Place": place.Place,
            # "Amenity": amenity.Amenity,
            # "Review": review.Review,
        }
        self.__session = scoped_session(session_factory)()
