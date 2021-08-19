# Dead when not even work alots
# Because of new discover: .yaml

import win32api, win32con, win32gui
import pyautogui, keyboard
import pygame
import time, random, sys, os, math

from Vector2d import * # Class Vector2D
from instruction_loader import *
from O_Clicker import *
from O_Swicher import *

pyautogui.FAILSAFE = False


#TODO: neu moi Frame chi chay 1 get_now thi co duoc ko?


class KeyPress:
	# Check for keypress
	def __init__(self, tKeyPressData):
		self.KeyPressData = tKeyPressData

		for x in self.KeyPressData:
			if self.KeyPressData.count(x) >=2:
				raise Exception("Your KeyPress is duplicate")

	def OnPressed(self, Global_holdKey):
		for x in self.KeyPressData:
			if x not in Global_holdKey:
				return False
		return True

class Base:
	init_time = time.perf_counter()
	run_time = 0
	init_run_time = 0
	CreatedEvent = 0
	def __init__(self, tName):
		self.name = str(tName)
		self.Condition = {}

	def Update(self):
		run_time = Global.get_now() - self.start_time
		init_run_time = Global.get_now() - self.init_time

	def Start(self):
		self.start_time = 0

	def Kill(self, Global_holdKey):

	def Event(self, ):
		self.CreatedEvent+=1

class Global:
	def __init__(self, tFPS=60, tStopKey=["Ctrl","Esc"]):
		self.init_time = time.perf_counter()
		self.start_time = 0
		self.run_time = 0
		self.init_run_time = 0
		self.running_object = 0
		self.CreatedEvent = 0

		self.frameCount = 0
		self.FPS = tFPS
		self.KillData = tStopKey
		self.clock = pygame.time.Clock()
		self.holdKey = []

		self.GetFPS = clock.get_fps
		self.get_now = time.perf_counter

	def Update(self):
		self.run_time = time.perf_counter() - self.init_time
		self.init_run_time = time.perf_counter() - self.start_time
		self.running_object = 0 #TODO
		self.CreatedEvent = 0	#TODO

		self.MousePos = Vector2D(pyautogui.position()[0],pyautogui.position()[1])
		self.frameCount+=1

		self.clock.tick(self.FPS)

	def Kill(self):
		for key in self.StopKey:
			if not keyboard.is_pressed(key):
				return False
		return True

	def _sleep(duration): #High accurate sleep
		now = get_now()
		
		end = now + duration
		while now < end:
			if end-now >= 1/61:
				time.sleep(1/1000)
			now = get_now()



	

#while True: 
#	for x in Object:
#		x.Update()
#
#	System.Update() # Limit fps
#	if System.Kill()==True:
#		pygame.quit(); sys.exit()



