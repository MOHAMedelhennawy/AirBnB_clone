#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    Classes_dict = {"BaseModel": BaseModel}
    instance = []
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
            print("{}".format(new_obj.id))

        # Create a list of instances
        self.instance.append(new_obj)
        self.instance_representation.append(new_obj.__str__())

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

        # Check for id in instance list and return obj if ture, otherwise do nothing "False"
        matching_instances = [check_id for check_id in self.instance if check_id.id == cmd_args[1]]

        # if true print representation of an instance, otherwise print Err_msg
        if matching_instances:
            print(matching_instances[0])
        else:
            print("** no instance found **")
            return


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

        flag = 0
        for check_id in self.instance:
            if check_id.id == cmd_args[1]:
                flag = 1
                representation = check_id.__str__() # Or you can write => str(check.id)
                self.instance.remove(check_id)
                self.instance_representation.remove(representation)
        if flag == 0:
            print("** no instance found **")


    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all OR all <class name>
        """
        cmd_args = arg.split()
        if cmd_args[0] not in self.Classes_dict.keys() and len(self.instance_representation) != 0:
            print("** class doesn't exist **")
            return

        print(self.instance_representation)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
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

        matching_instances = [check_id for check_id in self.instance if check_id.id == cmd_args[1]]

        if not matching_instances:
            print("** no instance found **")
            return

        if len(cmd_args) < 3:
            print("** attribute name missing **")
            return
        
        if len(cmd_args) < 4:
            print("** value missing **")
            return

        var, value = cmd_args[2], cmd_args[3]
        setattr(matching_instances[0], var, value)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
