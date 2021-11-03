# Interact with Minecraft 1.8.9
import numpy as np
import winAPIOut
import winAPIIn
from win32api import keybd_event
from time import perf_counter, sleep
from Lib import _List
import win32con


class OnChatMessage():
    file = "C:/Users/Admin/AppData/Roaming/.minecraft/logs/latest.log"
    sleepTime = 0
    stop = False

    def __init__(self, callback):
        self.line = ""
        self.callback = callback

    def start(self):
        with open(self.file, "r") as self.f:
            while (not self.stop):
                sleep(self.sleepTime)
                self.line = self.f.readline()

                if self.line != "":
                    self.sleepTime = 0
                    if "[Client thread/INFO]: [CHAT]" in self.line:

                        self.line = self.line.replace(
                            "[Client thread/INFO]: [CHAT]", "")
                        self.line = self.line.replace("\n", "")
                        self.callback(self.line)
                elif self.line == "":
                    # Sleep for 1/40 seconds if not reading anything new.
                    self.sleepTime = 1/40


def isFocused():
    # if "Minecraft 1.8.9" in winAPIIn.getActiveWindowName():
    if "V9" in winAPIIn.getActiveWindowName():
        return True
    else:
        return False


def chat(self, text="."):
    # Type text: str to Minecraft console
    # Release all potentiality key can mess thing up
    KeyboardState = winAPIIn.getKeyboardState()
    for i in winAPIIn.getKeyboardState():
        winAPIOut.Sleepp(1/500)

        try:
            keybd_event(
                _List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
        except KeyError as p:
            print(p)
    # Open chat
    winAPIOut.press("/")
    # Sleep so minecraft can progress
    winAPIOut.Sleepp(1/20)
    if text == -1:
        # -1 = last command send
        winAPIOut.press("up_arrow")
        winAPIOut.Sleepp(1/500)

    elif type(text) == str:
        # Open chat
        if text[0] == "/":
            text = text[1:]
            winAPIOut.typer(text)
        else:
            winAPIOut.Sleepp(0.004)
            winAPIOut.press("backspace")
            winAPIOut.Sleepp(1/500)
            winAPIOut.typer(text)

    # Close chat
    winAPIOut.press("enter")
    winAPIOut.Sleepp(1/25)

    # press back Released key
    for i in KeyboardState:
        winAPIOut.Sleepp(1/500)
        try:
            keybd_event(_List.VK_CODE[i], 0, 0, 0)
        except KeyError as p:
            print(p)


def takeScreenShot(self):
    # Need Bandicam to take a screenshot in full screen mode
    #
    return np.array(1920, 1080)
