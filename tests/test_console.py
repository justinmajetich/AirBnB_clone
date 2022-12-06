#!/usr/bin/python3

"""This is Console Test Module."""

import json
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class TestConsole(unittest.TestCase):
    """Implement Unittest for the console."""

    def test_help(self):
        """Test the help method."""
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, f.getvalue())

    def test_empty_line(self):
        """Test empty line method."""
        expected = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(expected, f.getvalue())

    def test_quit(self):
        """Test quit method."""
        expected = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(expected, f.getvalue())

    def test_eof(self):
        """Test quit method."""
        expected = ""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(expected, f.getvalue())

    def test_create_without_model_fail(self):
        """Test if create without model fails."""
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(expected, f.getvalue())

    def test_create_with_wrong_model_fail(self):
        """Test if create with wrong model fails."""
        expected = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create FakeModel")
            self.assertEqual(expected, f.getvalue())

    def test_show_without_model_fail(self):
        """Test if show without model fails."""
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(expected, f.getvalue())

    def test_show_with_wrong_model_fail(self):
        """Test if show with wrong model fails."""
        expected = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show FakeModel")
            self.assertEqual(expected, f.getvalue())

    def test_show_without_inst_id_fail(self):
        """Test if show without inst id fails."""
        expected = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expected, f.getvalue())

    def test_show_with_wrong_inst_id_fail(self):
        """Test if show with wrong inst id fails."""
        expected = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 24217-2372673")
            self.assertEqual(expected, f.getvalue())

    def test_update_without_model_fail(self):
        """Test if update without model fails."""
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(expected, f.getvalue())

    def test_update_with_wrong_model_fail(self):
        """Test if update with wrong model fails."""
        expected = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update FakeModel")
            self.assertEqual(expected, f.getvalue())

    def test_update_without_inst_id_fail(self):
        """Test if update without inst id fails."""
        expected = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(expected, f.getvalue())

    def test_update_with_wrong_inst_id_fail(self):
        """Test if show with wrong inst id fails."""
        expected = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 24217-2372673")
            self.assertEqual(expected, f.getvalue())

    def test_destroy_without_model_fail(self):
        """Test if destroy without model fails."""
        expected = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expected, f.getvalue())

    def test_destroy_with_wrong_model_fail(self):
        """Test if show with wrong model fails."""
        expected = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy FakeModel")
            self.assertEqual(expected, f.getvalue())

    def test_destroy_without_inst_id_fail(self):
        """Test if destroy without inst id fails."""
        expected = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(expected, f.getvalue())

    def test_destroy_with_wrong_inst_id_fail(self):
        """Test if destroy with wrong inst id fails."""
        expected = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 24217-2372673")
            self.assertEqual(expected, f.getvalue())

    def test_all(self):
        """Test if all return list of all instances."""
        out = []
        for k, v in storage.all().items():
            k = k.split('.')
            v = v.to_dict()
            obj = eval(f'{k[0]}(**v)')
            out.append(str(obj))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f'{out}\n', f.getvalue())

    def test_all_model(self):
        """Test if all return list of all instances of a model."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"all {name}")
                out = []
                for k, v in storage.all().items():
                    k = k.split('.')
                    if name == k[0]:
                        v = v.to_dict()
                        obj = eval(f'{name}(**v)')
                        out.append(str(obj))
                self.assertEqual(f'{out}\n', f.getvalue())

    def test_update_def_models(self):
        """Test if all each model can be updated."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {name}")
                id = f.getvalue().replace('\n', '')
            with patch('sys.stdout', new=StringIO()) as f:
                fmt = ".update(" + id + ", {'attribute_name': 'string_value'})"
                HBNBCommand().onecmd(name + fmt)
                self.assertEqual('', f.getvalue())
                storage.reload()
                key = f'{name}.{id}'
                with open('file.json', 'r', encoding='utf-8') as f:
                    dict_obj = json.loads(f.read())
                obj = dict_obj[key]
                self.assertIn('attribute_name', obj)
                self.assertEqual(obj['attribute_name'], 'string_value')

    def test_count_def_models(self):
        """Test if method count return the total instance of each model."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f'{name}.count()')
                cmd_cnt = f.getvalue()
                cnt = 0
                for k in storage.all():
                    # nme = k[:k.index('.')]
                    if name in k:
                        cnt += 1
                print(name)
                self.assertEqual(f'{str(cnt)}\n', cmd_cnt)

    def test_show_def_with_wrong_model_fail(self):
        """Test if show with wrong model fails."""
        expected = "** class doesn't exist **\n"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("FakeModel.show()")
            self.assertEqual(expected, f.getvalue())

    def test_show_def_without_inst_id_fail(self):
        """Test if show without inst id fails."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']
        expected = "** instance id missing **\n"

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{name}.show()")
                self.assertEqual(expected, f.getvalue())

    def test_show_def_with_wrong_inst_id_fail(self):
        """Test if show with wrong inst id fails."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']
        expected = "** no instance found **\n"

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{name}.show(24217-2372673)")
                self.assertEqual(expected, f.getvalue())

    def test_destroy_def_with_wrong_model_fail(self):
        """Test if show with wrong model fails."""
        expected = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("FakeModel.destroy()")
            self.assertEqual(expected, f.getvalue())

    def test_destroy_def_without_inst_id_fail(self):
        """Test if destroy without inst id fails."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']
        expected = "** instance id missing **\n"

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{name}.destroy()")
                self.assertEqual(expected, f.getvalue())

    def test_destroy_def_with_wrong_inst_id_fail(self):
        """Test if destroy with wrong inst id fails."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']
        expected = "** no instance found **\n"

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{name}.destroy(24217-2372673)")
                self.assertEqual(expected, f.getvalue())

    def test_def_all_model(self):
        """Test if all return list of all instances of a model."""
        class_name = ['BaseModel', 'City', 'State', 'Place']
        class_name += ['Review', 'Amenity', 'User']

        for name in class_name:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{name}.all()")
                out = []
                for k, v in storage.all().items():
                    k = k.split('.')
                    if k[0] == name:
                        v = v.to_dict()
                        obj = eval(f'{k[0]}(**v)')
                        out.append(str(obj))
                self.assertEqual(f'{out}\n', f.getvalue())
