from io import StringIO
import os
import unittest
from unittest import mock
import sys
import uuid

from console import HBNBCommand


class TestConsoleUpdate(unittest.TestCase):
    def setUp(self):
        mock_stdin = mock.create_autospec(sys.stdin)
        mock_stdout = mock.create_autospec(sys.stdout)

        self.hbnbCMD = HBNBCommand(stdin=mock_stdin, stdout=mock_stdout)

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_update_no_uuid(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n",
                fake_out.getvalue(),
            )

    def test_update_no_uuid_instance(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("update User {}".format(uuid.uuid4()))
            self.assertEqual(
                "** no instance found **\n",
                fake_out.getvalue(),
            )

    def test_update_no_class(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("update")
            self.assertEqual("** class name missing **\n", fake_out.getvalue())

    def test_update_object_no_attr(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("create User")
            id = fake_out.getvalue()
            fake_out.seek(0)
            fake_out.truncate(0)
            line = self.hbnbCMD.precmd("update User {}".format(id.strip()))
            self.hbnbCMD.onecmd(line)
            self.assertEqual(
                "** attribute name missing **\n",
                fake_out.getvalue(),
            )

    def test_update_object_no_value(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("create User")
            id = fake_out.getvalue()
            fake_out.seek(0)
            fake_out.truncate(0)
            line = self.hbnbCMD.precmd(
                "update User {} name".format(id.strip()),
            )
            self.hbnbCMD.onecmd(line)
            self.assertEqual(
                "** value missing **\n",
                fake_out.getvalue(),
            )

    def test_update_object(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("create User")
            id = fake_out.getvalue()
            fake_out.seek(0)
            fake_out.truncate(0)
            line = self.hbnbCMD.precmd(
                "update User {} name Ayo".format(id.strip()),
            )
            self.hbnbCMD.onecmd(line)
            self.assertEqual(
                "",
                fake_out.getvalue(),
            )

    def test_update_object_alt_syntax_braces(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("create User")
            id = fake_out.getvalue().strip()
            fake_out.seek(0)
            fake_out.truncate(0)
            line = self.hbnbCMD.precmd(
                # Getting key error for some reason if .format is used
                "User.update("
                + id
                + ", {'name': 'Ayobami'})",
            )
            self.hbnbCMD.onecmd(line)
            self.assertEqual(
                "",
                fake_out.getvalue(),
            )
            fake_out.seek(0)
            fake_out.truncate(0)
            self.hbnbCMD.onecmd("show User {}".format(id))
            self.assertRegex(fake_out.getvalue(), "'name': 'Ayobami")

    def test_update_object_alt_syntax_equals(self):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            self.hbnbCMD.onecmd("create User")
            id = fake_out.getvalue().strip()
            fake_out.seek(0)
            fake_out.truncate(0)
            line = self.hbnbCMD.precmd(
                'User.update({}, name Ayobami)'.format(id),
            )
            self.hbnbCMD.onecmd(line)
            self.assertEqual(
                "",
                fake_out.getvalue(),
            )
            fake_out.seek(0)
            fake_out.truncate(0)
            self.hbnbCMD.onecmd("show User {}".format(id))
            self.assertRegex(fake_out.getvalue(), "'name': 'Ayobami'")
