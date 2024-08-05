from attributes import Point, Size
import tkinter


class TextWidget:
    """ Base For All Widgets """

    def __init__(self):
        self.size = Size()
        self.position = Point()

        self.place(0, 0)
    
    def set_text_var(self, text=''):
        self.__text__ = tkinter.StringVar()
        self.__base__.config(textvariable=self.__text__)
        
        self.set_text(text)

    def place(self, x = None, y = None):
        """ Locate Widget On Selected Place """

        if not x:
            x = self.position.x
        else:
            self.position.x = x

        if not y:
            y = self.position.y
        else:
            self.position.y = y

        self.__base__.place(x=x, y=y)

    def delete(self):
        """ Delete Widget From Form """
        self.__base__.place_forget()

    def set_size(self, width=None, height=None):
        """ Set Size Of Widget """

        if not width:
            width = self.size.width
        else:
            self.size.width = width

        if not height:
            height = self.size.height
        else:
            self.size.height = height

        self.__base__.config(width=width, height=height)

    def scale(self):
        """ Returns Size Of Widget """
        return (self.size.width, self.size.height)
    
    def coordinates(self):
        """ Returns Coordinates Of Widget """
        return (self.position.x, self.position.y)

    def set_text(self, text):
        """ Sets New Text To Widget """
        if hasattr(self, '__text__'):
            self.__text__.set(text)

    def add_text(self, text):
        """ Add Some Text To Widget's Text """
        if hasattr(self, '__text__'):
            self.__text__.set(self.__text__.get() + text)

    def reset_text(self):
        """ Resets Widget's Text """
        if hasattr(self, '__text__'):
            self.set_text('')

    def text(self):
        """ Returns Widget's Text """
        return self.__text__.get().strip()
