# -*- coding:utf-8 -*-


class Foo(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item, end=" ")
        return self

    # 打印时FOO对象时，默认的输出修改，若没有重写。则默认打印对象的地址
    def __str__(self):
        return ""

# 在类查找类属性时，首先查找实例字典foo.__dict__字典中是否有该属性，若没有
# 则类的属性魔法属性Foo.__dict__字典中没有则最后在__getattr__中是否是否有此属性。
# 在此可使用pycharm进行调试跟踪
print(Foo().think.diffent.hello)
