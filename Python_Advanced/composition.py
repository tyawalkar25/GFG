# Example of composition: an apartment contains a kitchen as a dependent part of the object.

class Apartment:

    def __init__(self, bhk:str, kitchen_type:str, kitchen_size:str):
        self.__bhk = bhk
        self.__kitchen = Kitchen(kitchen_type, kitchen_size)

    def get_bhk(self) -> str:
        return self.__bhk

    def get_kitchen(self) -> "Kitchen":
        return self.__kitchen

    def get_apartment_details(self) -> None:
        print(f"Apartment BHK: {self.get_bhk()}")
        print(f"Kitchen Type: {self.get_kitchen().get_type()}")
        print(f"Kitchen Size: {self.get_kitchen().get_size()}")

    

class Kitchen:

    def __init__(self, type:str, size:str):
        self.__type : str = type
        self.__size : str = size

    def get_type(self) -> str:
        return self.__type

    def get_size(self) -> str:
        return self.__size

my_apartment: Apartment = Apartment("2BHK", "Modular", "Medium")
my_apartment.get_apartment_details()