#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv

db_engine = create_engine('sqlite:///mydatabase.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

Base.metadata.create_all(db_engine)

Session = sessionmaker(bind=db_engine)
session = Session()

new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)
session.commit()

session.close()
