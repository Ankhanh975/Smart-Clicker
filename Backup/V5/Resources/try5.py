import win32gui, time

for a in range(1000):
    time.sleep(1/60)
    hwnd = win32gui.FindWindow(None, "Untitled - Notepad")
    win32gui.MoveWindow(hwnd, int(10+a/3), int(10+a/2), 500, 500, True)