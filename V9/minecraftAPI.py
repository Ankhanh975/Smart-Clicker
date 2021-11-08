# Interact with Minecraft 1.8.9
import winAPIOut
import winAPIIn
from win32api import keybd_event
from time import sleep
from Lib import _List
import win32con
from threading import Thread
from _main import setInterval, setTimeout


class onChatMessage():
    file = "C:/Users/Admin/AppData/Roaming/.minecraft/logs/latest.log"

    def __init__(self, callback):
        self.line = ""
        self.callback = callback
        Thread(target=self.loop).start()
        try:
            self.f = open(self.file, "r")
        except Exception as p:
            print(p)
            return
        self.id = setInterval(self.loop, 1000.0/40)

    def loop(self):
        try:
            self.line = self.f.readline()

            # Sleep for 1/40 seconds if not reading anything new.
            while self.line != "":
                if "[Client thread/INFO]: [CHAT]" in self.line:

                    self.line = self.line.replace(
                        "[Client thread/INFO]: [CHAT]", "")
                    self.line = self.line.replace("\n", "")
                    self.line = self.line[12:]
                    self.callback(self.line)
                self.line = self.f.readline()
        except Exception as p:
            print("pp ", p)

    def stop(self):
        self.f.close()
        self.id.stop()


def isFocused():
    if "Minecraft 1.8.9" in winAPIIn.getActiveWindowName():
        return True

    elif "V9" == winAPIIn.getActiveWindowName():
        return True
    else:
        return False


def chat(text=".", RePress=True):
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

    if RePress == True:
        # press back Released key
        for i in KeyboardState:
            winAPIOut.Sleepp(1/500)
            try:
                keybd_event(_List.VK_CODE[i], 0, 0, 0)
            except KeyError as p:
                print(p)
