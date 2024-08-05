import tkinter
from .base import TextWidget

class Button(TextWidget):
    def __init__(self, master, text='', **argv):
        self.__base__ = tkinter.Button(master, text=text)
        self.command = None

        if command := argv.get('command'):
            self.onClick(command)

        TextWidget.__init__(self)
        TextWidget.set_text_var(self, text)

    def on_click(self, command):
        """ Command, That Will Be Called On Button Click """

        self.__base__.config(command=command)
        self.command = command


