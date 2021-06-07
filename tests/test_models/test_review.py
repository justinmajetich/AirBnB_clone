#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.place import Place
from models.user import User

newU = User(email="john69@hotmail.com", password="4201337",
           first_name="John", last_name="Hancock")
newP = Place(city_id=new_C.id, user_id=new_U.id, name='KFC',
            description='Fried', number_rooms=2,
            number_bathrooms=1, max_guest=30,
            price_by_night=5, latitude=1.2, logitude=3.4)
new = Review(place_id=newU.id, user_id=User().id, text='bla')


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
