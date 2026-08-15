from observers import Observers

class TVDisplay(Observers):

    def update(self, tv_temp):
        print(f"TV Display temperature is {tv_temp}")