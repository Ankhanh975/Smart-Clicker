import win32con, win32api	

def fastclick(button = "left", x=None,y=None, duration = 0.005): #Click
	if button == "left":
		  _ButtonDown = win32con.MOUSEEVENTF_LEFTDOWN
		  _ButtonUp = win32con.MOUSEEVENTF_LEFTUP
	elif button == "right":
		  _ButtonDown = win32con.MOUSEEVENTF_RIGHTDOWN
		  _ButtonUp = win32con.MOUSEEVENTF_RIGHTUP

	if not x==None:
		_MousePos = pyautogui.position()
		win32api.SetCursorPos((x,y))

		win32api.mouse_event(_ButtonDown,0,0)
		_sleep(duration) 
		win32api.mouse_event(_ButtonUp,0,0)

		win32api.SetCursorPos(_MousePos)
	else:
		win32api.mouse_event(_ButtonDown,0,0)
		_sleep(duration) 
		win32api.mouse_event(_ButtonUp,0,0)

class O_Clicker(Base): #TODO
	def __init__(self, tName, tTPS):
		self.Name = str(tName)
		self.ClickEvent = 
		self.TPS = int(tTPS)
		self.Condition = 
		self. = 
		self.TimePrecise = 
		self.PosPrecise = 
		self.ClickSound = 
		
	def Kill(self, )
class Click:
	NextClickTime = 0
	WasClicked=0
	def __init__(self , tFPS, tbutton="left", RandomInFPS=0, tx=None, ty=None, trandomInPos=0, ClickCondition=[], tName=""):
		tFPSMin = tFPS - RandomInFPS/2
		tFPSMax = tFPS + RandomInFPS/2

		if tFPSMin>tFPSMax:
			raise Exception("Not possible")

		if tFPSMin > 70:
			print(self.Name+ " Waring: Can't click faster than 70 ClickPerSec")
			tFPSMin = 70

		if tFPSMax > 70:
			print(self.Name+" Waring: Can't click faster than 70 ClickPerSec")
			tFPSMax = 70

		if tFPSMin>0:
			self.delayMin = 1.0/tFPSMin
		elif tFPSMin==0:
			self.delayMin = 100_000
		else:
			raise Exception(self.Name+" FPS can't be less than 0")

		if tFPSMax>0:
			self.delayMax = 1.0/tFPSMax
		elif tFPSMax==0:
			self.delayMax = 100_000
		else:
			raise Exception(self.Name+" FPS can't be less than 0")

		if tx==None or ty==None:
			self.pos = None
		else:
			self.pos = Vector2D(tx,ty)
	   
		self.lastClick = get_now()
		self.button = tbutton.lower()
		self.Name = tName

	def Update(self):
		self.WasClicked+=1
		
		self.DelayToNextClick = random.uniform(self.delayMin, self.delayMax)
		if get_now() >= self.NextClickTime - 0.0001:
			while get_now() - self.NextClickTime >= self.DelayToNextClick*5: # If more than 5 click are not clicked
				print(self.Name+" Unable to click that fast: Remove " +str(3)+ " click.")
				self.NextClickTime += (self.DelayToNextClick*3 )

			self._click()
			self.NextClickTime = self.NextClickTime + self.DelayToNextClick*1.01  #TODO: understand why need this slower adjusted

		

		return self.RealClickPerSec()
	def _click(self):
		#TODO: let user deside it click duration. (should be easy)
		if self.pos == None:
			fastclick(self.button)
			
		else:
			fastclick(self.button, self.pos.x, self.pos.y)


	def RealClickPerSec(self): #TODO
		return 0

class Typist:

	def __init__(self, arg):
		self.arg = arg
		