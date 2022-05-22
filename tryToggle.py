from pynput.mouse import Listener
import win32api, win32con 
import time 

def fastclick(button, x=None, y=None, duration = 0.005, Global_MousePos=[]): #Click
    def __Click(_ButtonDown: int, duration, _ButtonUp: int):
        win32api.mouse_event(_ButtonDown,0,0)
        time.sleep(duration) 
        win32api.mouse_event(_ButtonUp,0,0)

    if button.lower() == "lbutton":
        _ButtonDown = win32con.MOUSEEVENTF_LEFTDOWN
        _ButtonUp = win32con.MOUSEEVENTF_LEFTUP
    elif button.lower() == "rbutton":
        _ButtonDown = win32con.MOUSEEVENTF_RIGHTDOWN
        _ButtonUp = win32con.MOUSEEVENTF_RIGHTUP
    elif button.lower() == "mbutton":
        _ButtonDown = win32con.MOUSEEVENTF_MIDDLEDOWN
        _ButtonUp = win32con.MOUSEEVENTF_MIDDLEUP
    else:
        resorce.press(button)
        return
        
    if not x==None:
        if not (x,y)==Global_MousePos:
            win32api.SetCursorPos((x,y))
            __Click(_ButtonDown, duration, _ButtonUp)
            win32api.SetCursorPos(Global_MousePos)
        else:
            __Click(_ButtonDown, duration, _ButtonUp)
    else:
        __Click(_ButtonDown, duration, _ButtonUp)
import time
while True:
    time.sleep(10)
    fastclick("lbutton")
    print("click")
# def on_click(x, y, button, pressed):
    
#     print(str(button))
#     if pressed:
#         if str(button)=="Button.right":
#             time.sleep(1/20)
#             fastclick("lbutton")


#     #return False # Stop listener

# # Collect events until released
# with Listener(
#         on_click=on_click) as listener:
#     listener.join()