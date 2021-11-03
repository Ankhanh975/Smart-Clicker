import minecraftAPI
import winAPIOut
import winAPIIn
from _main import *
from win32api import keybd_event
from threading import Thread
from Lib import _List
import win32con
import win32gui
from time import perf_counter, sleep
from os import system as OsCmd


def LeftClick():
    # print("LeftClick")

    if not minecraftAPI.isFocused():
        return
    elif "mbutton" not in winAPIIn.getMouseState():
        return
    print("==")
    winAPIOut.fastclick()


def RightClick():
    # print("RightClick")
    if not minecraftAPI.isFocused():
        return
    elif winAPIIn.getKeyState(0x43) == None:
        # If "c" is not pressed
        return
    print("++")

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
            eval(a)


def init():
    def resizeConsole():
        winSize = (500, 300)
        hwnd = win32gui.FindWindow(None, "Auto Clicker")
        x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
        win32gui.MoveWindow(hwnd, x0, y0,
                            winSize[0], winSize[1], True)
    OsCmd("title "+"Auto Clicker")
    OsCmd("color 2d")
    resizeConsole()


def more():
    print("more...")
    
    # run 30 time a second
    if winAPIIn.getKeyState(0x73) != None:
        # Pressed F4
        print("Press F4 to continue...")
        id1.stop()
        id2.stop()
        id3.stop()
        id4.stop()
        id5.stop()
        return
    else:
        print("more...")
        OsCmd("cls")
        print(id1.FPS, id2.FPS)
        
    if not minecraftAPI.isFocused():
        return
    elif winAPIIn.getKeyState(0x4C) and winAPIIn.getKeyState(0xA2):

        # Login to server 3fmc.com
        minecraftAPI.chat("/l ak2006@@")
        sleep(1/3.5)
        winAPIOut.fastclick("lbutton")
        sleep(1/60)
    else:
        numpad = [0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69]
        for keyCode in numpad:
            if winAPIIn.getKeyState(keyCode):
                minecraftAPI.chat(":)")
                # release key pressed
                keybd_event(keyCode, 0, win32con.KEYEVENTF_KEYUP, 0)
                sleep(1/30)
                keybd_event(keyCode, 0, win32con.KEYEVENTF_KEYUP, 0)


log = []


def onChatMessage(text):
    print(text)


init()
id1 = setInterval(LeftClick, 1000/17.5, randomMs=1000/14.5-1000/17.5)
id2 = setInterval(RightClick, 1000/15, randomMs=1000/15-1000/13)
id3 = setInterval(zoom, 16.6)
id4 = setInterval(more, 33.3)
id5 = minecraftAPI.onChatMessage(onChatMessage)
Thread(target=console, daemon=True).start()
