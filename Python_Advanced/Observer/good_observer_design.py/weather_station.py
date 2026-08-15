from observers import Observers
from typing import List
from mobile import Mobile

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observers : List[Observers] = []

    def update_temperature(self, new_temp):
        self.__temperature = new_temp
        self.notify_temperature_update()

    def add_observer(self, new_observer : Observers):
        return self.__observers.append(new_observer)

    def remove_observer(self, observer: Observers):
        self.__observers.remove(observer)

    def notify_temperature_update(self):
        for ob in self.__observers:
            ob.update(self.__temperature)

