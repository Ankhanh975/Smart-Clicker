#from UserInput import *
import win32api, win32con 
import Lib.resorce
import Lib._List

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

class ClickerThread(RunThread):
	done = "Na"

	def __init__(self, name: str, FPS, Switch_Condition, Condition_Button: str, Event_Button: str):
		super().__init__(name, FPS)
		self.Switch_Condition = Switch_Condition
		self.Condition_Button = [Condition_Button]
		self.Event_Button = Event_Button

		self.Switch = UserInput.Switch(Switch_Condition)
		self.Switch._Event()

	def Stuff(self):
		self.Switch.Update(userInput)
		self.done = "Na"

		# if userInput.Global_OnActiveWindow != "Minecraft 1.8.9":
			# return
		#if not LogReader.allowClick:
		#	return
		if userInput.IsPressed(self.Condition_Button) and self.Switch.GetState()==True:
			if userInput.Global_OnActiveWindow == title:
				if userInput.IsPressed(self.Condition_Button) and self.Switch.GetState()==True:
					O_Sound.ClickSound.play()
					self.done = "Spam!"
				return
			else:
				self.done = "Clicked"
				O_Clicker.fastclick(UserInput, self.Event_Button)
	
	def WarningRelaese(self):
		pass
	def info(self):
		State= "On" if self.Switch.GetState() else "Off"
		State = f"({State})"
		#if userInput.Global_OnActiveWindow != "Minecraft 1.8.9" and State=="(On)":
		#	State= "On" if self.Switch.GetState() else "Off"
		#	State = "("+State+"| Outsize Minecraft"+")"
		#	return State, ""

		FPS = self.get_fps()
		FPS = f"{FPS} CPS"

		Done = "Done: " + (FPS if self.done=="Clicked" else self.done)
		if State=="(Off)":
			Done=""
		return State, Done