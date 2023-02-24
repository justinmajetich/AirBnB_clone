#!/usr/bin/python3
"""This module defines a class to manage DataBase storage for hbnb clone"""
import sys
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy.orm import sessionmaker

class DBStorage:
	"""Databse engine class"""
	__engine = None
	__session = None

	def __init__(self):
		"""Constructor of DBclass"""
		user = getenv('HBNB_MYSQL_USER')
		pwd = getenv('HBNB_MYSQL_PWD')
		host = getenv('HBNB_MYSQL_HOST')
		data_base = getenv('HBNB_MYSQL_DB')
		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
									  .format(user, pwd, host,
									  data_base), pool_pre_ping=True)

		if getenv('HBNB_ENV') == 'test':
			Base.metadata.drop_all(self.__engine)

		Session = sessionmaker(bind=self.__engine)
		self.__session = Session()

	def all(self, cls=None):
		"""Method to get all objects from database by class"""
		all_obj = {}
		if cls is None:			
			all_obj = self.__session.query(State, City, Place,
										   User, Amenity, Review).all()
			return all_obj
		else:
			all_obj = self.__session.query(cls).all()
			return all_obj

	def new(self, obj):
		"""Adds new object to storage dictionary"""
		self.__session.add()

	def save(self):
		"""Saves storage dictionary to file"""
		self.__session.add(self)
		self.__session.commit()
		self.__session.close()

	def delete(self, obj=None):
		"""delete obj from dbstorage"""
		if obj is not None:
			self.__session.delete(obj)
			self.__session.commit()	
		self.__session.close()

	def reload(self):
		"""Loads storage dictionary from database"""