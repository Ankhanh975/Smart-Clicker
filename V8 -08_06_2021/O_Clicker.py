import _List, win32api, win32con
import resorce
def fastclick(GlobalInput, button = "lbutton", x=None, y=None, duration = 0.005): #Click with VK_CODE, x and y use only for mouse_event
	def __Click(_ButtonDown: int, duration, _ButtonUp: int):
		win32api.mouse_event(_ButtonDown,0, 0)
		resorce.Sleepp(duration) 
		win32api.mouse_event(_ButtonUp, 0, 0)

	def press(CODE, duration):
	    win32api.keybd_event(CODE, 0, 0, 0)
	    resorce.Sleepp(duration)
	    win32api.keybd_event(CODE, 0, win32con.KEYEVENTF_KEYUP ,0)

	if button.lower() == "lbutton":
		_ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
	elif button.lower() == "rbutton":
		_ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP
	elif button.lower() == "mbutton":
		_ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_MIDDLEDOWN, win32con.MOUSEEVENTF_MIDDLEUP
	else:
		press(_List.VK_CODE[button], duration)
		return
		
	if (not x==None) and (not (x,y) == GlobalInput.Global_MousePos):
		win32api.SetCursorPos((x,y))
		__Click(_ButtonDown, duration, _ButtonUp)
		win32api.SetCursorPos(GlobalInput.Global_MousePos)
	else:
		__Click(_ButtonDown, duration, _ButtonUp)


