
'''
#Scroll one up
win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, 1, 0)

#Scroll one down
win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0)'''


import _List, win32api, win32con
import Sub_Method
def fastclick(GlobalInput, button = "lbutton", x=None, y=None, duration = 0.005): #Click with VK_CODE, x and y use only for mouse_event
	def __Click(_ButtonDown: int, duration, _ButtonUp: int):
		win32api.mouse_event(_ButtonDown,0, 0)
		Sub_Method.Sleep(duration) 
		win32api.mouse_event(_ButtonUp, 0, 0)

	def press(CODE, duration):
	    win32api.keybd_event(CODE, 0, 0, 0)
	    Sub_Method.Sleep(duration)
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
'''
import Vector2d, time
from O_Global import *

class O_Clicker(Base): #TODO
	def __init__(self, tName="", tTPS=1.0, tbutton="lbutton"):
		super().__init__(str(tName))
		self.x=None
		self.y=None
		self.button = str(tbutton)

		self.TPS = updateTPS(tTPS)
		self.PosPrecise = 3 #pixels

		self.lastClick = time.perf_counter()
		self.NextClickTime = time.perf_counter()

	def Update(self, GlobalInput):
		super().Update(GlobalInput)
		
		if time.perf_counter() >= self.NextClickTime:
			while time.perf_counter() - self.NextClickTime >= self.DelayToNextClick*5: # If more than 5 click are not clicked
				print(self.name+" Unable to click that fast: Remove " +str(3)+ " click.")
				self.NextClickTime += (self.DelayToNextClick*5 )

			self.Event(GlobalInput)
			self.NextClickTime+= self.DelayToNextClick*1.009
	
	def updateTPS(self, value):
		self.TPS = float(value)
		self.DelayToNextClick = 1/self.TPS

	def Event(self, GlobalInput):
		if super().Event(GlobalInput)==False:
			return

		if self.PosPrecise != 0:
			if self.x !=None: #and self.y !=None:
				ClickPos = Vector2d.Vector(self.x, self.y)
			else:
				ClickPos = Vector2d.Vector(GlobalInput.Global_MousePos)

			ClickPosRandom = Vector2d.Vector.random(size=self.PosPrecise)
			#print(ClickPos.x, ClickPos.y, ClickPosRandom.x, ClickPosRandom.y)
			ReadClick = ClickPos+ClickPosRandom
			fastclick(GlobalInput, x=int(ReadClick.x-self.PosPrecise/2), y=int(ReadClick.y-self.PosPrecise/2), button=self.button)

		else:
			fastclick(GlobalInput, x=self.x, y=self.y,  button = self.button)



class O_Clicker2(Base):
		x=None
		y=None
	def __init__(self, tName="", MinTPS=8.0, MaxTPS=12.0, tbutton="lbutton"):
		super().__init__(str(tName))
		self.button = str(tbutton)
		self.clock = pygame.time.Clock()
		self.PosPrecise = 3 #pixels

		self.MinTPS = float(MinTPS)
		self.MaxTPS = float(MaxTPS)


		self.delayMin = 1 / self.MinTPS
		self.delayMax = 1 / self.MaxTPS

		self.delay = random.uniform(self.delayMin, self.delayMax)

	def SetMinTPS(self, value):
		self.MinTPS = float(value)
		self.delayMin = 1 / self.MinTPS

		if self.MinTPS > self.MaxTPS:
			a = self.MinTPS
			self.MinTPS = self.MaxTPS
			self.MaxTPS = a

	def SetMaxTPS(self, value):
		self.MaxTPS = float(value)
		self.delayMax =1 / self.MaxTPS
		
		if self.MinTPS > self.MaxTPS:
			a = self.MinTPS
			self.MinTPS = self.MaxTPS
			self.MaxTPS = a

	def Update(self, GlobalInput):
		super().Update(GlobalInput)
		
		if time.perf_counter() >= self.NextClickTime:
			while time.perf_counter() - self.NextClickTime >= self.DelayToNextClick*5: # If more than 5 click are not clicked
				print(self.name+" Unable to click that fast: Remove " +str(3)+ " click.")
				self.NextClickTime += (self.DelayToNextClick*5 )

			self.Event(GlobalInput)
			self.NextClickTime+= self.DelayToNextClick*1.009
	def click(self, GlobalInput):
		if super().Event(GlobalInput)==False:
			return

		if self.PosPrecise != 0:
			if self.x !=None: #and self.y !=None:
				ClickPos = Vector2d.Vector(self.x, self.y)
			else:
				ClickPos = Vector2d.Vector(GlobalInput.Global_MousePos)

			ClickPosRandom = Vector2d.Vector.random(size=self.PosPrecise)
			#print(ClickPos.x, ClickPos.y, ClickPosRandom.x, ClickPosRandom.y)
			ReadClick = ClickPos+ClickPosRandom
			fastclick(GlobalInput, x=int(ReadClick.x-self.PosPrecise/2), y=int(ReadClick.y-self.PosPrecise/2), button=self.button)

		else:
			fastclick(GlobalInput, x=self.x, y=self.y,  button = self.button)

	def MesereClickTPS(self): #TODO
		return round(self.clock.get_fps(), 2)
'''
'''		
if __name__ == '__main__':
	flags, hcursor, Global_MousePos = win32gui.GetCursorInfo()
	for x in range(50):
		flags, hcursor, Global_MousePos = win32gui.GetCursorInfo()
		time.sleep(1/30)
		print(Global_MousePos)
		fastclick(Global_MousePos, "middle", Global_MousePos[0]+100, Global_MousePos[1]+100)'''