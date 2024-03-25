#!/usr/bin/python3

"""
Fichier: test_console.py
Auteur: Teddy Deberdt
Date: 2024-03-25
Description: Tests pour vérifier les améliorations apportées à la console HBNB.
"""
from models.engine.file_storage import FileStorage
from unittest.mock import patch, MagicMock
from console import HBNBCommand
from io import StringIO
import unittest


class TestDoCreate(unittest.TestCase):

    def setUp(self):
        """Configuration avant chaque test."""
        self.mock_stdout = patch('sys.stdout', new_callable=StringIO)
        self.mock_storage_new = patch('models.storage.new', MagicMock())
        self.mock_storage_save = patch('models.storage.save', MagicMock())

    def tearDown(self):
        """Nettoyage après chaque test."""
        patch.stopall()

    def test_create_missing_class_name(self):
        """Teste la réaction à l'absence du nom de classe."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('')
            self.assertEqual("** class name missing **\n",
                             mocked_out.getvalue())

    def test_create_class_does_not_exist(self):
        """Teste la réaction à un nom de classe invalide."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('NonExistentClass')
            self.assertEqual("** class doesn't exist **\n",
                             mocked_out.getvalue())

    def test_create_attribute_format_error(self):
        """Teste la réaction à un format d'attribut malformé."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('User email="user@example.com" Password')
            self.assertIn(
                "** attribute format error **: Password (expected key=value)", mocked_out.getvalue())

    def test_create_with_valid_attributes(self):
        """Teste la création avec des attributs valides."""
        with self.mock_stdout as mocked_out, self.mock_storage_new, self.mock_storage_save:
            HBNBCommand().do_create('Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            # Assert que storage.new a été appelé avec l'objet ayant les attributs corrects
            # Note : Cela nécessite une compréhension plus approfondie de la manière dont votre modèle et stockage fonctionnent ensemble

    def test_create_with_mixed_types_attributes(self):
        """Teste la création avec des attributs de types mixtes."""
        with self.mock_stdout as mocked_out, self.mock_storage_new, self.mock_storage_save:
            HBNBCommand().do_create(
                'Place name="My_little_house" number_rooms=4 latitude=37.773972 longitude=-122.431297')
            # Vérifiez si l'objet a été correctement créé avec les attributs attendus

    def test_create_with_complex_string_attributes(self):
        """Teste la création avec des chaînes complexes comme attributs."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('Place name="\\\"My little house\\\""')
            # Insérez des vérifications spécifiques ici

    def test_create_with_incomplete_attributes(self):
        """Teste la création avec des spécifications d'attributs incomplètes."""
        with self.mock_stdout as mocked_out:
            HBNBCommand().do_create('User email=')
            self.assertIn("** attribute format error **",
                          mocked_out.getvalue())


if __name__ == "__main__":
    unittest.main()
