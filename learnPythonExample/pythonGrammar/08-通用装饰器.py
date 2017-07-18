# -*- coding:utf-8 -*-
"""
装饰器相当于执行@xxx时将下面的函数名作为参数传送给了装饰器函数
如下面的例子：

@DecoratorFunc
def func2():
    xxx

相当于func2 = DecoratorFunc(func2)

"""
from time import (ctime,sleep)

def DecoratorFunc(funcName):
    print("执行装饰器")

    #为了保证装饰的函函数有参数的情况，应该使用*args和**kwargs保存参数
    #下面为通用的函数装饰，包括参数和返回值
    def inner_func(*args,**kwargs):
        print("%s函数调用时间为:%s"%(funcName.__name__,ctime()))
        ret = funcName(*args,**kwargs)

        return ret #返回原函数的返回值
    print("装饰器执行完毕")
    return inner_func

@DecoratorFunc
def func1():
    print("这是无参数的函数")

@DecoratorFunc
def func2(a,b):
    print("含有两个参数：%d %d"%(a,b))

@DecoratorFunc
def func3(a,b,c,d):
    print("含有多个个参数：%d %d %d %d"%(a,b,c,d))

@DecoratorFunc
def func4(a):
    print("参数:%d"%a)
    return "这是一个函数返回测试"

func1()
func2(11,22)
func3(11,22,33,44)

ret =func4(100)
print(ret)
