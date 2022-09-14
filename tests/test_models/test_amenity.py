#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amenity = Amenity(name="wifi")

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_creation(self):
        """ Test Amenity class instance creation"""
        amenity = self.value(id="001", name="wifi")
        self.assertEqual(amenity.name, "wifi")
        self.assertEqual(amenity.id, "001")

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_no_name(self):
        """ Check for mandatory arguments"""
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_amenity_instance(self):
        """ Check that amenity is an instance of Amenity class"""
        amenity = self.value()
        self.assertTrue(isinstance(amenity, Amenity))
