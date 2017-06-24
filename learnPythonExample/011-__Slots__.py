
class Person(object):
    __slots__ = ("name","age")

p1 = Person()

p1.name = "py"
print(p1.name)

p1.age = 100
print(p1.age)

#在类中使用__slots__属性修饰的变量，才能在实例中动态添加该类属性
#否则不能够使用，下面的语句执行将会出错
#p1.addr = "addr"
#rprint(p1.addr)
