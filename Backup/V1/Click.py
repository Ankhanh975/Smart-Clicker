import pyautogui
import time
import random
import time, win32api, win32con

from Vector2d import * # Class Vector2D

from datetime import datetime	
import keyboard

pyautogui.FAILSAFE = False

get_now = time.perf_counter
#TODO: neu moi Frame chi chay 1 get_now thi co duoc ko?

def _sleep(duration): # Fast, high accurate clock
	time.sleep(1/60)
	#now = get_now()
	
	#end = now + duration
	#while now < end:
	#	if end-now >= 1/60:
	#		time.sleep(1/1000)
	#	now = get_now()

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

class Control:
	StartProgram = get_now()
	
	def __init__(self, tFPS=60, tStopKey=["Ctrl","Esc"]):

		self.frameCount = 0;
		self.FPS = tFPS
		self.DesireTimePerFrame = 1.0/self.FPS # const

		self.StopKey = tStopKey

		self.lastFrame = 0 # Just setup, it's nothing


	def Update(self):
		self.MousePos = Vector2D(pyautogui.position()[0],pyautogui.position()[1])
		self.frameCount+=1
		self.LimitFPS()
		self.lastFrame = get_now()

	def StopProgram(self):
		for key in self.StopKey:
			if not keyboard.is_pressed(key):
				return False
		return True

	def LimitFPS(self):

		startTime = self.lastFrame
		endTime = get_now()
		self.FrameDelay = endTime - startTime
		#print(FrameDelay, self.p , endTime, startTime)
		if self.FrameDelay <= self.DesireTimePerFrame:
			_sleep(self.DesireTimePerFrame - self.FrameDelay)
			#print("FrameDelay: "+str(self.GetFPS()))

		else:
			pass
			#print("Not able to run at "+str(self.FPS)+"fps !")
			#print("FrameDelay: "+str(self.GetFPS()))


	def GetFPS(self): #TODO: for now this just return FrameDelay
		return self.FrameDelay

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

def LoadInstruction():
	import json
	f = open('instruction.json')
	data = json.load(f)
	return data

def lower_json(json_info):
	# Lower all string input 
	if isinstance(json_info,dict):
		for key in list(json_info.keys()):
			if key.islower():
				lower_json(json_info[key])
			else:
				key_lower = key.lower()
				json_info[key_lower] = json_info[key]
				del json_info[key]
				lower_json(json_info[key_lower])

	elif isinstance(json_info,list):
		for item in json_info:
			lower_json(item)

data = LoadInstruction()
lower_json(data)

System = Control()
System.StopKey = data["stopkey"]

Object = []
for xx in data:
	if not xx=="stopkey": #Then is a theat
		if data[xx]["type"]=="Click":
			try:
				button = data[xx]["button"]
			except KeyError:
				button = "left"

			try:
				RandomInFPS = data[xx]["randomInFPS"]
			except KeyError:
				RandomInFPS=0

			try:
				x = data[xx]["x"]
				y = data[xx]["y"]

			except KeyError:
				x = None
				y = None

			new = Click(data[xx]["fps"], button, RandomInFPS, x, y, xx)
			Object.append(new)
	

while True: 
	for x in Object:
		x.Update()

	System.Update() # Limit fps
	if System.StopProgram()==True: # Break
		break

