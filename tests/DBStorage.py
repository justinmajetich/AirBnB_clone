#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

# Create the database connection
engine = create_engine('your_database_connection_string')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the State, City, User, and Place models
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', backref='cities')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    number_rooms = Column(Integer)
    number_bathrooms = Column(Integer)
    max_guest = Column(Integer)
    price_by_night = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    city = relationship('City', backref='places')
    user = relationship('User', backref='places')


place_id = place.id
place = session.query(Place).filter_by(id=place_id).first()
if place:
    print(f"Place {place_id} is present")
else:
    print(f"Place {place_id} is not found")
