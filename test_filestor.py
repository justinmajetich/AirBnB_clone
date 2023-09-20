#!/usr/bin/python3
from models.state import State
from models.city import City

new_state = State()
new_state.name = 'orizona'
city1 = City()
city1.name = 'Elksar El kabir'
city2 = City()
city3 = City()
city3.name = 'tanger'
city4 = City()
city4.name = 'Massa'
city5 = City(name="sssssss")

city1.state_id = new_state.id
city4.state_id = new_state.id
list_cities = new_state.cities

for city in list_cities:
    print(city)
