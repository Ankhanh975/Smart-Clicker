import win32api, win32con, win32gui
import pyautogui, keyboard
import time
from O_Control import *

pyautogui.FAILSAFE = False

def _sleep(duration): #High accurate sleep
	now = time.perf_counter()
	end = now + duration
	while now < end:
		if end-now >= 1/61:
			time.sleep(1/1000)
		now = time.perf_counter()

def fastclick(Global_MousePos, button = "left", x=None,y=None, duration = 0.005): #Click
	if button.lower() == "left":
		_ButtonDown = win32con.MOUSEEVENTF_LEFTDOWN
		_ButtonUp = win32con.MOUSEEVENTF_LEFTUP
	elif button.lower() == "right":
		_ButtonDown = win32con.MOUSEEVENTF_RIGHTDOWN
		_ButtonUp = win32con.MOUSEEVENTF_RIGHTUP
	elif button.lower() == "middle":
		_ButtonDown = win32con.MOUSEEVENTF_MIDDLEDOWN
		_ButtonUp = win32con.MOUSEEVENTF_MIDDLEUP
		

	if not x==None:
		win32api.SetCursorPos((x,y))

		win32api.mouse_event(_ButtonDown,0,0)
		_sleep(duration) 
		win32api.mouse_event(_ButtonUp,0,0)

		win32api.SetCursorPos(Global_MousePos)
	else:
		win32api.mouse_event(_ButtonDown,0,0)
		_sleep(duration) 
		win32api.mouse_event(_ButtonUp,0,0)

class O_Clicker(Base): #TODO
	def __init__(self, tName="", tTPS=1, tbutton="left"):
		super().__init__(str(tName))
		self.x=None
		self.y=None
		self.button = str(tbutton)
		self.TPS = int(tTPS)
		self.TimePrecise = int(0)
		self.PosPrecise = 0 #TODO
		self.ClickSound = 0
		self.ClickDuration = 0

		if self.TPS > 70:
			print(self.Name+ " Waring: >70 ClickPerSec might be overkill")
			tFPSMin = 70

		self.lastClick = time.perf_counter()

	def Update(self):
		super().Update()
		self.DelayToNextClick = self.TPS
		if time.perf_counter() >= self.NextClickTime - 0.0001:
			while time.perf_counter() - self.NextClickTime >= self.DelayToNextClick*5: # If more than 5 click are not clicked
				print(self.Name+" Unable to click that fast: Remove " +str(3)+ " click.")
				self.NextClickTime += (self.DelayToNextClick*3 )

				self.Event()
				self.NextClickTime = self.NextClickTime + self.DelayToNextClick*1.01  #TODO: understand why need this slower adjusted
	

	def Event(self, Global_MousePos):
		super().Event()
		fastclick(Global_MousePos, self.x, self.y, self.button)

	def MesereTPS(self): #TODO
		return 0
