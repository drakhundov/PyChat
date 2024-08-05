import tkinter
from .base import TextWidget

class Text(TextWidget):
    """ Text To Show, Or To Write Something """

    def __init__(self, master, width=100, height=100, only_to_show=False):
        self.__base__ = tkinter.Text(master)

        TextWidget.__init__(self)

        self.set_size(width, height)

        if only_to_show:
            self.set_state('disabled')
    
    def set_state(self, state):
        self.__base__.config(state=state)
    
    def set_text(self, text):
        self.set_state('normal')
        self.__base__.delete(0.0, 'end')
        self.__base__.insert(0.0, text)
        self.set_state('disabled')
    
    def add_text(self, text):
        self.set_text(self.text() + text)
    
    def reset_text(self):
        self.__base__.delete(0.0, 'end')
    
    def text(self):
        return self.__base__.get(1.0, 'end').strip()
