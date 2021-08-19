import win32api, win32con, win32gui
import pyautogui, keyboard
import pygame
import time, random, sys, os, math
pyautogui.FAILSAFE = False

#class MousePress:
#	# Check for keypress
#	def __init__(self, tMousePressButton):
#		if tMousePressButton=="Middle":
#			self.MouseButton=1
#		elif tMousePressButton=="Left":
#			self.MouseButton=0
#		elif tMousePressButton=="Right":
#			self.MouseButton=2
#
#	def OnPressed(self, Global_HoldMouseButton):
#		if Global_HoldMouseButton[self.MouseButton]==1:
#			return True
#		else:
#			return False

def _sleep(duration): #High accurate sleep
	now = time.perf_counter()
	end = now + duration
	while now < end:
		if end-now >= 1/61:
			time.sleep(1/1000)
		now = time.perf_counter()

class KeyPress:
	# Check for keypress
	def __init__(self, tKeyPressData):

		if type(tKeyPressData)==str:
			#Ex: tKeyPressData= 'Ctrl+Shift+Esc'
			self.KeyPressData = tKeyPressData.split("+")
		elif type(tKeyPressData)==list:
			#Ex: tKeyPressData= ["Ctrl", "Shift", "Esc"]
			self.KeyPressData = tKeyPressData

		for x in self.KeyPressData:
			if self.KeyPressData.count(x) >=2:
				raise Exception("Your KeyPress: "+tKeyPressData+" is duplicate")

	def OnPressed(self, Global_holdKey):
		for x in self.KeyPressData:
			if x not in Global_holdKey:
				return False
		return True

class Switch:
	def __init__(self, tKeyPressEvent="", tSwitchSound=100):
		self.KeyPressEvent = str(tKeyPressEvent)
		self.SwitchSound = int(tSwitchSound)

		self.State = False
		self.TwoLastState=[False,False]

	def Update(self, Global_HoldKey):
		Now=self.TwoLastState[1]
		if self.KeyPressEvent in str(Global_HoldKey):
			Now=True
		else:
			Now=False

		self.TwoLastState=[self.TwoLastState[1],Now]
		if self.TwoLastState==[False,True]:
			self.SwitchEvent()

	def SwitchEvent(self):
		self.State = not self.State
		print(self.State)


class Condition:
	def __init__(self, KeyPressCondition="", Box=[[0,0],[1920,1080]], ActiveWindow=""):
		self.KeyPressCondition = ""
		self.Box = [[0,0],[1920,1080]]
		self.ActiveWindow = ""
		self._KeyPress = KeyPress(self.KeyPressCondition)
		self.LimitActiveTime = 10_000_000
		self.O_Switch = Switch() #TODO

		self.ActiveTime = 0
	def IsTrue(self, Global_holdKey, Global_MousePos, Global_ActiveWindow):
		self.O_Switch.Update()
		if self.IsInActiveWindow(Global_ActiveWindow) and self.IsInBox(Global_MousePos) and self.IsHoldKey(Global_holdKey) and self.ActiveTime<self.LimitActiveTime:
			self.ActiveTime+=1
			return True
		else:
			return False

	def IsInActiveWindow(self, Global_ActiveWindow):
		if self.ActiveWindow == "":
			return True
		if self.ActiveWindow==str(Global_ActiveWindow):
			return True
		else:
			return False

	def IsInBox(self, Global_MousePos):
		if self.Box[0][0] <= Global_MousePos[0] <= self.Box[1][0]:
			if self.Box[0][1] <= Global_MousePos[1] <= self.Box[1][1]:
				return True
		else:
			return False
	def IsHoldKey(self, Global_holdKey):
		return self._KeyPress.OnPressed()
	def Switch(self):
		if self.O_Switch.State==True:
			return True
		else:
			return False

class Base:
	def __init__(self, tName=""):
		if tName=="":
			self.name = "id: " + str(random.randint(0,10000))
		else:
			self.name = str(tName)

		self.StartCondition = Condition()
		self.KillCondition = Condition()
		self.EventCondition = Condition()
		self.State="__init__ed"

		self.init_time = time.perf_counter()
		self.start_time = 0
		self.run_time = 0
		self.init_run_time = 0
		self.CreatedEvent = 0

	def Update(self): #TODO
		self.run_time = time.perf_counter() - self.start_time
		self.init_run_time = time.perf_counter() - self.init_time

		if self.State=="__init__ed" and self.StartCondition.IsTrue():
			self.Start()

		if self.State=="started" and self.KillCondition.IsTrue():
			self.Kill()

	def Start(self):
		self.start_time = time.perf_counter()
		self.State="started"

	def Kill(self):
		self.State="ended"

	def Event(self):
		if not self.EventCondition.IsTrue():
			return
		if not self.EventCondition.IsTrue():
			return
		self.CreatedEvent+=1
		
class Global(Base):
	def __init__(self, tFPS=60):
		super().__init__(tName="Controller")
		self.screenSize = pyautogui.size()
		self.FPS = tFPS
		self.clock = pygame.time.Clock()
		self.frameCount = 0
		self.NeedCheckedKey = []

		self.Global_HoldKey = []
		self.Global_MouseIn = GetWindowText(hcursor)
		self.Global_HoldMouseState = []
		self.Global_MousePos = []
		self.Global_ActiveWindow = []

		self.running_object = 0
		self.running_object_names = []
		
	def Update(self):
		super().Update()
		self.running_object = 0 #TODO

		flags, hcursor, self.Global_MousePos = win32gui.GetCursorInfo()

		self.Global_MouseIn = GetWindowText(hcursor)
		self.Global_ActiveWindow = GetWindowText(GetForegroundWindow())
		self.Global_HoldMouseButton = []
		self.Global_HoldKey = []
		self.clock.tick(self.FPS)

	def get_fps(self):
		return clock.get_fps()

	


if __name__ == '__main__':
	a= Switch("c")
	while True:
		time.sleep(1/30)
		print(keyboard.read_key())