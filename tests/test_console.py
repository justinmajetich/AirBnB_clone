#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Unit test for console.py"""
from console import HBNBCommand

from unittest import TestCase, mock
from io import StringIO
import unittest
import cmd
import os
import uuid
import random
import string
import copy
import json
import inspect
import pep8

from models import storage


class TestHBNBCommand(TestCase):
    """Test cases for HBNBCommand class."""

    def setUp(self):
        """Setup for FileStorage tests."""
        storage._FileStorage__objects.clear()

    def tearDown(self):
        """Clean test files."""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instance(self):
        """Test for correct instancing of HBNBCommand object."""
        self.assertIsInstance(HBNBCommand(), HBNBCommand)
        self.assertIsInstance(HBNBCommand(), cmd.Cmd)

    def test_empty_line(self):
        """Test for correct empty line action (empty line + RETURN)."""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue(), "")

    def test_quit_eof(self):
        """Test for correct quit and eof command actions."""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), "")

        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """Test for correct help command output."""
        msg = ("\nDocumented commands (type help <topic>):\n"
               "========================================\n"
               "EOF  all  count  create  destroy  help  quit  show  update"
               "\n\n")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertEqual(f.getvalue(), msg)

    def test_create(self):
        """Test for correct create command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct creation of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
            self.assertIn(class_name + "." + f.getvalue()[:-1], storage.all())
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for key in storage.all().keys():
            self.assertIn(key, json_dict)

    def test_create_missing_class(self):
        exp = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_create_unexisting_class(self):
        exp = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create MyClass")
            real = output.getvalue()
            self.assertEqual(exp, real)

    def test_create(self):
        k_cls = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
        ]

        for c_name in k_cls:
            command = "create " + c_name
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                obj_key = c_name + "." + output.getvalue().strip()
                self.assertIn(obj_key, storage.all().keys())

    def test_show(self):
        """Test for correct show command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show " + rand_class)
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show " + rand_class + " " + rand_id)
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct search of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        for key in storage.all():
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + key[0] + " " + key[1])
            f_class = f.getvalue().split(" ")[0][1:-1]
            f_id = f.getvalue().split(" ")[1][1:-1]
            self.assertIn(f_class + "." + f_id, storage.all())

    def test_dot_show(self):
        """Test for correct show command action with its dot version."""
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show(1234-1234-1234-1234)")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".show()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".show(" + rand_id + ")")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct search of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        for key in storage.all():
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(key[0] + ".show(" + key[1] + ")")
            f_class = f.getvalue().split(" ")[0][1:-1]
            f_id = f.getvalue().split(" ")[1][1:-1]
            self.assertIn(f_class + "." + f_id, storage.all())

    def test_destroy(self):
        """Test for correct destroy command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy " + rand_class)
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy " + rand_class + " " + rand_id)
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct destruction of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        storage_cpy = copy.deepcopy(storage.all())
        for key in storage_cpy:
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy " + key[0] + " " + key[1])
        for key in storage_cpy:
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + key[0] + " " + key[1])
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "{}")

    def test_dot_destroy(self):
        """Test for correct destroy command action with its dot version."""
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.destroy(1234-1234-1234-1234)")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".destroy()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".destroy(" + rand_id + ")")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct destruction of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        storage_cpy = copy.deepcopy(storage.all())
        for key in storage_cpy:
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(key[0] + ".destroy(" + key[1] + ")")
        for key in storage_cpy:
            key = key.split(".")
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + key[0] + " " + key[1])
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "{}")

    def test_all(self):
        """Test for correct all command action."""
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct print of all TYPE when storage.all() is empty
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all " + rand_class)
        self.assertEqual(f.getvalue(), "[]\n")

        # Correct print of all when storage.all() is empty
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertEqual(f.getvalue(), "[]\n")

        # Correct print of all TYPE
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all " + class_name)
            correct_output = "["
            for key, val in storage.all().items():
                if key.split(".")[0] == class_name:
                    correct_output += "\"" + str(val) + "\", "
            correct_output = correct_output[:-2] + "]\n"
            self.assertEqual(f.getvalue(), correct_output)

        # Correct print of all
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        correct_output = "["
        for val in storage.all().values():
            correct_output += "\"" + str(val) + "\", "
        correct_output = correct_output[:-2] + "]\n"
        self.assertEqual(f.getvalue(), correct_output)

    def test_dot_all(self):
        """Test for correct all command action with its dot version."""
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct print of all TYPE when storage.all() is empty
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".all()")
        self.assertEqual(f.getvalue(), "[]\n")

        # Correct print of all TYPE
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_name + ".all()")
            correct_output = "["
            for key, val in storage.all().items():
                if key.split(".")[0] == class_name:
                    correct_output += "\"" + str(val) + "\", "
            correct_output = correct_output[:-2] + "]\n"
            self.assertEqual(f.getvalue(), correct_output)

    def test_update(self):
        """Test for correct update command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + rand_class)
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + rand_class + " " + rand_id)
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct message "** attribute name missing **"
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        rand_key = random.choice(list(storage.all().keys())).split(".")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + rand_key[0] + " " + rand_key[1])
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

        # Correct message "** value missing **"
        attr_dict = {"Amenity": {"name": ""},
                     "City": {"state_id": "", "name": ""},
                     "User":
                     {"email": "", "password": "",
                      "first_name": "", "last_name": ""},
                     "Place":
                     {"city_id": "", "user_id": "",
                      "name": "", "description": "",
                      "number_rooms": 0, "number_bathrooms": 0,
                      "max_guest": 0, "price_by_night": 0,
                      "latitude": 0.0, "longitude": 0.0,
                      "amenity_ids": []},
                     "Review":
                     {"place_id": "", "user_id": "", "text": ""},
                     "State": {"name": ""}}
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.choice(attr)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " + rand_key[0] + " " +
                                 rand_key[1] + " " + rand_attr)
        self.assertEqual(f.getvalue(), "** value missing **\n")

        # Correct ignore of multiple ATTRIBUTE_NAME and ATTRIBUTE_VALUE
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.sample(attr, 2)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        rand_val = []
        for at in rand_attr:
            if type(attr_dict[rand_key[0]][at]) == str:
                rand_val.append(''.join(random.choice(string.ascii_letters)
                                        for _ in range(20)))
            if type(attr_dict[rand_key[0]][at]) == int:
                rand_val.append(random.randint(1, 1000))
            if type(attr_dict[rand_key[0]][at]) == float:
                rand_val.append(random.random() * 10.0)
            if type(attr_dict[rand_key[0]][at]) == list:
                val = []
                for i in range(3):
                    val.append(''.join(random.choice(string.ascii_letters)
                                       for _ in range(20)))
                rand_val.append(val)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " +
                                 rand_key[0] + " " + rand_key[1] + " " +
                                 rand_attr[0] + " " + str(rand_val[0]) + " " +
                                 rand_attr[1] + " " + str(rand_val[1]))
        rand_key = rand_key[0] + "." + rand_key[1]
        self.assertNotIn(rand_attr[1], storage.all()[rand_key].__dict__)
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for attr, val in json_dict[rand_key].items():
            if attr == rand_attr[1]:
                self.assertNotEqual(val, rand_val[1])
                break

        # Correct update of object
        storage._FileStorage__objects.clear()
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.sample(attr, 2)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        rand_attr = random.choice(attr)
        if type(attr_dict[rand_key[0]][rand_attr]) == str:
            rand_val = ''.join(random.choice(string.ascii_letters)
                               for _ in range(20))
        if type(attr_dict[rand_key[0]][rand_attr]) == int:
            rand_val = random.randint(1, 1000)
        if type(attr_dict[rand_key[0]][rand_attr]) == float:
            rand_val = random.random() * 10.0
        if type(attr_dict[rand_key[0]][rand_attr]) == list:
            rand_val = []
            for i in range(3):
                rand_val.append(''.join(random.choice(string.ascii_letters)
                                        for _ in range(20)))
        old_storage = copy.deepcopy(storage.all())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update " +
                                 rand_key[0] + " " + rand_key[1] + " " +
                                 rand_attr + " " + str(rand_val))
        rand_key = rand_key[0] + "." + rand_key[1]
        self.assertNotIn(rand_attr, old_storage[rand_key].__dict__)
        self.assertIn(rand_attr, storage.all()[rand_key].__dict__)
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for attr, val in json_dict[rand_key].items():
            if attr == rand_attr:
                self.assertEqual(str(val), str(rand_val))
                self.assertEqual(val,
                                 storage.all()[rand_key].__dict__[rand_attr])
                self.assertNotIn(attr,
                                 old_storage[rand_key].__dict__)
                break

    def test_dot_update(self):
        """Test for correct update command action with its dot version."""
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.update()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".update()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".update(" + rand_id + ")")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct message "** attribute name missing **"
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        rand_key = random.choice(list(storage.all().keys())).split(".")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_key[0] + ".update(" + rand_key[1] + ")")
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

        # Correct message "** value missing **"
        attr_dict = {"Amenity": {"name": ""},
                     "City": {"state_id": "", "name": ""},
                     "User":
                     {"email": "", "password": "",
                      "first_name": "", "last_name": ""},
                     "Place":
                     {"city_id": "", "user_id": "",
                      "name": "", "description": "",
                      "number_rooms": 0, "number_bathrooms": 0,
                      "max_guest": 0, "price_by_night": 0,
                      "latitude": 0.0, "longitude": 0.0,
                      "amenity_ids": []},
                     "Review":
                     {"place_id": "", "user_id": "", "text": ""},
                     "State": {"name": ""}}
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.choice(attr)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_key[0] + ".update(" +
                                 rand_key[1] + ", " + rand_attr +
                                 ")")
        self.assertEqual(f.getvalue(), "** value missing **\n")

        # Correct ignore of multiple ATTRIBUTE_NAME and ATTRIBUTE_VALUE
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.sample(attr, 2)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        rand_val = []
        for at in rand_attr:
            if type(attr_dict[rand_key[0]][at]) == str:
                rand_val.append(''.join(random.choice(string.ascii_letters)
                                        for _ in range(20)))
            if type(attr_dict[rand_key[0]][at]) == int:
                rand_val.append(random.randint(1, 1000))
            if type(attr_dict[rand_key[0]][at]) == float:
                rand_val.append(random.random() * 10.0)
            if type(attr_dict[rand_key[0]][at]) == list:
                val = []
                for i in range(3):
                    val.append(''.join(random.choice(string.ascii_letters)
                                       for _ in range(20)))
                rand_val.append(val)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_key[0] + ".update(" +
                                 rand_key[1] + ", " +
                                 rand_attr[0] + ", " +
                                 str(rand_val[0]) + ", " +
                                 rand_attr[1] + ", " +
                                 str(rand_val[1]) + ")")
        rand_key = rand_key[0] + "." + rand_key[1]
        self.assertNotIn(rand_attr[1], storage.all()[rand_key].__dict__)
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for attr, val in json_dict[rand_key].items():
            if attr == rand_attr[1]:
                self.assertNotEqual(val, rand_val[1])
                break

        # Correct update of object
        storage._FileStorage__objects.clear()
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.sample(attr, 2)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        rand_attr = random.choice(attr)
        if type(attr_dict[rand_key[0]][rand_attr]) == str:
            rand_val = ''.join(random.choice(string.ascii_letters)
                               for _ in range(20))
        if type(attr_dict[rand_key[0]][rand_attr]) == int:
            rand_val = random.randint(1, 1000)
        if type(attr_dict[rand_key[0]][rand_attr]) == float:
            rand_val = random.random() * 10.0
        if type(attr_dict[rand_key[0]][rand_attr]) == list:
            rand_val = []
            for i in range(3):
                rand_val.append(''.join(random.choice(string.ascii_letters)
                                        for _ in range(20)))
        old_storage = copy.deepcopy(storage.all())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_key[0] + ".update(" +
                                 rand_key[1] + ", " +
                                 rand_attr + ", " +
                                 str(rand_val) + ")")
        rand_key = rand_key[0] + "." + rand_key[1]
        self.assertNotIn(rand_attr, old_storage[rand_key].__dict__)
        self.assertIn(rand_attr, storage.all()[rand_key].__dict__)
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for attr, val in json_dict[rand_key].items():
            if attr == rand_attr:
                self.assertEqual(val, str(rand_val))
                self.assertEqual(val,
                                 storage.all()[rand_key].__dict__[rand_attr])
                self.assertNotIn(attr,
                                 old_storage[rand_key].__dict__)
                break

    def test_dot_update_dict(self):
        """\
        Test for correct update command action with its dot version using
        dictionaries.\
        """
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.update()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct message "** instance id missing **"
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
        rand_class = random.choice(HBNBCommand().class_list)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".update()")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        # Correct message "** no instance found **"
        rand_class = random.choice(HBNBCommand().class_list)
        rand_id = str(uuid.uuid4())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_class + ".update(" + rand_id + ")")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        # Correct update of object
        attr_dict = {"Amenity": {"name": ""},
                     "City": {"state_id": "", "name": ""},
                     "User":
                     {"email": "", "password": "",
                      "first_name": "", "last_name": ""},
                     "Place":
                     {"city_id": "", "user_id": "",
                      "name": "", "description": "",
                      "number_rooms": 0, "number_bathrooms": 0,
                      "max_guest": 0, "price_by_night": 0,
                      "latitude": 0.0, "longitude": 0.0,
                      "amenity_ids": []},
                     "Review":
                     {"place_id": "", "user_id": "", "text": ""},
                     "State": {"name": ""}}
        done = False
        while (done is False):
            try:
                key = [key for key in storage.all()
                       if key.split(".")[0] != "BaseModel"]
                rand_key = random.choice(key)
                attr = list(attr_dict[rand_key.split(".")[0]].keys())
                rand_attr = random.sample(attr, 2)
                done = True
            except ValueError:
                pass
        rand_key = rand_key.split(".")
        rand_val = []
        for at in rand_attr:
            if type(attr_dict[rand_key[0]][at]) == str:
                rand_val.append(''.join(random.choice(string.ascii_letters)
                                        for _ in range(20)))
            if type(attr_dict[rand_key[0]][at]) == int:
                rand_val.append(random.randint(1, 1000))
            if type(attr_dict[rand_key[0]][at]) == float:
                rand_val.append(random.random() * 10.0)
            if type(attr_dict[rand_key[0]][at]) == list:
                val = []
                for i in range(3):
                    val.append(''.join(random.choice(string.ascii_letters)
                                       for _ in range(20)))
                rand_val.append(val)
        rand_dict = dict(zip(rand_attr, rand_val))
        old_storage = copy.deepcopy(storage.all())
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(rand_key[0] + ".update(" +
                                 rand_key[1] + ", " +
                                 str(rand_dict) + ")")
        rand_key = rand_key[0] + "." + rand_key[1]
        for attr, val in rand_dict.items():
            self.assertEqual(storage.all()[rand_key].__dict__[attr],
                             val)
            self.assertNotIn(attr, old_storage[rand_key].__dict__)
        with open(storage._FileStorage__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for attr, val in rand_dict.items():
            self.assertEqual(val, json_dict[rand_key][attr])
            self.assertEqual(val,
                             storage.all()[rand_key].
                             __dict__[attr])
            self.assertNotIn(attr, old_storage[rand_key].__dict__)
            break

    def test_count(self):
        """Test for correct count command action."""
        # Correct message "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
        self.assertEqual(f.getvalue(), "** class name missing **\n")
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct count of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)

        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("count " + class_name)
            self.assertEqual(f.getvalue(), "1\n")

    def test_dot_count(self):
        """Test for correct count command action with its dot version."""
        # Correct message "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        # Correct count of object
        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)

        for class_name in HBNBCommand().class_list:
            with mock.patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_name + ".count()")
            self.assertEqual(f.getvalue(), "1\n")


class TestHBNBCommandDoc(TestCase):
    "Tests documentation and pep8 for HBNBCommand class."

    @classmethod
    def setUpClass(cls):
        """Sets the whole functions of the class HBNBCommand to be inspected for
        correct documentation."""
        cls.functions = inspect.getmembers(HBNBCommand,
                                           inspect.isfunction(HBNBCommand))

    def test_doc_module(self):
        """Tests for docstring presence in the module and the class."""
        import console

        self.assertTrue(len(console.__doc__) > 0)
        self.assertTrue(len(console.HBNBCommand.__doc__) > 0)

    def test_doc_fun(self):
        """Tests for docstring presence in all functions of class."""
        for fun in self.functions:
            self.assertTrue(len(fun.__doc__) > 0)

    def test_pep8(self):
        """Tests pep8 style compliance of module and test files."""
        p8 = pep8.StyleGuide(quiet=False)

        res = p8.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
        res = p8.check_files(['tests/test_console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
