!/usr/bin/python3
"""This script explains the AirBnB console."""

import cmd
import re
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """ manages curly braces for flexible attribute modifications"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in shlex.split(arg)]
        else:
            lexer = shlex.split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = shlex.split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ defines the interpreter for AirBnB.

Attributes:
prompt (str): The command prompt.
__classes (list): Supported class names for validation.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """ takes no action when an empty line is received."""
        pass

    def default(self, arg):
        """does default behavior for invalid cmd module inputs."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("* Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """handles the quit command to end the program."""
        return True

    def do_EOF(self, arg):
        """transmits the program termination EOF signal."""
        print("")
        return True

    def do_create(self, arg):
        """creates a fresh instance of a class and outputs its unique ID."""
        argl = parse(arg)
        if len(argl) == 0:
            print("* class name missing *")
        elif argl[0] not in HBNBCommand.__classes:
            print("* class doesn't exist *")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Shows string representation of an instance."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("* class name missing *")
        elif argl[0] not in HBNBCommand.__classes:
            print("* class doesn't exist *")
        elif len(argl) == 1:
            print("* instance id missing *")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("* no instance found *")
        elif len(argl) == 1:
            print("* instance id missing *")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("* no instance found *")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: delete <class> <id> or <class>.delete(<id>)
Removes an instance by ID or class."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("* class name missing *")
        elif argl[0] not in HBNBCommand.__classes:
            print("* class doesn't exist *")
        elif len(argl) == 1:
            print("* instance id missing *")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("* no instance found *")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: outputs all instances of a class or all objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("*Invalid class. *")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj._class.name_:
                    objl.append(obj._str_())
                elif len(argl) == 0:
                    objl.append(obj._str_())
            print(objl)

    def do_count(self, arg):
        """Retrieve instance count."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj._class.name_:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update instance attributes by ID."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("* Missing class name. *")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("* Invalid class. *")
            return False
        if len(argl) == 1:
            print("* Missing instance ID. *")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("* Instance not found. *")
            return False
        if len(argl) == 2:
            print("* Missing attribute name. *")
            return False
        if len(argl) == 3:
          try:
              type(eval(argl[2])) != dict
          except NameError:
              print("* Missing value. *")
              return False

        if len(argl) == 4:
          obj = objdict["{}.{}".format(argl[0], argl[1])]
          if argl[2] in obj._class.dict_.keys():
              valtype = type(obj._class.dict_[argl[2]])
              obj._dict_[argl[2]] = valtype(argl[3])
          else:
              obj._dict_[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
          obj = objdict["{}.{}".format(argl[0], argl[1])]
          for k, v in eval(argl[2]).items():
              if (k in obj._class.dict_.keys() and
                      type(obj._class.dict_[k]) in {str, int, float}):
                  valtype = type(obj._class.dict_[k])
                  obj._dict_[k] = valtype(v)
              else:
                  obj._dict_[k] = v
        storage.save()


        if __name__ == '__main__':
        HBNBCommand().cmdloop()
