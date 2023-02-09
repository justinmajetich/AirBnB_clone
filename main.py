#!/usr/bin/env python3

from models.state import State, City

s1 = State()
s1ID = s1.id
s1.save()

s2 = State()
s2ID = s2.id
s2.save()

c1 = City()
c1.name = "Ikeja"
c1.state_id = s1ID
c1.save()

c2 = City()
c2.name = "Ajah"
c2.state_id = s1ID
c2.save()

c3 = City()
c3.name = "Okigwe"
c3.state_id = s2ID
c3.save()
