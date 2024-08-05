import tkinter
import os

from pyform.utils.attributes import Size

class Form:
    """ Base Class For All UI Classes """

    def __init__(self, title = 'PyForm'):
        self.form = tkinter.Tk()
        self.set_caption(title)
    
    def set_caption(self, title):
        """ Set Title On The Top Left Of Form """

        self.title = title
        self.form.title(title)

    def set_icon(self, icon):
        """ Set Icon On The Top Left Of Form """

        if not os.path.isabs(icon):
            icon = os.path.join(os.getcwd(), icon)
        
        if os.path.exists(icon):
            self.form.iconbitmap(os.path.join(os.getcwd(), icon))
            self.icon = icon
        
        else:
            raise FileNotFoundError

    def set_size(self, width, height):
        self.size = Size(width, height)
        self.form.geometry(f'{width}x{height}')

    def set_bg(self, bg):
        """ Set Back Ground Color """

        self.bg = bg
        self.form.config(bg = '#%02x%02x%02x' % bg)

    def update(self):
        """ Draw Changes On Form """

        self.form.update()
        self.form.update_idletasks()

    def destroy(self):
        """ Delete Form """

        self.form.destroy()
        self.form.quit()