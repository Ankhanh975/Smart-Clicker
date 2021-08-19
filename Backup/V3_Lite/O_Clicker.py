import win32api, win32con
import time 
from O_Global import *
from Sub_Method import *
import Vector2d
import resorce

#TODO: O_Clicker cuold generale to all pressable key in keyboard
def fastclick(Global_MousePos, button, x=None, y=None, duration = 0.005): #Click
	def __Click(_ButtonDown: int, duration, _ButtonUp: int):
		win32api.mouse_event(_ButtonDown,0,0)
		Sleep(duration) 
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


class O_Clicker(Base): #TODO
	def __init__(self, tName="", tTPS=1, tbutton="left"):
		
		super().__init__(str(tName))
		self.x=None
		self.y=None
		self.button = str(tbutton)

		self.TPS = float(tTPS)
		self.PosPrecise = 3 #pixels

		self.lastClick = time.perf_counter()
		self.NextClickTime = time.perf_counter()
		self.DelayToNextClick = 1/self.TPS

	def Update(self, Global_HoldKey, Global_MousePos, Global_ActiveWindow):
		super().Update(Global_HoldKey, Global_MousePos, Global_ActiveWindow)
		
		self.DelayToNextClick = 1/self.TPS
		if time.perf_counter() >= self.NextClickTime:
			while time.perf_counter() - self.NextClickTime >= self.DelayToNextClick*5: # If more than 5 click are not clicked
				print(self.name+" Unable to click that fast: Remove " +str(3)+ " click.")
				self.NextClickTime += (self.DelayToNextClick*5 ) #TODO

			self.Event(Global_HoldKey, Global_MousePos, Global_ActiveWindow)
			self.NextClickTime+= self.DelayToNextClick*1.009
	

	def Event(self, Global_HoldKey, Global_MousePos, Global_ActiveWindow):
		if super().Event(Global_HoldKey, Global_MousePos, Global_ActiveWindow)==False:
			return

		if self.PosPrecise>0:
			if self.x !=None: #and self.y !=None:
				ClickPos = Vector2d.Vector(self.x, self.y)
			else:
				ClickPos = Vector2d.Vector(Global_MousePos)

			ClickPosRandom = Vector2d.Vector.random(size=self.PosPrecise)
			#print(ClickPos.x, ClickPos.y, ClickPosRandom.x, ClickPosRandom.y)
			ReadClick = ClickPos+ClickPosRandom
			fastclick(Global_MousePos, x=int(ReadClick.x-self.PosPrecise/2), y=int(ReadClick.y-self.PosPrecise/2), button=self.button)

		else:
			fastclick(Global_MousePos, x=self.x, y=self.y,  button = self.button)

	def MesereTPS(self): #TODO
		return 0

if __name__ == '__main__':
	flags, hcursor, Global_MousePos = win32gui.GetCursorInfo()
	for x in range(50):
		flags, hcursor, Global_MousePos = win32gui.GetCursorInfo()
		time.sleep(1/30)
		print(Global_MousePos)
		fastclick(Global_MousePos, "middle", Global_MousePos[0]+100, Global_MousePos[1]+100)