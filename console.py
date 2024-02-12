#!/usr/bin/python3
""" Displays console like a shell """


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    """ Console desplay in python along with its method"""
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """new line for empty lines"""
        pass

    def do_show(self, line):
        pass

    def do_create(self, line):
        pass

    def do_destroy(self, line):
        pass

    def do_update(self, line):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
