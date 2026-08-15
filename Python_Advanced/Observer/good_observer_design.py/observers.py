from abc import ABC, abstractmethod

class Observers(ABC):

    @abstractmethod
    def update(self, observer_temp):
        pass
