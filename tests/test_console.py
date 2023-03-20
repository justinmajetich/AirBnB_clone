#!/usr/bin/python2
"""
This is the test module for `console`
"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from unittest.mock import patch
from io import StringIO
import os
import tempfile


class TestConsole(unittest.TestCase):
    """This is the test class for HBNBCommand"""

    @classmethod
    def setUpClass(cls):
        """Set up temporary file to use as file storage database"""
        cls.original_file_path = FileStorage._FileStorage__file_path
        cls.tmp = tempfile.NamedTemporaryFile(suffix=".json")
        cls.tmp.close()
        cls.tmp_path = cls.tmp.name
        setattr(FileStorage, "_FileStorage__file_path", cls.tmp_path)
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Reset the file storage path to original file"""
        setattr(FileStorage, "_FileStorage__file_path", cls.original_file_path)
        storage.reload()

        # delete temporary file
        if os.path.isfile(cls.tmp_path):
            os.remove(cls.tmp_path)

    def setUp(self):
        """delete temporary file if exists and reset objects dict"""
        if os.path.isfile(self.tmp_path):
            os.remove(self.tmp_path)

        FileStorage._FileStorage__objects = {}

    def test_create_string(self):
        """Test string parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all City")
        all = fd.getvalue()[:-1]
        self.assertNotIn("name", all)
        self.assertNotIn("New York", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("create City name=\"New_York\"")
        uid = fd.getvalue()[:-1]

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("show City {}".format(uid))
        instance = fd.getvalue()[:-1]
        self.assertIn(uid, instance)
        self.assertIn("City", instance)
        self.assertIn("name", instance)
        self.assertIn("New York", instance)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all City")
        all = fd.getvalue()[:-1]
        self.assertIn("New York", all)

    def test_create_float(self):
        """Test float parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Place")
        all = fd.getvalue()[:-1]
        self.assertNotIn("longitude", all)
        self.assertNotIn("-132.505", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("create Place longitude=-132.505")
        uid = fd.getvalue()[:-1]

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Place")
        all = fd.getvalue()[:-1]
        self.assertIn("longitude", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("show Place {}".format(uid))
        instance = fd.getvalue()[:-1]
        self.assertIn(uid, instance)
        self.assertIn("Place", instance)
        self.assertIn("longitude", instance)
        self.assertIn("-132.505", instance)

    def test_create_int(self):
        """Test integer parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Place")
        all = fd.getvalue()[:-1]
        self.assertNotIn("number_rooms", all)
        self.assertNotIn("1", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("create Place number_rooms=1")
        uid = fd.getvalue()[:-1]

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Place")
        all = fd.getvalue()[:-1]
        self.assertIn("number_rooms", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("show Place {}".format(uid))
        instance = fd.getvalue()[:-1]
        self.assertIn(uid, instance)
        self.assertIn("Place", instance)
        self.assertIn("number_rooms", instance)
        self.assertIn("1", instance)

    def test_multiple_params(self):
        """Test setting multiple parameters on creation"""

        self.classname = "Review"
        self.text_key = "text"
        self.text_val = "Great_location"
        self.user_id_key = "user_id"
        self.user_id_val = "1234"

        items = [self.classname, self.text_key,
                 self.text_val, self.user_id_key, self.user_id_val]

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all {}".format(self.classname))
        all = fd.getvalue()[:-1]

        for item in items:
            self.assertNotIn(item, all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd(
                "create {} {}=\"{}\" {}={}".format(
                    self.classname, self.text_key, self.text_val,
                    self.user_id_key, self.user_id_val))

        uid = fd.getvalue()[:-1]
        items.append(uid)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Review")
        all = fd.getvalue()[:-1]

        for item in items:
            if item == self.text_val:
                item = item.replace("_", " ")
            self.assertIn(item, all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("show {} {}".format(self.classname, uid))

        instance = fd.getvalue()[:-1]
        for item in items:
            if item == self.text_val:
                item = item.replace("_", " ")
            self.assertIn(item, instance)

    def test_create_invalid_param(self):
        """Test invalid parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Amenity")
        all = fd.getvalue()[:-1]
        self.assertNotIn("right_key", all)
        self.assertNotIn("right_value", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("create Amenity right_key=\"right_value\"")
        uid = fd.getvalue()[:-1]

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Amenity")
        all = fd.getvalue()[:-1]
        self.assertIn("right_key", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("show Amenity {}".format(uid))
        instance = fd.getvalue()[:-1]
        self.assertIn(uid, instance)
        self.assertIn("Amenity", instance)
        self.assertIn("right_key", instance)
        self.assertIn("right value", instance)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Amenity")
        all = fd.getvalue()[:-1]
        self.assertNotIn("invalid_key", all)
        self.assertNotIn("13\"invalid", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("create Amenity invalid_key=13\"invalid")
        uid = fd.getvalue()[:-1]

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Amenity")
        all = fd.getvalue()[:-1]
        self.assertNotIn("invalid_key", all)

        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("show Amenity {}".format(uid))
        instance = fd.getvalue()[:-1]
        self.assertIn(uid, instance)
        self.assertIn("Amenity", instance)
        self.assertNotIn("invalid_key", instance)
        self.assertNotIn("right value", instance)
