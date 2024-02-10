#!/usr/bin/python3

import cmd
import sys
import models
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    Classes_dict = {
        "BaseModel": BaseModel, "User": User, "City": City,
        "Place": Place, "Review": Review, "Amenity": Amenity, "State": State
                    }
    all_objs = storage.all()
    instance_representation = []

    def do_EOF(self, args):
        """Exit command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def help_quit(self):
        """help quit command to display ...
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help quit command to display ...
        """
        print("Exit command to exit the program\n")

    def emptyline(self):
        """an empty line + ENTER should not execute anything
        """
        ...

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Usage: create <class name>
        """

        if not arg:
            print("** class name missing **")
            return
        if arg not in self.Classes_dict:
            print("** class doesn't exist **")
            return

        if arg in self.Classes_dict.keys():
            new_obj = self.Classes_dict[arg]()
            new_obj.save()
            print("{}".format(new_obj.id))

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <object id>
        """
        if not arg:
            print("** class name missing **")
            return

        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(cmd_args[0], cmd_args[1])
        try:
            cls_name = self.Classes_dict[cmd_args[0]]
            print(cls_name(self.all_objs[key]))
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Usage: destroy <class name> <object id>
        """
        if not arg:
            print("** class name missing **")
            return

        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(cmd_args[0], cmd_args[1])
        try:
            deleted_representaiton = str(self.all_objs[key])
            self.instance_representation.remove(deleted_representaiton)
            del self.all_objs[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all OR all <class name>
        """

        self.instance_representation = []
        if not arg:
            if self.all_objs:
                for obj_dict in self.all_objs.values():
                    self.instance_representation.append(str(obj_dict))

        else:
            if arg not in self.Classes_dict.keys():
                print("** class doesn't exist **")
                return
            for obj_dict in self.all_objs.values():
                cls_name = self.Classes_dict[arg]
                if isinstance(obj_dict, cls_name):
                    self.instance_representation.append(str(obj_dict))
        print(self.instance_representation)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        update <class name> <id> <attribute name> "<attribute value>"
        """

        if not arg:
            print("** class name missing **")
            return

        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(cmd_args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(cmd_args[0], cmd_args[1])
        try:
            obj_dict = self.all_objs[key]
        except KeyError:
            print("** no instance found **")
            return

        if len(cmd_args) < 3:
            print("** attribute name missing **")
            return

        if len(cmd_args) < 4:
            print("** value missing **")
            return

        var, value = cmd_args[2], cmd_args[3].strip('"')
        if var not in ["id", "updated_at", "created_at"]:
            setattr(obj_dict, var, value)
            obj_dict.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
