# Interact with Minecraft 1.8.9
import numpy as np
import winAPIOut
import winAPIIn
from win32api import keybd_event
from time import perf_counter


class OnChatMessage():
    file = "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log"
    sleepTime = 0
    stop = False

    def __init__(self):
        self.id = []
        self.chatHistory = []
        # self.chatHistory.append(text)

    def addListener(self, callback):
        self.id.append(id(callback))

    def hasListener(self, callback):
        if (id(callback) in self.id):
            return True
        else:
            return False

    def removeListener(self, callback):
        self.id.remove(id(callback))
    # callback(self.chat)


class Minecraft:
    def __init__(self):
        self.onChatMessage = OnChatMessage()

    def isFocused():
        if "Minecraft 1.8.9" in winAPIIn.getActiveWindowName():
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
        return np.array(1920, 1080)


minecraft = Minecraft()


def onChatMessage(self):
    print("onChatMessage", self.text)
    print("onChatMessage", self.history)


minecraft.onChatMessage.addListener(onChatMessage)
