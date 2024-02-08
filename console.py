#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

    # def do_create(self, arg):
    #     if not arg:
    #         print("** class name missing **")
    #         return
        
    #     if not arg in dir(arg):
    #         print("** class doesn't exist **")
    #         return
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()