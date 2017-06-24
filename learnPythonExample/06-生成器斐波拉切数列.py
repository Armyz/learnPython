# -*- coding:utf-8 -*-

#生成器的不会立即返回需要生成的列表，调用生成器后，返回一个生成器对象
#对象中保持了需要生成列表的算法，每使用一次next()功能后生成数

#普通函数，生成斐波拉切数列
def Fib(times):
    a,b = 0,1
    while times > 0:
        times -= 1
        print(b)
        a,b = b,a+b
    print("Done")

#添加yeild关键字，不会立即生成斐波拉切数列
#此函数将会返回一个生成生成器对象，每次执行一次，生成一个数
def yeildFib(times):
    a,b = 0,1
    while times > 0:
        times -= 1
        yield(b)
        print(b)
        a,b = b,a+b
    print("Done")

if __name__ == "__main__":

    Fib(10)

    a = yeildFib(5)

    print("开始执行生成器对象")
    for x in a:
        pass
