import time, pygame
import cv2
import mss
import numpy

class WindowCapture: #Full screen recording
    w = 0
    h = 0
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
    def __init__(self, window_name=None):
        pass

    def get_screenshot(self):
        with mss.mss() as sct:
            img = numpy.array(sct.grab(self.monitor))
        return img


    def setCrop(self, topLeft, buttomRight):
        self.monitor["top"] = topLeft[0]
        self.monitor["left"] = topLeft[1]
        self.monitor["width"] = abs(topLeft[0] - buttomRight[0])
        self.monitor["height"] = abs(topLeft[1] - buttomRight[1])
        


import cv2 as cv
import numpy as np
import os
import time, pygame

clock = pygame.time.Clock()

class GetMinecraftActiveSlot:
    slot = None # 1->9, None

    def __init__(self):
        self.Obj = WindowCapture()
        self.Obj.setCrop((600,1070), (1320,1071))

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

        #if self.slot != None:
        cv.imshow('Computer Vision', screenshot)

        return self.slot


slot = GetMinecraftActiveSlot()

while True:
    clock.tick(60)

    print(slot.get())
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    #print(clock.get_fps())
