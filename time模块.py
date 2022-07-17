from abc import ABCMeta

class WaterHeater:
    """热水器；战胜寒冬的有利武器"""

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemparature(self,tmp):
        self.__temperature = tmp
        print("当前的温度："+str(self.__temperature) +'度')
        self.notifies()

    def