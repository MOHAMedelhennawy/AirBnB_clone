#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    Classes = ['BaseModel']

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

    def do_undo(self, arg):
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
        if arg not in self.Classes:
            print("** class doesn't exist **")
            return
        new_obj = BaseModel()
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
        if cmd_args[0] not in self.Classes:
            print("** class doesn't exist **")
            return
        if len(cmd_args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = '{}.{}'.format(cmd_args[0], cmd_args[1])
        if (all_objs[key]):
            print(all_objs[key])
        else:
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
        if cmd_args[0] not in self.Classes:
            print("** class doesn't exist **")
            return
        if len(cmd_args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if (cmd_args[1] == obj_id):
                all_objs.pop()
                del all_objs[obj_id]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all OR all <class name>
        """
        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        if (len(cmd_args) == 1):
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            for obj_id in all_objs.keys():
                if(cmd_args[1] == all_objs[obj_id]['__class__']):
                    print(all_objs[obj_id])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
