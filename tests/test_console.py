#!/usr/bin/python3
"""Este es un test para la consola"""
import unittest
from unittest.mock import path
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


# Define una clase llamada TestConsole que hereda de unittest.TestCase
class TestConsole(unittest.TestCase):
    """Este test probará la consola"""

# Este método se ejecuta una vez antes de ejecutar las pruebas
    @classmethod
    def setUpClass(cls):
        """Configuracion para la prueba"""
        # Crea una instancia de la clase HBNBCommand y la asigna a la
        # variable de clase 'consol'
        cls.consol = HBNBCommand

    def tearDown(self):
        """Remueve el archivo temporal(file.json) creado como resultado"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """Comprobando docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Prueba de entrada de linea vacia"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create qwerty")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="user" password="passwd"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual(
                "[\"[User", f.getvalue()[:7])

    def test_show(self):
        """Prueba de entrada del comando show"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show qwerty")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel Meco")
            self.assertEqual(
                    "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Prueba de entrada del comando destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy Montes")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel 2aq3wsed5rf6tg7yh8")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_all(self):
        """Probar todas las entradas del comando"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.oncmd("all qwerty")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """Probar la entrada del comando de actualización"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update qwerty")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update user")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User aqwsedf5g67hj8")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all user")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + my_id + ")")
            self.assertNotEqual("** attribute name missing **",
                                f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + my_id + ", name)")
            self.assertNotEqual("** Value missing **\n",
                                f.getvalue())


if __name__ == "__main__":
    unittest.main()
