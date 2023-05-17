#!/usr/bin/python3
"""Create Database"""
import os
from models.engine.db_storage import DBStorage
from models.base_model import Base
from models.user import User
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review

os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
os.environ['HBNB_TYPE_STORAGE'] = 'db'

# create an instance of the DBStorage class
storage = DBStorage()
storage.reload()

# create all the tables in the database
Base.metadata.create_all(storage._DBStorage__engine)

# add some example data
# state = State(name="California")
# city = City(name="San Francisco", state_id=state.id)
user = User(email="johndoe@example.com", password="password", first_name="Elijah", last_name="Chinedu")
#amenity = Amenity(name="Wifi")
#place = Place(name="Cozy Apartment", description="A small but cozy apartment", number_rooms=1, number_bathrooms=1, max_guest=2, price_by_night=100, latitude=37.7749, longitude=-122.4194, city=city, user=user)
#review = Review(text="Great place!", place=place, user=user)

# add the data to the current database session and save changes
#storage.new(state)
#storage.new(city)
storage.new(user)
#storage.new(amenity)
#storage.new(place)
#storage.new(review)
storage.save()
