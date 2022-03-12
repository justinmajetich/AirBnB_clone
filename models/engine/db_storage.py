#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import json
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
	"""This class manages storage of hbnb models in a database"""
	__engine = None
	__session = None

	classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review
				}

	def __init__(self):
		"""Instantiates a new model"""

		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.\
									format(getenv(HBNB_MYSQL_USER),\
										getenv(HBNB_MYSQL_PWD),\
										getenv(HBNB_MYSQL_HOST),\
										getenv(HBNB_MYSQL_DB),\
										pool_pre_ping=True)
		if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""Returns a dictionary of models currently in storage"""
		if cls:
            objs = self.__session.query(self.classes[cls])
		else:
			objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
		
		dict_objs = {}
		for obj in objs:
			key = '{}.{}'.format(type(obj).__name__, obj.id)
            dict_objs[key] = obj
        return dict_objs


	def new(self, obj):
		"""Adds new object to storage dictionary"""
		self.__session.add(obj)

	def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

	def reload(self):
		"""Loads storage dictionary from file"""

		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		Session = scoped_session(session_factory)
		self.__session = Session()

	def delete(self, obj=None):
		"""Deletes an object from storage dictionary"""
		if obj == None:
			pass
		else: 
			self.__session.delete(obj)

	def close(self):
        """Removes the session"""
        self.__session.close()
