from tkinter.constants import E
from .key import keyboard, mouse
from .utils.settings import Settings

import os
import sys
import json
import time
from tkinter import messagebox


sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))


apps = {}


def add(app, name, settings=None):
    """ Adds Program Into Apps """

    global apps

    apps[name] = app

    if not settings:
        settings = os.path.join('ui', name, 'settings.json')

    with open(os.path.join(os.getcwd(), settings), 'r') as settings_file:
        app.settings = Settings(json.load(settings_file))

    app.run = False


def remove(name):
    global apps
    del apps[name]


def update():
    global apps

    for name, app in apps.items():
        if app.run:
            if hasattr(app, 'destroy_next_frame') and app.destroy_next_frame:
                apps[name].destroy()
                apps[name].run = False
                continue

            if hasattr(app, 'update'):
                app.update()

            update_form(app.form)
            handle_hotkeys(app)

            time.sleep(1 / app.settings.INTERVAL)


def mainloop():
    global apps

    while any([app.run for app in apps.values()]):
        update()


def run(name):
    """ Runs The Program With Selected Name """

    global apps

    app = apps[name] = apps[name]()

    app.set_caption(app.settings.TITLE)
    app.set_size(app.settings.SIZE[0], app.settings.SIZE[1])
    app.set_icon(app.settings.ICON)
    app.set_bg(app.settings.BACKGROUND)

    if hasattr(app, 'start'):
        app.start()

    app.run = True


def quit(name):
    """ Quits From Program With Selected Name """

    global apps

    apps[name].destroy_next_frame = True

    if hasattr(apps[name], 'end'):
        apps[name].end()


def handle_hotkeys(app):
    """ To Handle Whether The User Uses KeyWord """

    keys = keyboard.pressed_keys()

    if hasattr(app, 'keydown'):
        for special_key in keyboard.special.values():
            if special_key in keys and not 'click' in special_key:
                for i in range(len(keys)):
                    app.keydown('-'.join(keys))
                    keys.insert(0, keys.pop(-1))

                return

        if keys and (key := keys[0]):
            app.keydown(key)
            return

    if hasattr(app, 'mousedown') and keys and 'click' in (key := keys[0]):
        app.mousedown(key.replace('click', ''), mouse.cursor_pos())


def update_form(form):
    form.update()
    form.update_idletasks()


def ask(message):
    return messagebox.askyesno(message)


def message(message):
    return messagebox.showinfo(message)