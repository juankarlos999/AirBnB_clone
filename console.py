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

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exit interpreter Crtl + D"""
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt. If this
        method is not overridden, it repeats the last nonempty comman entered.
        cmd execute precmd, onecmd and postcmd methods sequentially. onecmd is
        the main one which exetues the given line.
        This method check the line, if line is empty it calls the emptyline
        method and it returns the last command which is a global variable called
        as 'lastcmd'. The method emptyline(), override the variable 'lastcmd'
        asigning double quotes.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
