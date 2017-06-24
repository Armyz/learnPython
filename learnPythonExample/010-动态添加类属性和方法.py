#coding=utf-8

import types

class Person(object):
    def __init__(self,newName):
        self.name = newName

def run(self):
    print("%s在%s跑步"%(self.name,self.addr))

@staticmethod #静态方法没有self
def eat():
    #print("%s在%s在吃饭"%(self.name,self.addr))
    print("吃饭")

@classmethod #
def sleeping(cls):
    #print("%s在%s在睡觉"%(cls.name,cls.addr))
    print("在睡觉")


p1 = Person("老李")
p2 = Person("老赵")

#动态添加实例属性
#新创建的实例属性不可用
p1.age = 100;
print(p1.age)
#print(p2.age)  #不可用

#动态添加类属性，
#所有的实例对象均可以使用
Person.addr = "北京"
print(p1.addr)
print(p2.addr)

#动态添加实例方法
#使用types包中的MethodType(function,instance)动态添加
p1.run = types.MethodType(run,p1)
p1.run()
#p2.run() #不可用,，需要使用run方法需要重新添加

#动态添加静态方法
#Person.eat = types.MethodType(eat,Person)
Person.eat = eat
p1.eat()
p2.eat()

#动态添加类方法
#Person.eat = types.MethodType(eat,Person)
Person.sleepping = sleeping
p1.sleepping()
p2.sleepping()
