import numpy as np
import win32gui, win32ui, win32con

class WindowCapture: #Record a specific window even it's not on top
    #https://www.youtube.com/watch?v=WymCpVUPWQ4
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0

    def __init__(self, window_name=None):
        # find the handle for the window we want to capture

        if window_name!= None:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))

            window_rect = win32gui.GetWindowRect(self.hwnd)
            self.w = window_rect[2] - window_rect[0]
            self.h = window_rect[3] - window_rect[1]

            border_pixels = 8
            titlebar_pixels = 30
            self.w = self.w - (border_pixels * 2)
            self.h = self.h - titlebar_pixels - border_pixels
            self.cropped_x = border_pixels
            self.cropped_y = titlebar_pixels

        else:
            self.hwnd = None
            self.w, self.h = 1920, 1080
            window_rect = [0,0, 1920, 1080]

    def get_screenshot(self):
        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        self.cDC = dcObj.CreateCompatibleDC()
        self.dataBitMap = win32ui.CreateBitmap()
        self.dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        self.cDC.SelectObject(self.dataBitMap)
        self.cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)


        # convert the raw data into a format opencv can read
        self.dataBitMap.SaveBitmapFile(self.cDC, 'debug'+str(round(time.perf_counter(), 2))+'.bmp')
        signedIntsArray = self.dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        self.cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(self.dataBitMap.GetHandle())

        img = img[:, :, 0] # Just use red channel (besize 4 channel) in this case 
        img = np.ascontiguousarray(img)

        return img


    def setCrop(self, topLeft, buttomRight):
        self.w = abs(buttomRight[0] - topLeft[0])
        self.h = abs(buttomRight[1] - topLeft[1]) 
        self.cropped_x = topLeft[0]
        self.cropped_y = topLeft[1]





import cv2 as cv
import numpy as np
import os
import time, pygame

clock = pygame.time.Clock()

class GetMinecraftActiveSlot:
    slot = None # 1->9, None
    #slotPos = [(600, 1071), (680, 1071), (760, 1071), (840, 1071), (920, 1071), (1000, 1071), (1080, 1071), (1160, 1071), (1240, 1071), (1320, 1071)] 

    def __init__(self):
        self.Obj = WindowCapture("Minecraft 1.8.9")
        self.Obj.setCrop((0,0), (1320,1071))

        data = list(self.Obj.get_screenshot().shape)
        self.screenshotSize = [data[0], data[1]]

    def get(self):
        self.slot = None
        screenshot = self.Obj.get_screenshot()
        
        ShotFitler = screenshot > 130
        #

        for a in range(9):
            WhitePixel = np.count_nonzero(ShotFitler[0, 0+a*80:80+a*80])
            if WhitePixel / 80 > 0.7:
                self.slot = a + 1

        if self.slot != None:
            cv.imshow('Computer Vision', screenshot)

        return self.slot


slot = GetMinecraftActiveSlot()

while True:
    clock.tick(2)

    print(slot.get())

    
    #print(clock.get_fps())

















'''def list_window_names():
    # find all window you might interested in
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    All=[]
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            Wintitle = win32gui.GetWindowText(hwnd)
            if Wintitle !="" and Wintitle not in All:
                if Wintitle not in ["Program Manager", "Settings"]:
                    All.append(Wintitle)
    win32gui.EnumWindows(winEnumHandler, None)
    return All'''