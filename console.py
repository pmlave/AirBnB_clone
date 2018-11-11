#!/usr/bin/python3
"""Method Command Interpreter"""

import cmd, sys

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit():
        """Quits the program"""
        raise SystemExit

    def do_EOF(self):
        """Handles end of file condition"""
        return True

    def do_help(self, args):
        """Get help on commands
        'help' or '?' with no arguments prints a list of commands for which help is available
        'help <command>' or '? <command>' gives help on <command>
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """Doesn't execute anything when user enter an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
