#!/usr/bin/python3
""" """
# KASPER edited at 9:28 pm
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.state import State
from models.city import City
from models.user import User


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home")
        self.assertEqual(type(new_place.city_id), str)

    def test_user_id(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home")
        self.assertEqual(type(new_place.user_id), str)

    def test_name(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home")
        self.assertEqual(type(new_place.name), str)

    def test_description(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user,
                          name="home", description="a building")
        self.assertEqual(type(new_place.description), str)

    def test_number_rooms(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home",
                          number_rooms=1)
        self.assertEqual(type(new_place.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user,
                          name="home", number_bathrooms=1)
        self.assertEqual(type(new_place.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user,
                          name="home", max_guest=2)
        self.assertEqual(type(new_place.max_guest), int)

    def test_price_by_night(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home",
                          price_by_night=60)
        self.assertEqual(type(new_place.price_by_night), int)

    def test_latitude(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home",
                          latitude=4.13)
        self.assertEqual(type(new_place.latitude), float)

    def test_longitude(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home",
                          longitude=4.13)
        self.assertEqual(type(new_place.longitude), float)

    def test_amenity_ids(self):
        """ """
        new_state = State(name="Oklahoma")
        id_state = new_state.id
        new_city = City(name="Tulsa", state_id=id_state)
        id_city = new_city.id
        new_user = User(nme="Kasper")
        id_user = new_user.id
        new_place = Place(city_id=id_city, user_id=id_user, name="home")
        self.assertEqual(type(new_place.amenity_ids), list)
