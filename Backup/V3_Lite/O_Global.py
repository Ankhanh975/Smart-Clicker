import win32api, win32con, win32gui
import pyautogui, keyboard
import pygame
import time, random, sys, os, math
from Sub_Method import *
from instruction_loader import *
class Switch:
	def __init__(self, tKeyPressEvent=[], tSwitchSound=100):
		self.SwitchEvent = list(tKeyPressEvent)
		self.SwitchSound = int(tSwitchSound)

		self.TwoLastState=[False,False]
		self.State = False
	def Update(self, Global_HoldKey):
		if self.SwitchEvent!=[] and IsPressed(Global_HoldKey, self.SwitchEvent):
			Now = True
		else:
			Now = False
		self.TwoLastState=[self.TwoLastState[1],Now]

		if self.TwoLastState==[False,True]:
			self._Event()

	def _Event(self):
		self.State = not self.State
		#TODO: sound

	def GetState(self):
		#First init state is false
		return self.State


class Condition:
	def __init__(self, tKeyPressCondition=[], tBox=None, tActiveWindow=None, tO_Switch_Event=[], tActiveTime=None):
		self.KeyPressCondition = tKeyPressCondition
		self.Box = tBox
		self.ActiveWindow = tActiveWindow
		self.ActiveTime = tActiveTime
		self.initTime = time.perf_counter()
		self.O_Switch = Switch(tKeyPressEvent=[])
		self.O_Switch.SwitchEvent = [] 

		#self.O_Switch.Update() shuold be call every frame

		self.Save1 = False
		self.Save2 = False
		self.Save3 = False
		self.Save4 = False
		self.Save5 = False

	def IsTrue(self, Global_HoldKey, Global_MousePos, Global_ActiveWindow):
		self.Save1 = self.IsInActiveWindow(Global_ActiveWindow)
		self.Save2 = self.IsInBox(Global_MousePos)
		self.Save3 = self.IsHoldKey(Global_HoldKey)
		self.Save4 = self.IsSwich()
		self.Save5 = self.IsActiveTime()

		if self.IsInActiveWindow(Global_ActiveWindow) and self.IsInBox(Global_MousePos) and self.IsHoldKey(Global_HoldKey) and self.IsSwich() and self.IsActiveTime():
			return True
		else:
			return False

	def IsInActiveWindow(self, Global_ActiveWindow):
		if self.ActiveWindow == None:
			return True
		elif self.ActiveWindow == str(Global_ActiveWindow):
			return True
		else:
			return False
	def IsSwich(self):
		if self.O_Switch.SwitchEvent ==[]:
			return True
		else:
			return self.O_Switch.GetState()
	def IsInBox(self, Global_MousePos):
		if self.Box == None:
			return True
		elif self.Box[0][0] <= Global_MousePos[0] <= self.Box[1][0]:
			if self.Box[0][1] <= Global_MousePos[1] <= self.Box[1][1]:
				return True
		return False

	def IsHoldKey(self, Global_HoldKey):
		return IsPressed(Global_HoldKey, self.KeyPressCondition)

	def IsActiveTime(self):
		if self.ActiveTime == None:
			return True
		elif time.perf_counter() - self.initTime > self.ActiveTime:
			return False
		else:
			return True
	def __str__(self): 
		return str([int(self.Save1), int(self.Save2), int(self.Save3), int(self.Save4), int(self.Save5) ])
	def __repr__(self):
		return self.__str__()

class Base:
	def __init__(self, tName=""):
		if tName=="": #TODO
			self.name = "id: " + str(random.randint(0,10000))
		else:
			self.name = str(tName)

		self.StartCondition = Condition() #Defalt is true
		self.KillCondition = Condition() #Defalt is false
		self.EventCondition = Condition() #Defalt is true

		self.State="__init__ed"

		self.init_time = time.perf_counter()
		self.start_time = 0
		self.run_time = 0
		self.init_run_time = 0
		self.CreatedEvent = 0
		self.stop_time = None

	def Update(self, Global_HoldKey, Global_MousePos, Global_ActiveWindow):
		self.StartCondition.O_Switch.Update(Global_HoldKey)
		self.KillCondition.O_Switch.Update(Global_HoldKey)
		self.EventCondition.O_Switch.Update(Global_HoldKey)

		if self.State=="started":
			self.run_time = time.perf_counter() - self.start_time
			self.init_run_time = time.perf_counter() - self.init_time

		if self.State== "__init__ed" and self.StartCondition.IsTrue(Global_HoldKey, Global_MousePos, Global_ActiveWindow):
			self.Start()

		if self.State=="started": #TODO: only need (self.KillCondition.O_Switch.SwitchEvent == []) ?
			if not(self.KillCondition.O_Switch.SwitchEvent == [] and
				   self.KillCondition.KeyPressCondition == [] and
				   self.KillCondition.Box == None and
				   self.KillCondition.ActiveWindow == None and
				   self.KillCondition.ActiveTime == None):
				if self.KillCondition.IsTrue(Global_HoldKey, Global_MousePos, Global_ActiveWindow):
					self.Kill()

	def Start(self):
		self.start_time = time.perf_counter()
		self.run_time = 0
		self.State="started"

	def Kill(self):
		self.State="ended"
		self.stop_time = time.perf_counter()

	def Event(self, Global_HoldKey, Global_MousePos, Global_ActiveWindow):
		if self.EventCondition.IsTrue(Global_HoldKey, Global_MousePos, Global_ActiveWindow):
			if self.State == "started":
				self.CreatedEvent+=1
				return True
		return False

class Global(Base):
	def __init__(self, tFPS=60):
		super().__init__(tName="_Controller")
		self.screenSize = pyautogui.size()
		self.FPS = tFPS
		self.clock = pygame.time.Clock()
		self.frameCount = 0
		self.NeedCheckedKey = []

		self.Global_HoldKey = []
		self.Global_MouseIn = "2c3q7rbxytngeiyu44i3"
		self.Global_MousePos = [0,0]
		self.Global_ActiveWindow = "84rg6es5fd321xv"

		self.running_object = 0 #TODO
		self.running_object_names = [] #TODO

	def Update(self):
		super().Update(self.Global_HoldKey, self.Global_MousePos, self.Global_ActiveWindow)
		self.frameCount +=1
		self.clock.tick(self.FPS)

		flags, hcursor, self.Global_MousePos = win32gui.GetCursorInfo()

		self.Global_MouseIn = win32gui.GetWindowText(hcursor)
		self.Global_ActiveWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
		self.Global_HoldKey = getKeyState(self.NeedCheckedKey)

	def get_fps(self):
		return round(self.clock.get_fps(), 2)

	def Kill(self):
		super().Kill()
		pygame.quit(); sys.exit()
		#TODO: sound

if __name__ == '__main__':
	a=Global()
	a.StartCondition.KeyPressCondition = ["K_F4"]
	while True:
		a.Global_HoldKey, a.Global_MousePos, a.Global_ActiveWindow
		print(a.State)

		a.Update()

#if __name__ == '__main__':
#	control = Global()
#	while True:
#		print(control.frameCount)
#		control.Update()