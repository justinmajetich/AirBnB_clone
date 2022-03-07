#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
	"""This class manages storage of hbnb models in a database"""
	__engine = None
	__session = None

	def __init__(self):
		"""Instantiates a new model"""

		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.\
									format(HBNB_MYSQL_PWD,\
										HBNB_MYSQL_USER,\
										HBNB_MYSQL_HOST,\
										HBNB_MYSQL_DB),\
										pool_pre_ping=True)
		
	def all(self, cls=None):
		"""Returns a dictionary of models currently in storage"""
		if cls == None:
			return self.__session
		else:
			for k, v in self.__session.items():
				if cls == k.split(.)[0]:
					return self.__session[k]


	def new(self, obj):
		"""Adds new object to storage dictionary"""
		self.__session.new({obj.to_dict()['__class__'] + '.' + obj.id: obj})
		self.__session.close()


	def save(self):
		"""Saves storage dictionary to file"""
		self.__session.commit()

	def reload(self):
		"""Loads storage dictionary from file"""
		from models.base_model import BaseModel
		from models.user import User
		from models.place import Place
		from models.state import State
		from models.city import City
		from models.amenity import Amenity
		from models.review import Review

		classes = {
					'BaseModel': BaseModel, 'User': User, 'Place': Place,
					'State': State, 'City': City, 'Amenity': Amenity,
					'Review': Review
				  }

		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine, expire_on_commit=False)
		self.__session = Session()

	def delete(self, obj=None):
		"""Deletes an object from storage dictionary"""
		if obj == None:
			pass
		else: 
			self.__session.delete(obj)
