import time
from threading import Thread
import datetime as dt
import win32gui, win32api
import win32con 
#For win32gui argument

class ReadMinecreaftLog: 
	#Might break in anthor version (cần tùy chỉnh theo log của từng phiên bản)
	#mincraft reset latest.log every day
	file = "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log"
 
	sleepTime=0
	stop = False

	def __init__(self):
		self.mode = "3fmc Before Login"
		self.allowClick = True
		self.NotAllowClickTime = time.perf_counter()

		self.today = dt.datetime.now()  #Date this being read
		self.currentTime =  dt.time(self.today.hour, self.today.minute, self.today.second) #Init time

		self.line=""
		self.FiltedLog = []

		self.Up_KIEM = False
		self.Up_GIAP = [0,1,2,3,4][0]
		self.ACTIVE_IT_TRAP = [None, dt.time(13, 00, 00)][0]
		self.IT_TRAP = 0

		self.DEAD = 0
		self.KILL = 0
		self.LastChatSpam = [None, dt.time(self.today.hour, self.today.minute, self.today.second)][0]
		self.LastDEAD = dt.datetime.now()
		self.LastKILL = dt.datetime.now()
		self.GameStartedTime = dt.datetime.now()
		self.GameEndedTime = dt.datetime.now()

	def loop(self):
		if self.allowClick == False and time.perf_counter()-self.NotAllowClickTime > (1/20)*3:
			self.allowClick = True

		with open(self.file, "r") as self.f:
			while (not self.stop):
				time.sleep(self.sleepTime)
				self.line = self.f.readline()

				if self.line!="":
					self.sleepTime=0
					if "[Client thread/INFO]: [CHAT]" in self.line:
						self.line = self.line.replace("[Client thread/INFO]: [CHAT]", "")
						self.line = self.line.replace("\n", "")
						self.progess(self.line)
				elif self.line=="":
					self.sleepTime=1/40