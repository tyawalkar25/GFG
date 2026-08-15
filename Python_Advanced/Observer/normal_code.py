class Mobile:
    def update(self, device_temp):
        print(f"The temperature on the mobile is {device_temp}")

class TV:
    def update(self, device_temp):
        print(f"The temperature on TV is {device_temp}")

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__device_type_1 = Mobile()
        self.__device_type_2 = TV()

    def update_temperature(self, new_temerature):
        self.__temperature = new_temerature
        
        self.notify_temperature_update()
        

    def notify_temperature_update(self):
        self.__device_type_1.update(self.__temperature)
        self.__device_type_2.update(self.__temperature)


ws1 = WeatherStation()
ws1.update_temperature(35)


