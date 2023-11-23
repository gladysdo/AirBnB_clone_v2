import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage

class TestConsoleCreateMethod(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        storage.reset()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_params(self, mock_stdout):
        self.console.do_create("BaseModel name=\"My_little_house\" value=42.5")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith(""))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        self.console.do_create("")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_nonexistent_class(self, mock_stdout):
        self.console.do_create("NonExistentClass")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()

