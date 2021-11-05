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
        self.f = open(self.file, "r")
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


def takeScreenShot():
    Z = [(4, 4), (4, 76), (4, 148), (4, 220), (4, 292),
         (4, 364), (4, 436), (4, 508), (4, 580), (76, 4),
         (76, 76), (76, 148), (76, 220), (76, 292), (76, 364),
         (76, 436), (76, 508), (76, 580), (148, 4), (148, 76),
         (148, 148), (148, 220), (148, 292), (148, 364), (148, 436),
         (148, 508), (148, 580), (236, 4), (236, 76), (236, 148),
         (236, 220), (236, 292), (236, 364), (236, 436), (236, 508),
         (236, 580)]
    # Need Bandicam to take a screenshot when Minecraft in full screen mode
    from tensorflow.keras.models import load_model
    model = load_model("item_reader_seq.model")
    import numpy as np
    import cv2
    import os
    img = cv2.imread("D:/Bi/Record/javaw 2021-11-05 21-41-48-099.jpg")
    img = img[540:845, 636:1285]
    # img = img[480:845, 600:1285]

    Slot = []
    for x, y in Z:
        Slot.append(img[x:x+64, y:y+32])
        # Slot.append(img)

    for n in range(36):
        Slot[n] = cv2.resize(Slot[n], (32//4, 64//4), interpolation=cv2.INTER_AREA)
    
    model.predict(X)