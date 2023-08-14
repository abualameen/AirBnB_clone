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


class TestConsole(unittest.TestCase):
    """
    this class is the test cases for the creat

    """
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
        #instance.created_at = instance.created_at.isoformat()
        #instance.updated_at = instance.created_at.isoformat()
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

            
if __name__ == '__main__':
    unittest.main()
