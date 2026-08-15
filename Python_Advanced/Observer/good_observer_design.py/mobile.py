from observers import Observers

class Mobile(Observers):

    def update(self, mobile_temp):
        print(f"Mobile temperature is {mobile_temp}")