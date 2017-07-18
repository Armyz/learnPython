class Dog(object):
    def __init__(self):
        print("__init__方法")
    def __str__(self):
        print("__str__方法")
    def __del__(self):
        print("__del__方法")
    def __new__(cls):
        print("__new__方法")
        return object.__new__(cls)

xtq=Dog()
