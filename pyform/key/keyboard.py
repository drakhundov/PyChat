import win32api as windows
import json
import os

with open(os.path.join(os.path.dirname(__file__), 'keys.json'), 'r') as keys:
    special = json.load(keys)


def pressed_keys():
    """ Keys, That User Pressed """

    keys = []

    for i in range(1, 256):
        if windows.GetAsyncKeyState(i):
            if str(i) in special.keys():
                keys.append(special[str(i)])

    return keys


def is_pressed (key):
    """ Keys, Separated By '-'. If This Keys Is Pressed, Returns True, Else - False """

    pressed = pressed_keys()

    if '-' in key:
        keys = key.split('-')

        for key in keys:
            if not key.lower().replace(' ', '') in pressed:
                return False
        return True

    else:
        if key.lower() in pressed:
            return True
        else:
            return False
        
