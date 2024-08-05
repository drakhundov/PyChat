import tkinter
from .base import TextWidget

class Label(TextWidget):
    """ Just Text To Show """

    def __init__(self, master, text=''):
        self.__base__ = tkinter.Label(master, text=text)

        TextWidget.__init__(self)
        TextWidget.set_text_var(self, text)