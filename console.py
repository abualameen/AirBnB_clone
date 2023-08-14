#!/usr/bin/python3
"""
this module is the implementation of the command intepreter

"""
import cmd
import sys


from models.base_model import BaseModel
import models
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    this class is the command interpreter for the projec
    """
    intro = "Welcome to my AirBnB clone command intepreter!"
    prompt = "(hbnb) "
    __prog_classes = [
        "BaseModel",
        "FileStorage",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_quit(self, arg):
        """
        this method quit command to exit the programm.

        """
        return True

    def do_EOF(self, arg):
        """
        this method Exit the program on EOF (Ctrl+D)

        """
        print()
        return True

    def emptyline(self):
        """
        this method pass if the line is empty

        """
        pass

    def help_quit(self):
        """
        this method is prints help message for quit command

        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        this method prints the help message for EOF command (Ctrl+D)

        """
        print("Exi the program on EOF (Ctrl+D)")

    def do_create(self, args):
        """
        this method create a new instanco of BaseModel,
        and saves it to the JSON
        file and prints the id

        """
        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__prog_classes:
            print("** class doesn't exist **")
        else:
            try:
                new_instance = eval(args[0] + '()')
                models.storage.save()
                print(new_instance.id)
            except Exception as e:
                print(e)

    def do_show(self, arg):
        """
        this method prints str representation of an instance base on
        the class name and id
        how to use: show <class name> <id>

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in [cls for cls in HBNBCommand.__prog_classes]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            obj_key = args[0] + "." + args[1]
            if obj_key in all_objs:
                print(all_objs[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        this method deletes an instance based on the class name and id

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__prog_classes:
            print("** class does'nt exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            obj_key = args[0] + "." + args[1]
            if obj_key in all_objs:
                del all_objs[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        this method print all string representation of all instances
        based or not on the class name

        """
        args = arg.split()
        all_objs = models.storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        else:
            if args[0] in HBNBCommand.__prog_classes:
                instance_list = [
                    str(obj) for key, obj in all_objs.items()
                    if key.split('.')[0] == args[0]
                ]
                print(instance_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        this method updates an instance based on the class name and id
         Usage: update <class name> <id> <attribute name> "<attribute value>"

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__prog_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            obj_key = args[0] + "." + args[1]
            if obj_key not in all_objs:
                print("** no instance found **")
            elif len(args) < 3:
                print("*** attribute name missing **")
            elif len(args) < 4:
                print("** value mising **")
            else:
                try:
                    setattr(all_objs[obj_key], args[2], eval(args[3]))
                    models.storage.save()
                except Exception:
                    pass

    def default(self, line):
        """
        this method handls default behaviors of custom method
        lisek User.count()

        """
        parts = line.split('.')
        if len(parts) > 1 and \
                parts[0] in HBNBCommand.__prog_classes:
            if parts[1] == "count()":
                print(models.storage.count(parts[0]))
                return
            elif parts[1].startswith("show(") and parts[1].endswith(")"):
                method_args = parts[1][6:-1]
                method_args = method_args.strip()
                class_name = parts[0]
                obj_id = method_args.strip("\"")  # remove quotes if present
                self.do_show(f"{class_name} {obj_id}")
                return
            elif parts[1].startswith("destroy(") and parts[1].endswith(")"):
                method_args = parts[1][9:-1]
                method_args = method_args.strip()  # remove whitespace
                class_name = parts[0]
                obj_id = method_args.strip("\"")
                self.do_destroy(f"{class_name} {obj_id}")
                return
            elif parts[1] == "all()":
                self.do_all(parts[0])
                return
            elif parts[1].startswith("update(") and parts[1].endswith(")"):
                method_args = parts[1][7:-1]  # extract method arguments excluding "update(" and ")"
                method_args = method_args.strip()  # remove whitespace
                class_name = parts[0]
                args = method_args.split(",", 1)  # Split arguments into ID and dictionary representation
                if len(args) == 3:  # to see if it's update with attribute name and value
                    obj_id = args[0].strip().strip("\"")
                    attribute_name = args[1].strip().strip("\"")
                    attribute_value = args[2].strip().strip("\"")
                    self.do_update(f"{class_name} {obj_id} {attribute_name} {attribute_value}")
                else:
                    obj_id = args[0].strip().strip("\"")
                    dictionary_repre = args[1].strip()
                    self.do_update(f"{class_name} {obj_id} {dictionary_repre}")
                return
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
