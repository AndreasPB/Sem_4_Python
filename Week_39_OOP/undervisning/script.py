from inst import *

class Person:

    type = 'Mammel'

    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        if len(args) == 2:
            self.name = args[0]
            self.last = args[1]
        else:
            raise Exception()

    def full_name(self):
        """
        docstring
        """
        return self.name + ' ' + self.last + ' ' + self.funny

    def funny_age(self):
        self.funny = 'HahAhahaHa'

p = Person('Andreas', 'Brodersen')

#class Student:
#    def __init__(self, name):
#        self.name = name

s = Student('Jens')

class Instructor(Student):
    def __init__(self, *args):
        # super().__init__(args[0])
        Student.__init__(self, args[0])
        self.salary = args[1]

i = Instructor("Erik", 69420)

class Gender:
    def __init__(self, s):
        self.sex = s