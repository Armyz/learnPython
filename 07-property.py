
'''
property ：
1.讲类方法变为转换为只读属性
2.对类对象中的私有变量进行修改和值获取的一种方法,setter和getter方法
'''
class Test(object):
    def __init__(self):
        self.__num = 21

    @property
    def num(self):
        print("-----getter------")
        return self.__num

    @num.setter
    def num(self,newNum):
        print("-----setter------")
        self.__num = newNum

t = Test()
t.num = 100
print(t.num)
