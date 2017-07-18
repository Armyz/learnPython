# -*- coding:utf-8 -*-

class Car():
    def __init__(self):
        self.color = "黑色"
        self.wheel = 3
    def move(self):
        print("目标为夏威夷")

    @staticmethod
    def cash():
        print("ssss")

BMW = Car()
BMW.color = "write"
print("color = %s"%BMW.color)
print("wheel = %s"%BMW.wheel)
BMW.move()
BMW.cash()
