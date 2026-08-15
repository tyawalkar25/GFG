from text_memento import TextMemento

class TextEditor:

    def __init__(self):
        self.__text = ""

    def write_text(self,new_text) -> None:
        
        self.__text += new_text

    def get_text(self) -> str:
        return self.__text

    def restore(self, memento: TextMemento):
        self.__text = memento.get_saved_text()

    def save(self) -> TextMemento:
        return TextMemento(self.__text)
        



