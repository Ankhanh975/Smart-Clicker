from minecraftAPI import Minecraft
import winAPIOut
import winAPIIn
from _main import *
from win32api import keybd_event


def LeftClick():
    if not Minecraft.isFocused():
        return
    elif "mbutton" not in winAPIIn.getMouseState():
        return
    print("LeftClick")
    winAPIOut.fastclick()


def RightClick():
    if not Minecraft.isFocused():
        return
    elif winAPIIn.getKeyState(0x43) == None:
        # If "c" is not pressed
        return
    print("RightClick")
        
    winAPIOut.fastclick(button="rbutton")


inzoom = False


def zoom():
    # Pressed both left and right mouse will press Z
    # will zoom if you setup: mod optifine and change active from C to Z
    if not Minecraft.isFocused():
        return

    if winAPIIn.isPressed(["lbutton", "rbutton"]):
        inzoom = True
        if winAPIIn.getKeyState(0x5A) == None:
            keybd_event(0x5A, 0, 0, 0)
    elif inzoom == True:
        inzoom = False
        keybd_event(0x5A, 0, win32con.KEYEVENTF_KEYUP, 0)


setInterval(LeftClick, 1000/17.5, randomMs=1000/14.5-1000/17.5)
setInterval(RightClick, 1000/15, randomMs=1000/15-1000/13)
setInterval(zoom, 16.6)
