import tkinter
from .base import TextWidget

class Input(TextWidget):
    """ Widget, Where User Could Input Something """

    def __init__(self, master, **argv):
        self.__base__ = tkinter.Entry(master)

        if argv.get('show'):
            self.__base__.config(show=argv['show'])

        TextWidget.__init__(self)
        TextWidget.set_text_var(self)
    
    def set_length(self, length):
        self.__base__.config(width=length)