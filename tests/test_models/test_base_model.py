#!/usr/bin/python3
""" Test BaseModel """

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ Tests for basemodel class """

    def test_noarguments(self):
        """ Test to prove the basemodel with no arguments """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_baseid(self):
        """ Test with only the id """
        self.assertEqual(str, type(BaseModel().id))

    def test_basecreated(self):
        """ Test of created at variable """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_baseupdated(self):
        """ Test of updated at variable with correct datetime """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_basedict(self):
        """ Test of the function to dict method """
        tester = BaseModel()
        self.assertTrue(dict, type(tester.to_dict()))

    def test_basedict2(self):
        """ Test to know if the attributes are on the dict """
        tester = BaseModel()
        self.assertIn("id", tester.to_dict())
        self.assertIn("created_at", tester.to_dict())
        self.assertIn("updated_at", tester.to_dict())

    def test_baseid_different(self):
        """ Test to prove if the class create 2 different ids"""
        test1 = BaseModel()
        test2 = BaseModel()
        self.assertNotEqual(test1.id, test2, id)

    def test_basedif_times(self):
        """ Test for different times of creation """
        test1 = BaseModel()
        sleep(0.5)
        test2 = BaseModel()
        self.assertNotEqual(test1.created_at, test2.created_at)
        self.assertNotEqual(test1.updated_at, test2.updated_at)

    def test_basesave(self):
        """ Test for save """
        test1 = BaseModel()
        updt = test1.updated_at
        sleep(0.5)
        test1.save()
        self.assertNotEqual(test1.updated_at, updt)

    def test_basestr(self):
        """ Test for str method """
        date1 = datetime.today()
        test1 = BaseModel()
        test1.id = 712456769374
        test1.created_at = date1
        test1.updated_at = date1
        testerstr = test1.__str__()
        self.assertIn("[BaseModel] (712456769374)", testerstr)
        self.assertIn("'id': 712456769374", testerstr)
        self.assertIn("'created_at': " + repr(date1), testerstr)
        self.assertIn("'updated_at': " + repr(date1), testerstr)
