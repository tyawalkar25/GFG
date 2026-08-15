from text_memento import TextMemento
from typing import List

class History:
    def __init__(self):
        self.__mementos : List[TextMemento] = []

    def save_state(self, memento: TextMemento) -> None:
        self.__mementos.append(memento)

    def undo(self) -> TextMemento:
        if len(self.__mementos) > 0:
            self.__mementos.pop()
            if len(self.__mementos) == 0:
                return TextMemento("")
            return self.__mementos[-1]

        else:
            return TextMemento("")

    def get_mementos(self) -> TextMemento:
        for i in range(len(self.__mementos)):
            print(f"State {i+1}: {self.__mementos[i].get_saved_text()}")
        return self.__mementos