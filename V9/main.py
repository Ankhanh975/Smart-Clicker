# cd C:\src\Python\Smart Clicker\V9 && py "C:\src\Python\Smart Clicker\V9\main.py"

import minecraftAPI
import winAPIOut
import winAPIIn
from _main import *
from win32api import keybd_event
from threading import Thread
import win32con
from time import perf_counter, sleep
from os import system as OsCmd
from chat import onChatMessage
import sys
# sys.stdout = open("log.txt", 'a')
# sys.stderr = open("log.txt", 'a')

lastLeftClick = perf_counter()
lastRightClick = perf_counter()


def LeftClick():
    global lastLeftClick
    # print("LeftClick")

    if not minecraftAPI.isFocused():
        id1.FPS = 10
    elif not winAPIIn.getKeyState(0x04):
        # If "mbutton" is NOT pressed
        id1.FPS = 120
    else:
        id1.FPS = 17
        lastLeftClick = perf_counter()
        winAPIOut.fastclick()
        
    while True:

        sleep(1/120)
        if winAPIIn.getKeyState(0x04):
            if minecraftAPI.isFocused():
                break

    
def LeftClick():
    global lastLeftClick
    # print("LeftClick")

    if not minecraftAPI.isFocused():
        return
    while True:
        # If "mbutton" is NOT pressed

        sleep(1/120)
        if winAPIIn.getKeyState(0x04):
            if minecraftAPI.isFocused():
                break

    lastLeftClick = perf_counter()
    winAPIOut.fastclick()

def RightClick():
    global lastRightClick
    # print("RightClick")
    if not minecraftAPI.isFocused():
        return
    while True:
        # If "c" is not pressed
        sleep(1/120)
        if winAPIIn.getKeyState(0x43):
            if minecraftAPI.isFocused():
                break
    lastRightClick = perf_counter()
    winAPIOut.fastclick(button="rbutton")
# def LeftClick():
#     global lastLeftClick
#     # print("LeftClick")

#     if not minecraftAPI.isFocused():
#         return
#     elif "mbutton" not in winAPIIn.getMouseState():
#         return
#     lastLeftClick = perf_counter()
#     winAPIOut.fastclick()


# def RightClick():
#     global lastRightClick
#     # print("RightClick")
#     if not minecraftAPI.isFocused():
#         return
#     elif winAPIIn.getKeyState(0x43) == None:
#         # If "c" is not pressed
#         return
#     lastRightClick = perf_counter()
#     winAPIOut.fastclick(button="rbutton")


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
    from sys import exit as ThreadExit
    from win32gui import FindWindow, GetWindowRect, MoveWindow

    def resizeConsole(winSize=(500, 300)):
        hwnd = FindWindow(None, "Auto Clicker")
        x0, y0, x1, y1 = GetWindowRect(hwnd)
        MoveWindow(hwnd, x0, y0, winSize[0], winSize[1], True)

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
    resizeConsole()


ConsoleScreen = ""


def more():
    global ConsoleScreen
    # run 30 time a second
    if winAPIIn.getKeyState(0x73) != None:
        # Pressed F4
        O_Sound.ExitSound.play()

        print("Press F4 to continue...")
        for id in (id1, id2, id3, id4, id5):
            id.stop()
        # sleep(7/60)
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

        if newFrame != ConsoleScreen:
            ConsoleScreen = newFrame
            # OsCmd("cls")
            print(newFrame, end="")

    if not minecraftAPI.isFocused():
        return
    elif winAPIIn.getKeyState(0x4C) and winAPIIn.getKeyState(0xA2):
        # Ctrl+L
        print("Login to server 3fmc.com")
        minecraftAPI.chat("/l ak2006@@", RePress=False)
    elif winAPIIn.getKeyState(0x71):
        # F2
        # sleep(7/1000.0)
        pass
        # minecraftAPI.getInventoryPos()

    else:
        from chat import WhatToChat

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
                sleep(0.2)


id1 = setInterval(LeftClick, 1000.0/18.5, randomMs=1000/14.5-1000/17.5)
id2 = setInterval(RightClick, 1000.0/16, randomMs=1000/13-1000/15)
id3 = setInterval(zoom, 16.6)
id4 = setInterval(more, 33.3, daemon=False)
id5 = minecraftAPI.onChatMessage(onChatMessage)
# Thread(target=console, daemon=True).start()
init()


def AI():
    import item


Thread(target=AI, daemon=True).start()
O_Sound.StartSound.play()
