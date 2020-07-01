#!/usr/bin/python3
"""
Console or simple framework for writing line-oriented command interpreters
"""
import cmd
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    program that contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """ Quit command to exit the program"""
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
        method and it returns the last command which is a global variable
        called as 'lastcmd'. The method emptyline(), override the variable
        'lastcmd' asigning double quotes.
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_create(self, name_class):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. (Ex: $ create BaseModel)
        """
        if not name_class:
            print("** class name missing **")
            return
        if name_class == 'BaseModel':
            obj_base = BaseModel()
            obj_base.save()
            print(obj_base.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, class_and_id):
        """
        Prints the string representation of an instance based on the
        class name and id. (Ex: $ show BaseModel 1234-1234-1234)
        """
        if not class_and_id:
            print("** class name missing **")
            return

        validator_str = class_and_id.split()
        try:
            eval(validator_str[0])
        except:
            print("** class doesn't exist **")
            return

        if len(validator_str) < 2:
            print("** instance id missing **")

        all_objs = storage.all()
        for obj_id in all_objs:
            id_ = obj_id.split('.')
            if validator_str[1] == id_[1]:
                print(all_objs[obj_id])
                break
        else:
            print("** no instance found **")

    def do_destroy(self, class_del_id):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not class_del_id:
            print("** class name missing **")
            return

        validator_str = class_del_id.split()
        try:
            eval(validator_str[0])
        except:
            print("** class doesn't exist **")
            return

        if len(validator_str) < 2:
            print("** instance id missing **")

        all_objs = storage.all()
        for obj_id in all_objs:
            id_ = obj_id.split('.')
            if validator_str[1] == id_[1]:
                del all_objs[obj_id]
                storage.save()
                break
        else:
            print("** no instance found **")

    def do_all(self, optional_nameClass):
        """
        Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all.
        * The printed result must be a list of strings
        * If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ all MyModel)
        """
        objects_list = []
        _object = ""
        if optional_nameClass:
            try:
                eval(optional_nameClass)
            except:
                print("** class doesn't exist **")
                return
        all_objs = storage.all()
        for _, value in all_objs.items():
            _object = str(value)
            objects_list.append(_object)
        print(objects_list)

    def do_update(self, arg_mod_obj):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        validator_str = arg_mod_obj.split()
        all_objs = storage.all()

        if not arg_mod_obj:
            print("** class name missing **")
            return
        if arg_mod_obj:
            try:
                eval(validator_str[0])
            except:
                print("** class doesn't exist **")
                return
        if len(validator_str) < 2:
            print("** instance id missing **")
            return
        if len(validator_str) < 3:
            print("** attribute name missing **")
            return
        if len(validator_str) < 4:
            print("** value missing **")
            return

        for obj_id in all_objs:
            id_ = obj_id.split('.')
            if validator_str[1] == id_[1]:
                break
        else:
            print("** no instance found **")

        for  find_id in all_objs:
            _id = find_id.split('.')
            if validator_str[1] == _id[1]:
                setattr(all_objs[find_id], validator_str[2], validator_str[3])
                all_objs[find_id].save()
                break

if __name__ == '__main__':
    HBNBCommand().cmdloop()
