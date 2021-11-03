from win32gui import GetWindowText, GetForegroundWindow
from _main import *
import win32gui
import win32api
from Lib import _List


def getPos():
    return win32gui.GetCursorInfo()[2]


def getWindowNames():
    All = []

    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            Wintitle = win32gui.GetWindowText(hwnd)
            if Wintitle != "" and Wintitle not in All:
                if Wintitle not in ["Program Manager", "Settings"]:
                    All.append(Wintitle)
    win32gui.EnumWindows(winEnumHandler, None)
    return All


def getActiveWindowName():
    return GetWindowText(GetForegroundWindow())


def getMonitorSize():
    from ctypes import windll
    user32 = windll.user32
    screensize = user32.GetSystemMetrics(
        0), user32.GetSystemMetrics(1)
    return screensize


def getKeyState(x):
    a = win32api.GetKeyState(x)
    if a < 0 and _List.VK_CODE_REVERSE[x]:
        return _List.VK_CODE_REVERSE[x]


def getKeyboardState():
    Pressed = map(getKeyState, range(256))
    Pressed = filter(None, Pressed)
    Pressed = tuple(Pressed)
    return Pressed


def IsPressed(checkState, KeyboardState):
    # keyState: product of getKeyboardState()

    if (len(checkState) != len(KeyboardState)):
        return False
    elif set(checkState) == set(KeyboardState):
        return True
    else:
        return False
