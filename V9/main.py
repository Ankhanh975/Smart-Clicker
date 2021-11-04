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
from response import onChatMessage

lastLeftClick = perf_counter()
lastRightClick = perf_counter()

def LeftClick():
    global lastLeftClick
    # print("LeftClick")

    if not minecraftAPI.isFocused():
        return
    elif "mbutton" not in winAPIIn.getMouseState():
        return
    lastLeftClick = perf_counter()
    winAPIOut.fastclick()


def RightClick():
    global lastRightClick
    # print("RightClick")
    if not minecraftAPI.isFocused():
        return
    elif winAPIIn.getKeyState(0x43) == None:
        # If "c" is not pressed
        return
    lastRightClick = perf_counter()
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
        a = input(">>> ")
        a = a.lstrip().rstrip()
        if a != "":
            try:
                x = eval(a)
                print(x)
            except Exception as p:
                print(p)


def init():
    try:
        from sys import exit as ThreadExit

        def resizeConsole(winSize=(500, 300)):
            hwnd = win32gui.FindWindow(None, "Auto Clicker")
            x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
            win32gui.MoveWindow(hwnd, x0, y0,
                                winSize[0], winSize[1], True)
        resizeConsole()
        if "Auto Clicker" in winAPIIn.getWindowNames():
            # anthor instance is running
            O_Sound.ErrorSound.play()
            OsCmd("color c7")
            OsCmd("mode con cols=30 lines=6")

            print("Already open this program.")
            sleep(4)
            ThreadExit()  # Stop everything because no thread started yet

        OsCmd("title "+"Auto Clicker")
        OsCmd("color 2d")

    except Exception as p:
        pass


ConsoleScreen = ""


def more():
    global ConsoleScreen
    # run 30 time a second
    if winAPIIn.getKeyState(0x73) != None:
        # Pressed F4

        print("Press F4 to continue...")
        O_Sound.ExitSound.play()
        for id in (id1, id2, id3, id4, id5):
            id.stop()

        return
    else:
        line1 = minecraftAPI.isFocused()
        if line1 == True:
            if perf_counter()-lastLeftClick < 0.1:
                line2 = f" |LClick| {id1.FPS} CPS | \n"
            else:
                line2 = f" |LClick|  0 CPS | \n"

            if perf_counter()-lastRightClick < 0.1:
                line3 = f" |RClick| {id2.FPS} CPS | \n"
            else:
                line3 = f" |RClick|  0 CPS | \n"
        else:
            line2 = line3 = "\n"
        line1 = f" |Focus |  {line1}  | \n"

        newFrame = "\n"
        newFrame += line1
        newFrame += line2
        newFrame += line3
        newFrame += ">>> "

        if newFrame != ConsoleScreen:
            ConsoleScreen = newFrame
            # OsCmd("cls")
            print(newFrame, end="")

    if not minecraftAPI.isFocused():
        return
    elif winAPIIn.getKeyState(0x4C) and winAPIIn.getKeyState(0xA2):

        # Login to server 3fmc.com
        minecraftAPI.chat("/l ak2006@@", RePress=False)

    else:
        from response import WhatToChat

        numpad = [0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69]
        for keyCode in numpad:
            if winAPIIn.getKeyState(keyCode):
                print("Got key: ", keyCode)
                whatToChat = WhatToChat(keyCode-0x60)
                print("whatToChat", whatToChat)
                minecraftAPI.chat(whatToChat)
                # release key pressed
                keybd_event(keyCode, 0, win32con.KEYEVENTF_KEYUP, 0)
                sleep(1/30)
                keybd_event(keyCode, 0, win32con.KEYEVENTF_KEYUP, 0)


init()
id1 = setInterval(LeftClick, 1000.0/17.5, randomMs=1000/14.5-1000/17.5)
id2 = setInterval(RightClick, 1000.0/15, randomMs=1000/13-1000/15)
id3 = setInterval(zoom, 16.6)
id4 = setInterval(more, 33.3)
id5 = minecraftAPI.onChatMessage(onChatMessage)
Thread(target=console, daemon=True).start()
