import win32api, win32con, win32gui
import pyautogui, keyboard
import pygame
import time, random, sys, os, math
from Sub_Method import *
from Preprocess_instruction import *
from Condition import *
import _List

class Base:
	def __init__(self, Name=""):
		if Name=="": #TODO
			self.name = "id: " + str(random.randint(0,10000))
		else:
			self.name = str(Name)

		self.StartCondition = Condition()
		self.KillCondition = Condition()
		self.EventCondition = Condition()

		self.State="__init__ed"

		self.init_time = time.perf_counter()
		self.start_time = 0
		self.run_time = 0
		self.init_run_time = 0
		self.CreatedEvent = 0
		self.stop_time = None

	def Update(self, GlobalInput):
		self.StartCondition.O_Switch.Update(Global_HoldKey)
		self.KillCondition.O_Switch.Update(Global_HoldKey)
		self.EventCondition.O_Switch.Update(Global_HoldKey)

		if self.State=="started":
			self.run_time = time.perf_counter() - self.start_time
			self.init_run_time = time.perf_counter() - self.init_time

		if self.State== "__init__ed" and self.StartCondition.IsTrue(GlobalInput):
			self.Start()

		if self.State=="started": #TODO: only need (self.KillCondition.O_Switch.SwitchEvent == []) ?
			if not(self.KillCondition.O_Switch.SwitchEvent == [] and
				   self.KillCondition.KeyPressCondition == [] and
				   self.KillCondition.Box == None and
				   self.KillCondition.ActiveWindow == None and
				   self.KillCondition.ActiveTime == None):
				if self.KillCondition.IsTrue(GlobalInput):
					self.Kill()

	def Start(self):
		self.start_time = time.perf_counter()
		self.run_time = 0
		self.State="started"

	def Kill(self):
		self.State="ended"
		self.stop_time = time.perf_counter()

	def Event(self, GlobalInput):
		if self.EventCondition.IsTrue(GlobalInput):
			if self.State == "started":
				self.CreatedEvent+=1
				return True
		return False

class Global(Base):
	def __init__(self, FPS=60):
		super().__init__(tName="_Controller")
		self.screenSize = pyautogui.size()
		self.FPS = FPS
		self.clock = pygame.time.Clock()
		self.frameCount = 0
		self.NeedCheckedKey = []

		self.UserInput = GetInput()

		self.running_object = 0 #TODO
		self.running_object_names = [] #TODO

	def Update(self):
		super().Update(GlobalInput)
		self.frameCount +=1
		self.clock.tick(self.FPS)

		self.UserInput.Update()

	def get_fps(self):
		return round(self.clock.get_fps(), 2)

	def Kill(self):
		super().Kill()
		pygame.quit(); sys.exit()
		#TODO: sound

if __name__ == '__main__':
	a= Global()
	for b in range(1000):
		a.Update
		print()