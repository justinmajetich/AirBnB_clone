#!/usr/bin/python3
"""
Test AirBnB console using unittest module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
import os


class TestConsole(unittest.TestCase):
    """
    subclass of TestCase that test the console features
    """
    @classmethod
    def setUpClass(cls):
        """ setUp the class environment
        """
        # if os.getenv("HBNB_TYPE_STORAGE") == "File_Storage":
        pass

    def setUp(self):
        """ setUp the test environment variables
        """
        TestConsole.wraper = StringIO()
        TestConsole.patcher = patch('sys.stdout', new=TestConsole.wraper)
        TestConsole.patcher.start()

    def tearDown(self):
        """ Cleaning after finshing the test
        """
        TestConsole.patcher.stop()
        del TestConsole.patcher
        if os.path.exists("file.json"):
            os.remove("file.json")

    @classmethod
    def tearDownClass(cls):
        """ Clean after finshing the class test
        """
        pass

    def test_create(self):
        """Test do_create(self, args)
        """
        import re
        from console import storage

        cls = "BaseModel"
        id = re.compile(r"\w{8}-(\w{4}-){3}\w{12}")
        HBNBCommand().onecmd("create {}".format(cls))

        result = TestConsole.wraper.getvalue().strip()
        instance = storage.all()["{}.{}".format(cls, result)]
        self.assertRegex(result, id)
        self.assertIsInstance(instance, BaseModel)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No test on DB")
    def test_create_with_params(self):
        """ Test do_create(self, args) with parameters
        """
        from models.place import Place
        from console import storage

        cls = "Place"
        command = f"create {cls} latitude=7.50 longitude=5.25 max_guest=4"
        command += ' name="My_Hidden_Garden"'
        HBNBCommand().onecmd(command)
        id = TestConsole.wraper.getvalue().strip()

        self.assertRegex(id, r"\w{8}-(\w{4}-){3}\w{12}")
        instance = storage.all()["{}.{}".format(cls, id)]

        self.assertEqual(instance.latitude, 7.5)
        self.assertEqual(instance.longitude, 5.25)
        self.assertEqual(instance.max_guest, 4)
        self.assertEqual(instance.name, "My Hidden Garden")

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No test on DB")
    def test_create_with_RightWrong_params(self):
        """ Test do_create(self, args), with one right syntax and
         others wrong syntax parameters
        """
        cls = "Place"
        command = f'create {cls} latitude= 7.50 longitude=5.25 max_guest = 4'
        HBNBCommand().onecmd(command)
        id = TestConsole.wraper.getvalue().strip()

        self.assertRegex(id, r"\w{8}-(\w{4}-){3}\w{12}")
        instance = storage.all()["{}.{}".format(cls, id)]

        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 5.25)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.name, "")

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No test on DB")
    def test_create_with_wrong_params(self):
        """ Test do_create(self, args), with wrong syntax parameters
        """
        cls = "Place"
        command = f'create {cls} latitude= 7.50 longitude="5.25" max_guest = 4'
        HBNBCommand().onecmd(command)
        id = TestConsole.wraper.getvalue().strip()

        self.assertRegex(id, r"\w{8}-(\w{4}-){3}\w{12}")
        instance = storage.all()["{}.{}".format(cls, id)]

        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 0.0)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.name, "")

    def test_create_no_class(self):
        """ Test do_create(self, args), given no class
        """
        HBNBCommand().onecmd("create")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class name missing **")

    def test_create_wrong_class(self):
        """ Test do_create(self, args), given wrong class name
        """
        HBNBCommand().onecmd("create MEEE")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class doesn't exist **")

    @patch('console.storage', **{"save.return_value": None})
    def test_create_call_save(self, storage):
        """ Test do_create(self, args) that call the storage.save()
        """
        HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(storage.save.called)

    def test_show(self):
        """ Test do_show(self, args)
        """
        instance = BaseModel()
        cls = "BaseModel"
        HBNBCommand().onecmd("show {} {}".format(cls, instance.id))
        result = TestConsole.wraper.getvalue().strip()

        self.assertEqual(result, str(instance))

    def test_show_no_class(self):
        """ Test do_show(self, args) with no class
        """
        HBNBCommand().onecmd("show ")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class name missing **")

    def test_show_wrong_class(self):
        """ Test do_show(self, args) with wrong class name
        """
        HBNBCommand().onecmd("show MEEEE")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class doesn't exist **")

    def test_show_no_id(self):
        """ Test do_show(self, args) with no id
        """
        HBNBCommand().onecmd("show BaseModel")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** instance id missing **")

    def test_show_wrong_id(self):
        """ Test do_show(self, args) with wrong id
        """
        HBNBCommand().onecmd("show BaseModel 1234-1234-2468")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** no instance found **")

    def test_destroy(self):
        """ Test do_destroy(self, args)
        """
        from console import storage

        instance = BaseModel()
        cls = "BaseModel"
        id = instance.id
        HBNBCommand().onecmd("destroy {} {}".format(cls, id))
        objects = storage.all()
        self.assertNotIn(instance, objects.values())

    @patch("console.storage.save",
           return_value=None)
    def test_destroy_call_save(self, storage):
        """ Test do_destroy(self, args), call the storage.save()
        """
        instance = BaseModel()
        cls = "BaseModel"
        id = instance.id
        HBNBCommand().onecmd("destroy {} {}".format(cls, id))
        self.assertTrue(storage.called)

    def test_destroy_no_class(self):
        """ Test do_destroy(self, args), with no class name
        """
        HBNBCommand().onecmd("destroy")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class name missing **")

    def test_destroy_wrong_class(self):
        """ Test do_destroy(self, args), with wrong class name
        """
        HBNBCommand().onecmd("destroy NOOOO")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class doesn't exist **")

    def test_destroy_no_id(self):
        """ Test do_destroy(self, args) with no id
        """
        HBNBCommand().onecmd("destroy BaseModel")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** instance id missing **")

    def test_destroy_wrong_id(self):
        """ Test do_destroy(self, args) with wrong id
        """
        HBNBCommand().onecmd("destroy BaseModel 1234-1234-2468")
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** no instance found **")

    def test_all(self):
        """ Test do_all(self, args), without class name
        """

        inst_1 = BaseModel()
        inst_2 = BaseModel()

        inst_2.save()  # save the instances to the json file
        HBNBCommand().onecmd("all")
        result = TestConsole.wraper.getvalue().strip()

        self.assertTrue(type(eval(result)) is list)
        self.assertIn(inst_1.id, result)
        self.assertIn(str(inst_2), result)

    def test_all_with_cls(self):
        """ Test do_all(self, args), with a class name
        """
        from models.user import User

        inst_1 = BaseModel()
        inst_2 = BaseModel()
        inst_3 = User()

        inst_3.save()  # save the instances to the json file
        HBNBCommand().onecmd("all User")
        result = TestConsole.wraper.getvalue().strip()

        self.assertIn(str(inst_3), result)
        self.assertNotIn(str(inst_1), result)

    def test_all_wrong_cls(self):
        """ Test do_all(self, args), with wrong class name
        """
        HBNBCommand().onecmd("all OFMEEE")
        result = TestConsole.wraper.getvalue().strip()

        self.assertEqual(result, "** class doesn't exist **")

    '''
    def test_all_by_class_name(self):
        """ Test do_all(self, args), called by 'cls.all' statement
        """
        instance = BaseModel()
        cls = "BaseModel"
        id = instance.id
        HBNBCommand().onecmd("BaseModel.all()")
        result = TestConsole.wraper.getvalue().strip()

        self.assertTrue(type(eval(result)) is list)
        self.assertIn(instance.id, result)
        self.assertIn(str(instance), result)
    '''
    def test_update(self):
        """ Test do_update(self, args)
        """
        from models.place import Place

        instance = Place()
        id = instance.id
        cls = "Place"
        HBNBCommand().onecmd('update {} {} latitude "4.7"'.format(cls, id))

        self.assertTrue(type(instance.latitude) is float)
        self.assertEqual(instance.latitude, 4.7)

    def test_update_no_class(self):
        """ Test do_update(self, args), with no class name
        """
        HBNBCommand().onecmd('update')
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class name missing **")

    def test_update_wrong_class(self):
        """ Test do_update(self, args), with wrong class name
        """
        HBNBCommand().onecmd('update MEEEE')
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** class doesn't exist **")

    def test_update_no_id(self):
        """ Test do_update(self, args), with no id
        """
        HBNBCommand().onecmd('update BaseModel')
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** instance id missing **")

    def test_update_wrong_id(self):
        """ Test do_update(self, args), with wrong id
        """
        HBNBCommand().onecmd('update BaseModel 1234-1234-2468')
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** no instance found **")

    def test_update_no_attr(self):
        """ Test do_update(self, args), with no attribute
        """
        instance = BaseModel()
        cls = "BaseModel"
        id = instance.id
        instance.save()

        HBNBCommand().onecmd('update {} {}'.format(cls, id))
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** attribute name missing **")

    def test_update_no_value(self):
        """ Test do_update(self, args), with no attribute value
        """
        instance = BaseModel()
        cls = "BaseModel"
        id = instance.id
        instance.save()

        HBNBCommand().onecmd('update {} {} name'.format(cls, id))
        result = TestConsole.wraper.getvalue().strip()
        self.assertEqual(result, "** value missing **")
    '''
    def test_count(self):
        """ Test count(self, args)
        """
        inst_1 = BaseModel()
        inst_2 = BaseModel()

        HBNBCommand().onecmd("BaseModel.count()")
        result = TestConsole.wraper.getvalue().strip()

        self.assertEqual(result, "2")

    def test_count_empty(self):
        """ Test count(self, args), with empty instance class
        """
        HBNBCommand().onecmd("BaseModel.count()")
        result = TestConsole.wraper.getvalue().strip()

        self.assertEqual(result, "0")
    '''
