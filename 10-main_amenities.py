#!/usr/bin/python3
from models import *
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity

s = State(name="California")
s.save()
c = City(state_id=s.id, name="San Francisco")
c.save()

u = User(email="a@a.com", password="pwd")
u.save()

p1 = Place(user_id=u.id, city_id=c.id, name="House 1")
p1.save()
p2 = Place(user_id=u.id, city_id=c.id, name="House 2")
p2.save()

a1 = Amenity(name="Wifi")
a1.save()
a2 = Amenity(name="Cable")
a2.save()
a3 = Amenity(name="Eth")
a3.save()

p1.amenities.append(a1)
p1.amenities.append(a2)

p2.amenities.append(a1)
p2.amenities.append(a2)
p2.amenities.append(a3)

storage.save()
