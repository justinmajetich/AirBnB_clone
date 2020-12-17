#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

class DBStorage:
	"""Database Storage Class"""
	__engine = None
	__session = None

	def __init__(self):
		