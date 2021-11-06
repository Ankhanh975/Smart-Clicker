from win32api import keybd_event
from AI import predict
import cv2
import os
import winAPIIn
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
            # print(x)

            before = os.listdir("D:/Bi/Record/")
            # beforeLength = len(before)
            # os.remove(newFile)
            return x

    print("done")
    return


def more():
    if winAPIIn.getKeyState(0x71):
        start = perf_counter()
        keybd_event(0x71, 0, win32con.KEYEVENTF_KEYUP, 0)
        getInventoryPos()
        keybd_event(0x71, 0, win32con.KEYEVENTF_KEYUP, 0)
        end = perf_counter()
        print(end-start)
        sleep(0.2)


id4 = setInterval(more, 33.3, blocking=True)
