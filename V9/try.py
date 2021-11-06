from win32api import keybd_event
from AI import predict
import cv2
import os
import winAPIIn
from _main import *
import win32con
from time import perf_counter, sleep

before = os.listdir("D:/Bi/Record/")
beforeLength = len(before)


def getInventoryPos():
    global before, beforeLength
    print("start")
    sleep(5/200)
    for i in range(200):
        sleep(1/200)
        # sleep(10/200)
        now = os.listdir("D:/Bi/Record/")
        if len(now) != beforeLength:
            newFile = list(set(now) - set(before))[0]
            print(i, newFile)
            newFilePath = os.path.join("D:/Bi/Record/", newFile)
            img = cv2.imread(newFilePath)
            if type(img) == type(None):
                continue
            x = predict.model(img)
            print(x)

            before = os.listdir("D:/Bi/Record/")
            beforeLength = len(before)
            return x
    print("done")
    return


def more():
    if winAPIIn.getKeyState(0x71):
        start = perf_counter()
        getInventoryPos()
        end = perf_counter()
        print(end-start)
        keybd_event(0x5A, 0, win32con.KEYEVENTF_KEYUP, 0)


id4 = setInterval(more, 33.3, daemon=False)
