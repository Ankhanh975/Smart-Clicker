import time
import winAPIIn
import win32gui
import win32api
from win32con import *

for x in range(55):
    time.sleep(0.2)
    x = winAPIIn.getPos()
    hwnd = win32gui.WindowFromPoint(x)
    y = win32gui.GetForegroundWindow()
    print(x, y)
    if x != y:
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SetActiveWindow(hwnd)
        win32gui.SetWindowPos(hwnd, HWND_TOP, 0, 0, 0, 0,
                              SWP_SHOWWINDOW | SWP_NOMOVE | SWP_NOSIZE)
        
    #     rectX = win32gui.GetWindowRect(x)
    #     rectY = win32gui.GetWindowRect(y)
    #     if rectY

# win32gui.SetWindowPos(x,
#     HWND_TOPMOST,
#     0,
#     0,
#     0,
#     0,
#     SWP_SHOWWINDOW|SWP_NOSIZE|SWP_NOMOVE
#     )
