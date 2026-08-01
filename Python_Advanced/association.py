# Below is an example of association in Python. In this example, 
# we have two classes: Car and Driver. The Car class has a method drive_car that takes a Driver object as an argument, 
# demonstrating the association between the two classes.
class Car:
    def __init__(self,name,brand):
        self.__name = name
        self.__brand = brand

    def get_name(self) -> str:
        return self.__name

    def get_brand(self) -> str:
        return self.__brand

    def drive_car(self,driver:"Driver") -> None:
        print(f"{driver.get_name()} is driving {self.get_brand()}-{self.get_name()} car")


class Driver:
    def __init__(self,name):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

car = Car("Creta","Hyundai")
harsh = Driver("harsh")

car.drive_car(harsh)