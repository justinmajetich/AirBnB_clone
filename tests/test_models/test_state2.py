#!/st/bin/python3
"""Defines unittests for State.py

Unittests classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of class: State"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_new_gets_stored(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_and_str(self):
        self.assertEqual(str, type(State.name))

    def test_two_States_ids_unique(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_two_States_diff_created_at(self):
        st1 = State()
        sleep(0.1)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_two_States_diff_updated_at(self):
        st1 = State()
        sleep(0.1)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_str_value(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        st = State()
        st.id = "66566"
        st.created_at = d_t
        st.updated_at = d_t
        st_str = st.__str__()
        self.assertIn("[State] (66566)", st_str)
        self.assertIn("'id': '66566'", st_str)
        self.assertIn("'created_at': " + d_t_r, st_str)
        self.assertIn("'updated_at': " + d_t_r, st_str)

    def test_arguments_not_used(self):
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            State(id=None, create_at=None, updated_at=None)

class TestState_save(unittest.TestCase):
    """Unittests for save method of class: State"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        st = State()
        sleep(0.1)
        first_update = st.updated_at
        st.save()
        self.assertLess(first_update, st.updated_at)

    def test_two_saves(self):
        st = State()
        sleep(0.1)
        first_update = st.updated_at
        st.save()
        second_update = st.updated_at
        self.assertLess(first_update, second_update)
        sleep(0.1)
        st.save()
        self.assertLess(second_update, st.updated_at)

    def test_save_with_argument(self):
        st = State()
        with self.assertRaises(TypeError):
            st.save(None)

    def test_save_updates_file(self):
        st = State()
        st.save()
        st_id = "State." + st.id
        with open("file.json", "r") as file:
            self.assertIn(st_id, file.read())

class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of class: State"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_keys_accurate(self):
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_containes_added_attr(self):
        st = State()
        st.middle_name = "Ryan"
        st.meaning = 42
        self.assertEqual("Ryan", st.middle_name)
        self.assertIn("meaning", st.to_dict())

    def test_to_dict_datetime_is_str(self):
        st = State()
        st_dict = st.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_out(self):
        d_t = datetime.now()
        st = State()
        st.id = "66566"
        st.created_at = d_t
        st.updated_at = d_t
        temp_dict = {
            'id': '66566',
            '__class__': 'State',
            'created_at': d_t.isoformat(),
            'updated_at': d_t.isoformat()
        }
        self.assertDictEqual(st.to_dict(), temp_dict)

    def test_to_dict_dunder_dict_diff(self):
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

    def test_to_dict_with_argument(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)


if __name__ == "__main__":
    unittest.main()
