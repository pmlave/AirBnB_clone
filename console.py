#!/usr/bin/python3
"""Method Command Interpreter"""

import inspect
import cmd, sys
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
        if args != 'BaseModel':
            print("** class doesn't exist **")
        else:
            new_creation = BaseModel()
            models.storage.save()
            print(new_creation.id)

    def do_show(self, args):
        """Prints the string representation of a specific instance
        Usage: show <class name> <id>
        """
        strings = args.split()
        if len(strings) == 1:
            print("** instance id missing **")
        elif len(strings) == 0:
            print("** class name missing **")
        elif strings[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                print(models.storage.all()[key_value])
            except KeyError:
                print("** no instance found **")
    def do_destroy(self, args):
        """Deletes an instance
        Usage: destroy <class name> <id>
        """

    def do_all(self, args):
        """Prints a string representation of all instances, can include class
        name to specify only instances of that class
        Usage: destroy <class name> <id>
        """

    def do_update(self, args):
        """Update an instance.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
    def do_quit(self, args):
        """Quits the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """Handles end of file condition
        """
        return True

    def do_help(self, args):
        """Get help on commands
        'help' or '?' with no arguments prints a list of commands for which
        help is available
        'help <command>' or '? <command>' gives help on <command>
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """Doesn't execute anything when user enter an empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
