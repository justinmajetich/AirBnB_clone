#!/usr/bin/python3
"""
Unittest for the Class "State"
"""

import unittest
import time
import datetime
import models
from models.state import State


class Test_state_attr(unittest.TestCase):
    """This class defines unittests for the different attributes both inherited
    and unique for the State Class"""

    def test_uniq_time(self):
        """This function tests for the uniquenss of time creation"""
        state1 = State()
        time.sleep(0.001)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_uniq_id(self):
        """This function tests for the uniqueness of the id"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_custom_id(self):
        """This function creates a State with a specific ID"""
        state = State()
        state.id = "123456"
        self.assertEqual(state.id, "123456")

    def test_type_id(self):
        """This function tests the type of id attr"""
        self.assertIs(type(State().id), str)

    def test_type_created_at(self):
        """This function tests the type of created_at attr"""
        self.assertIs(type(State().created_at), datetime.datetime)

    def test_type_updated_at(self):
        """This function tests for the type of updated_at attr"""
        self.assertIs(type(State().updated_at), datetime.datetime)

    def test_type_name(self):
        """This function tests the type of name attr"""
        self.assertIs(type(State().name), str)

    def test_obj_storage(self):
        """This function tests that an object is automatically saved in
        the ___objects attr of storage instance"""
        state = State()
        self.assertIn(state, models.storage.all().values())

    def test_type_class(self):
        """This function tests the type of an instance created"""
        self.assertIs(type(State()), State)

    def test_str(self):
        """This funtion tests string representation of a BaseModel"""
        state = State()
        state.id = "123456"
        tdy = datetime.datetime.today()
        state.created_at = state.updated_at = tdy
        self.assertIn("[State] (123456)", state.__str__())
        self.assertIn("'id': '123456'", state.__str__())
        self.assertIn("'created_at': " + repr(tdy), state.__str__())
        self.assertIn("'updated_at': " + repr(tdy), state.__str__())


class Test_instantation(unittest.TestCase):
    """This class tests the instantation of a State class"""

    def test_init_kwargs(self):
        """This function create a State with kwargs"""
        tdy = datetime.datetime.today()
        state = State(id="123456", created_at=tdy.isoformat(),
                      updated_at=tdy.isoformat(), name="texas")
        self.assertEqual(state.id, "123456")
        self.assertEqual(state.created_at, tdy)
        self.assertEqual(state.updated_at, tdy)
        self.assertEqual(state.name, "texas")

    def test_init_args(self):
        """This function creates a State without args"""
        tdy = datetime.datetime.today()
        state = State("7890", id="4567", created_at=tdy.isoformat(),
                      updated_at=tdy.isoformat())
        self.assertEqual(state.id, "4567")
        self.assertEqual(state.created_at, tdy)
        self.assertEqual(state.updated_at, tdy)

    def teat_init_class(self):
        """This function tests giving args a class key"""
        state1 = State()
        dict_state1 = state1.to_dict()
        dict_state1['__class__'] = "BaseModel"
        state2 = State(**dict_state1)
        dict_state2 = state2.to_dict()
        self.assertEqual(dict_state2['__class__'], "State")


class Test_save(unittest.TestCase):
    """This class tests the instance method save(self)"""

    def test_save(self):
        """This function tests updating the time"""
        state = State()
        old_time = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, old_time)

    def test_two_save(self):
        """This function tests updates the time twice"""
        state = State()
        first_time = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, first_time)
        second_time = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, second_time)

    def test_save_args(self):
        """This function give save method an argument"""
        with self.assertRaises(TypeError):
            State().save("arg")

    def test_save_file(self):
        """This function tests saving into a JSOM file"""
        state = State()
        state.save()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as f:
            self.assertIn("State." + state.id, f.read())


class Test_to_dict(unittest.TestCase):
    """unittests for the instance method to_dict"""

    def test_type_dict(self):
        """This function tests the type of to_dict return value"""
        self.assertIs(type(State().to_dict()), dict)

    def test_contents_dict(self):
        """This function tests the contents of a dictionary"""
        state = State()
        self.assertIn('updated_at', state.to_dict())
        self.assertIn('__class__', state.to_dict())
        self.assertIn('id', state.to_dict())
        self.assertIn('created_at', state.to_dict())

    def test_dynamic_dict(self):
        """This function tests the dynamic creation of attributes in dict"""
        state = State()
        state.country = "US"
        state.postal_code = 456
        self.assertIn('country', state.to_dict())
        self.assertIn('postal_code', state.to_dict())

    def test_type_time_in_dict(self):
        """This function tests the type of created_at and updated_at in dict"""
        state = State()
        state_dict = state.to_dict()
        self.assertIs(type(state_dict['created_at']), str)
        self.assertIs(type(state_dict['updated_at']), str)

    def test_dict_kwargs(self):
        """This function create a User with kwargs and tests its dict"""
        tdy = datetime.datetime.today()
        state = State(id="123456", created_at=tdy.isoformat(),
                      updated_at=tdy.isoformat(), name="florida")
        state_dict = state.to_dict()
        self.assertIn('name', state_dict)

    def test_full_dict(self):
        """This function tests creation of a dictionary"""
        state = State()
        state.id = "123456"
        tdy = datetime.datetime.today()
        state.created_at = state.updated_at = tdy
        dict_state = {'__class__': 'State',
                      'updated_at': tdy.isoformat(),
                      'created_at': tdy.isoformat(),
                      'id': "123456"}
        self.assertDictEqual(state.to_dict(), dict_state)

    def test_dict_class(self):
        """This function tests that __dict__ repr and to_dict()
        are different"""
        state = State()
        self.assertNotEqual(state.__dict__, state.to_dict())

    def test_to_dict_arg(self):
        """This function tests giving the instance method to_dict arguments"""
        with self.assertRaises(TypeError):
            State().to_dict("arg")


if __name__ == '__main__':
    unittest.main()
