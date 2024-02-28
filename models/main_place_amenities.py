#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *


state = State(name="California")
state.save()

city = City(state_id=state.id, name="San Francisco")
city.save()

user = User(email="john@snow.com", password="johnpwd")
user.save()

place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
