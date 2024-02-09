#!/usr/bin/python3
""" Displays console like a shell """


import cmd


class HBNBCommand(cmd.Cmd):
    """ Console desplay in python along with its method"""
    def do_EOF(self, line):
        """Exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """new line for empty lines"""
        pass


if __name__ ==  "__main__":
    HBNBCommand().cmdloop()

