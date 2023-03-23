#!/usr/bin/python2
"""
This is the test module for `console`
"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage, storage_type
import unittest
from unittest.mock import patch
from io import StringIO
import os
import tempfile
from tests import reset_stream
import MySQLdb
import sqlalchemy
from models.user import User


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

    @unittest.skipIf(storage_type == "db", "File Storage specific")
    def test_create_string(self):
        """Test string parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all City")
            all = fd.getvalue().strip()
            self.assertNotIn("name", all)
            self.assertNotIn("New York", all)
            reset_stream(fd)

            HBNBCommand().onecmd("create City name=\"New_York\"")
            uid = fd.getvalue().strip()
            reset_stream(fd)

            HBNBCommand().onecmd("show City {}".format(uid))
            instance = fd.getvalue().strip()
            self.assertIn(uid, instance)
            self.assertIn("City", instance)
            self.assertIn("name", instance)
            self.assertIn("New York", instance)
            reset_stream(fd)

            HBNBCommand().onecmd("all City")
            all = fd.getvalue().strip()
            self.assertIn("New York", all)
            reset_stream(fd)
            fd.close()

    @unittest.skipIf(storage_type == "db", "File Storage specific")
    def test_create_float(self):
        """Test float parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Place")
            all = fd.getvalue().strip()
            self.assertNotIn("longitude", all)
            self.assertNotIn("-132.505", all)
            reset_stream(fd)

            HBNBCommand().onecmd("create Place longitude=-132.505")
            uid = fd.getvalue().strip()
            reset_stream(fd)

            HBNBCommand().onecmd("all Place")
            all = fd.getvalue().strip()
            self.assertIn("longitude", all)
            reset_stream(fd)

            HBNBCommand().onecmd("show Place {}".format(uid))
            instance = fd.getvalue().strip()
            self.assertIn(uid, instance)
            self.assertIn("Place", instance)
            self.assertIn("longitude", instance)
            self.assertIn("-132.505", instance)
            reset_stream(fd)
            fd.close()

    @unittest.skipIf(storage_type == "db", "File Storage specific")
    def test_create_int(self):
        """Test integer parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Place")
            all = fd.getvalue().strip()
            self.assertNotIn("number_rooms", all)
            self.assertNotIn("1", all)
            reset_stream(fd)

            HBNBCommand().onecmd("create Place number_rooms=1")
            uid = fd.getvalue().strip()
            reset_stream(fd)

            HBNBCommand().onecmd("all Place")
            all = fd.getvalue().strip()
            self.assertIn("number_rooms", all)
            reset_stream(fd)

            HBNBCommand().onecmd("show Place {}".format(uid))
            instance = fd.getvalue().strip()
            self.assertIn(uid, instance)
            self.assertIn("Place", instance)
            self.assertIn("number_rooms", instance)
            self.assertIn("1", instance)
            reset_stream(fd)
            fd.close()

    @unittest.skipIf(storage_type == "db", "File Storage specific")
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
            all = fd.getvalue().strip()

            for item in items:
                self.assertNotIn(item, all)
            reset_stream(fd)

            HBNBCommand().onecmd(
                "create {} {}=\"{}\" {}={}".format(
                    self.classname, self.text_key, self.text_val,
                    self.user_id_key, self.user_id_val))

            uid = fd.getvalue().strip()
            items.append(uid)
            reset_stream(fd)

            HBNBCommand().onecmd("all Review")
            all = fd.getvalue().strip()

            for item in items:
                if item == self.text_val:
                    item = item.replace("_", " ")
                self.assertIn(item, all)
            reset_stream(fd)

            HBNBCommand().onecmd("show {} {}".format(self.classname, uid))

            instance = fd.getvalue().strip()
            for item in items:
                if item == self.text_val:
                    item = item.replace("_", " ")
                self.assertIn(item, instance)
            reset_stream(fd)
            fd.close()

    @unittest.skipIf(storage_type == "db", "File Storage specific")
    def test_create_invalid_param(self):
        """Test invalid parameter"""
        with patch(('sys.stdout'), new=StringIO()) as fd:
            HBNBCommand().onecmd("all Amenity")
            all = fd.getvalue().strip()
            self.assertNotIn("right_key", all)
            self.assertNotIn("right_value", all)
            reset_stream(fd)

            HBNBCommand().onecmd("create Amenity right_key=\"right_value\"")
            uid = fd.getvalue().strip()
            reset_stream(fd)

            HBNBCommand().onecmd("all Amenity")
            all = fd.getvalue().strip()
            self.assertIn("right_key", all)
            reset_stream(fd)

            HBNBCommand().onecmd("show Amenity {}".format(uid))
            instance = fd.getvalue().strip()
            self.assertIn(uid, instance)
            self.assertIn("Amenity", instance)
            self.assertIn("right_key", instance)
            self.assertIn("right value", instance)
            reset_stream(fd)

            HBNBCommand().onecmd("all Amenity")
            all = fd.getvalue().strip()
            self.assertNotIn("invalid_key", all)
            self.assertNotIn("13\"invalid", all)
            reset_stream(fd)

            HBNBCommand().onecmd("create Amenity invalid_key=13\"invalid")
            uid = fd.getvalue().strip()
            reset_stream(fd)

            HBNBCommand().onecmd("all Amenity")
            all = fd.getvalue().strip()
            self.assertNotIn("invalid_key", all)
            reset_stream(fd)

            HBNBCommand().onecmd("show Amenity {}".format(uid))
            instance = fd.getvalue().strip()
            self.assertIn(uid, instance)
            self.assertIn("Amenity", instance)
            self.assertNotIn("invalid_key", instance)
            self.assertNotIn("right value", instance)
            reset_stream(fd)
            fd.close()

    @unittest.skipIf(storage_type != "db", "Test create cmd in database")
    def test_create_db_storage(self):
        """Test create command when running database engine
        """

        with patch('sys.stdout', new=StringIO()) as fd:
            console = HBNBCommand()
            console.onecmd(
                'create User email="ecokeke21@gmail.com" password="ovy"')
            uid = fd.getvalue().strip()

            connection = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(uid))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn("ecokeke21@gmail.com", result)
            self.assertIn("ovy", result)
            cursor.close()
            connection.close()

            with self.assertRaises(sqlalchemy.exc.OperationalError):
                console.onecmd('create User')
            reset_stream(fd)
            fd.close()

    @unittest.skipIf(storage_type != "db", "Test create cmd in database")
    def test_db_show(self):
        """Tests the show command with the database storage.
        """
        with patch('sys.stdout', new=StringIO()) as fd:
            console = HBNBCommand()
            obj = User(email="ecokeke21@gmail.com", password="ovy")
            connection = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = connection.cursor()

            # before calling save method
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(obj.id))
            result = cursor.fetchone()
            self.assertTrue(result is None)

            console.onecmd('show User {}'.format(obj.id))
            self.assertEqual(fd.getvalue().strip(), '** no instance found **')
            obj.save()

            connection = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(obj.id))
            reset_stream(fd)

            console.onecmd('show User {}'.format(obj.id))
            result = cursor.fetchone()
            self.assertTrue(result is not None)
            self.assertIn("ecokeke21@gmail.com", result)
            self.assertIn("ovy", result)
            self.assertIn("ecokeke21@gmail.com", fd.getvalue())
            self.assertIn("ovy", fd.getvalue())

            reset_stream(fd)
            fd.close()
            cursor.close()
            connection.close()

    @unittest.skipIf(storage_type != "db", "Test create cmd in database")
    def test_count_db_storage(self):
        """Tests the count command with the database storage.
        """

        with patch('sys.stdout', new=StringIO()) as fd:
            console = HBNBCommand()
            connection = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )

            cursor = connection.cursor()
            cursor.execute('SELECT COUNT(*) FROM states')
            prev_count = int(cursor.fetchone()[0])

            console.onecmd('create State name="Imo"')
            reset_stream(fd)

            console.onecmd('count State')
            new_count = fd.getvalue().strip()
            self.assertEqual(int(new_count), prev_count + 1)
            reset_stream(fd)

            fd.close()
            cursor.close()
            connection.close()
