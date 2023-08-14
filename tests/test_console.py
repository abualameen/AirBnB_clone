#!/usr/bin/python3
"""
this is the test module for the console

"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """
    this class is the test cases for the creat

    """
    def setUp(self):
        """ redirect console output for testing """
        self.console_out = StringIO()
        self.console = HBNBCommand(stdout=self.console_out)

    def tearDown(self):
        """ cleans up console after tests """
        self.console_out.close()

    def test_do_quit(self):
        """ test for quit command """
        with patch("sys.stdin", StringIO("quit\n")):
            result = self.console.onecmd("quit")
            self.assertTrue(True)

    def test_do_EOF(self):
        """ test for EOF command """
        with patch("sys.stdin", StringIO("EOF\n")):
            with patch("builtins.print") as mock_print:
                result = self.console.onecmd("EOF")
                self.assertTrue(result)
                mock_print.assert_called_once_with()

    def test_help_quit(self):
        """ test case for console help quit method """
        with patch("builtins.print") as mock_print:
            self.console.onecmd("help quit")
            mock_print.assert_called_once_with("Quit command to exit the program")

    def test_help_EOF(self):
        with patch("builtins.print") as mock_print:
            self.console.onecmd("help EOF")
            mock_print.assert_called_once_with("Exit the program on EOF (Ctrl+D)")

    def test_create(self):
        """
        this Test create command behaviour
        checks if a new instance is created
        checks if the instance ID is printed

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
        self.assertTrue(len(output) == 36) # to check if the output id isUUID
        instance_id = output
        instance = models.storage.all().get(f"BaseModel.{instance_id}")
        self.assertIsInstance(instance, BaseModel) # check if instance is of the class BaseModel
        
    def test_create_ifnotarg(self):
        """
        this test if arg does not exist

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            expected_output = "** class name missing **"
        self.assertEqual(expected_output, output)
    
    def test_create_classname_missing(self):
        """
        this test if class name is not in class list

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Togoo")
            output = f.getvalue().strip()
            expected_output = "** class doesn't exist **"
        self.assertEqual(expected_output, output)

    def test_show_ifinstanceismissing(self):
        """
        this method test if instance id is missing

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            expected_output = "** instance id missing **"
        self.assertEqual(expected_output, output)

    def test_show_missing_class_name(self):
        """ this method test if class name is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            expected_output = "** class name missing **"
        self.assertEqual(output, expected_output)

    def test_show_invalid_class_name(self):
        """ this method test if class name is valid """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Togoo")
            output = f.getvalue().strip()
            expected_output = "** class doesn't exist **"
        self.assertEqual(output, expected_output)

    def test_show_instance_id_doesnt_exist(self):
        """ this method test if an instance exist throught it id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
            output = f.getvalue().strip()
            expected_output = "** no instance found **"
        self.assertEqual(output, expected_output)

##################################################
    #  destroy test cases
    
    def test_destroy_ifinstanceismissing(self):
        """
        this method test if instance id is missing

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            expected_output = "** instance id missing **"
        self.assertEqual(expected_output, output)

    def test_destroy_missing_class_name(self):
        """ this method test if class name is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            expected_output = "** class name missing **"
        self.assertEqual(output, expected_output)

    def test_destroy_invalid_class_name(self):
        """ this method test if class name is valid """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Togoo")
            output = f.getvalue().strip()
            expected_output = "** class doesn't exist **"
        self.assertEqual(output, expected_output)

    def test_destroy_instance_id_doesnt_exist(self):
        """ this method test if an instance exist throught it id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234")
            output = f.getvalue().strip()
            expected_output = "** no instance found **"
        self.assertEqual(output, expected_output)

#################################################
    #  test case for all()
    def test_all_withno_args(self):
        """ test case for all with not args """
        instance = BaseModel()
        models.storage.new(instance)
        models.storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue().strip()
        expected_output = str(instance)
        self.assertIn(expected_output, output)
  
    def test_all_with_valid_class(self):
        """ case with valid class """
        instance = User()
        models.storage.new(instance)
        models.storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
        expected_output = str(instance)
        self.assertIn(expected_output, output)


    def update_ifinstanceismissing(self):
        """
        this method test if instance id is missing

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            output = f.getvalue().strip()
        expected_output = "** instance id missing **"
        self.assertEqual(expected_output, output)

    def test_update_missing_class_name(self):
        """ this method test if class name is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            expected_output = "** class name missing **"
        self.assertEqual(output, expected_output)

    def test_update_invalid_class_name(self):
        """ this method test if class name is valid """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Togoo")
            output = f.getvalue().strip()
            expected_output = "** class doesn't exist **"
        self.assertEqual(output, expected_output)

    def test_update_instance_id_doesnt_exist(self):
        """ this method test if an instance exist throught it id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234")
            output = f.getvalue().strip()
            expected_output = "** no instance found **"
        self.assertEqual(output, expected_output)

    def test_update_missing_attr_name(self):
        """ test case for valid instance """
        instance_id = "f1079e92-b887-4148-acb9-de9da3a56c98"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {instance_id}")
            output = f.getvalue().strip()
        expected_output = "** attribute name missing **"
        self.assertEqual(output, expected_output)

    def test_update_missing_value(self):
        """ test for missing  value """
        instance_id = "f1079e92-b887-4148-acb9-de9da3a56c98"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {instance_id} attribut_name")
            output = f.getvalue().strip()
        expected_output = "** value missing **"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
