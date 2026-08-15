from history import History
from text_editor import TextEditor
from text_memento import TextMemento
from typing import List

text_editor = TextEditor()
hist = History()

text_editor.write_text("Hello ")
text_editor.write_text("World")
#print(text_editor.get_text())  # Output: Hello, World!

hist.save_state(text_editor.save())

text_editor.write_text(" Good")
text_editor.write_text(" Morning")

hist.save_state(text_editor.save())

#print(hist.get_mementos())

new_memento : TextMemento = hist.undo()
text_editor.restore(new_memento)

print(text_editor.get_text())