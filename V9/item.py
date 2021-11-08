import re
from win32api import keybd_event
from AI import predict
import cv2
import os
import winAPIIn
import minecraftAPI
import winAPIOut
import win32api
from _main import *
import win32con
from time import perf_counter, sleep

before = os.listdir("D:/Bi/Record/")
# beforeLength = len(before)
PATH = os.path.join(os.getenv('APPDATA'), ".minecraft/screenshots")


def getInventoryPos():
    global before, beforeLength
    print("start")
    for i in range(50):
        sleep(1/200)
        # sleep(10/200)
        now = os.listdir("D:/Bi/Record/")
        newFile = set(now) - set(before)
        if len(newFile) != 0:
            newFile = tuple(newFile)
            for index in newFile:
                newFile = index
                if newFile not in now or not newFile.endswith("jpg"):
                    continue
                else:
                    break

            print(i, newFile)
            newFile = os.path.join("D:/Bi/Record/", newFile)
            img = cv2.imread(newFile)
            if type(img) == type(None):
                continue
            x = predict.model(img)
            print(newFile)

            before = os.listdir("D:/Bi/Record/")
            # beforeLength = len(before)
            # os.remove(newFile)
            return x

    print("done")
    return


def click(x, y):
    PosOfEachSlot = [[[671, 577], [746, 581], [819, 582], [891, 585], [955, 579],
                      [1039, 581], [1084, 582], [1174, 580], [1241, 575]],
                     [[676, 634], [741, 639], [815, 644], [908, 636], [964, 638],
                      [1043, 648], [1115, 648], [1174, 648], [1243, 645]],
                     [[665, 716], [751, 723], [813, 719], [908, 718], [959, 724],
                      [1032, 714], [1108, 724], [1187, 736], [1232, 727]],
                     [[674, 813], [742, 811], [823, 806], [890, 810], [967, 818],
                      [1029, 823], [1103, 819], [1171, 818], [1236, 815]]]

    x, y = PosOfEachSlot[x][y]
    win32api.SetCursorPos((x, y))
    winAPIOut.fastclick(duration=1.0/150)


def more():
    if winAPIIn.getKeyState(0x71):
        if not minecraftAPI.isFocused():
            return
        # start = perf_counter()
        # end = perf_counter()
        # print("Done in: ", end-start)
        keybd_event(0x71, 0, win32con.KEYEVENTF_KEYUP, 0)
        keybd_event(0xA0, 0, 0, 0)
        sleep(1/30)
        found = getInventoryPos()
        if type(found) == type(None):
            print("found=None")
            keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
            
            return
        print(found)
        now = winAPIIn.getPos()
        

        for x, row in enumerate(found):
            for y, item in enumerate(row):
                if int(item) in [5, 8, 27, 28]:
                    print("click", item)
                    click(x, y)
                    sleep(1/200)
        
        print("release shift")
        
        sleep(0.1)
        keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
        # win32api.SetCursorPos(now)
        win32api.SetCursorPos((1920//2, 1080//2))
        sleep(0.49)


O_Sound.ErrorSound.play()
id = setInterval(more, 33.3, blocking=True)


# 32 la bàn / 157
