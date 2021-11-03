import minecraftAPI
import winAPIOut
import winAPIIn
from _main import *
from win32api import keybd_event
from threading import Thread
from Lib import _List
import win32con


def LeftClick():
    print("LeftClick")

    if not minecraftAPI.isFocused():
        return
    elif "mbutton" not in winAPIIn.getMouseState():
        return
    print("==", end=" ")
    winAPIOut.fastclick()


def RightClick():
    print("RightClick")
    if not minecraftAPI.isFocused():
        return
    elif winAPIIn.getKeyState(0x43) == None:
        # If "c" is not pressed
        return
    print("++", end=" ")

    winAPIOut.fastclick(button="rbutton")


inzoom = False


def zoom():
    global inzoom
    # print("minecraftAPI.isFocused()", minecraftAPI.isFocused())
    # Pressed both left and right mouse will press Z
    # will zoom if you setup: mod optifine and change active from C to Z
    if not minecraftAPI.isFocused():
        return
    MouseState = winAPIIn.getMouseState()
    if winAPIIn.isPressed(["lbutton", "rbutton"], MouseState):
        inzoom = True
        # print("inzoom = True")
        if winAPIIn.getKeyState(0x5A) == None:
            # print("Event pressed")
            keybd_event(0x5A, 0, 0, 0)
    elif inzoom == True:
        # print("inzoom = False")

        inzoom = False
        # print("Event release")
        keybd_event(0x5A, 0, win32con.KEYEVENTF_KEYUP, 0)


def console():
    # Make console still available to run commands
    while True:
        a = input("")
        a = a.lstrip().rstrip()
        if a != "":
            print(f"You input: {a}")

def onChatMessage(text):
    print(text)

# setInterval(LeftClick, 1000/17.5, randomMs=1000/14.5-1000/17.5)
# setInterval(RightClick, 1000/15, randomMs=1000/15-1000/13)
# setInterval(zoom, 1000.0/60)
# Thread(target=console, daemon=True).start()

log = []

x = minecraftAPI.OnChatMessage(onChatMessage)
Thread(target=x.start, daemon=True).start()