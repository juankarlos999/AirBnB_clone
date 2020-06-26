#!/usr/bin/python3
"""
Console or simple framework for writing line-oriented command interpreters
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    program that contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'

if __name__ == '__main__':
    HBNBCommand().cmdloop()
