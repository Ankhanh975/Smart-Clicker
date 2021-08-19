import pygame
class Switch:
	def __init__(self, KeyPressEvent=[], playsuond=True):
		self.SwitchEvent = list(KeyPressEvent)
		self.playsuond=playsuond
		self.TwoLastState=[False,False]
		self.State = False

		def LoadSound():
			a = pygame.mixer.Sound("Resources/On.mp3")
			a.set_volume(0.15)
			a.fadeout(50)
			b = pygame.mixer.Sound("Resources/Off.mp3")
			b.set_volume(0.15)
			b.fadeout(50)
			return [a,b]
		self.Sound = LoadSound()

	def Update(self, GlobalInput):
		if self.SwitchEvent!=[] and GlobalInput.IsPressed(self.SwitchEvent):
			Now = True
		else:
			Now = False
		self.TwoLastState=[self.TwoLastState[1],Now]

		if self.TwoLastState==[False,True]:
			self._Event()

	def _Event(self):
		self.State = not self.State
		if self.playsuond:
			self.Sound[0 if self.State==True else 1].play()
	def GetState(self):
		return int(self.State)

	
class Condition:
	def __init__(self, KeyPressCondition=[], Box=None, ActiveWindow=None, tO_Switch_Event=[], ActiveTime=None):
		self.KeyPressCondition = KeyPressCondition
		self.Box = Box
		self.ActiveWindow = ActiveWindow
		self.ActiveTime = ActiveTime
		self.initTime = time.perf_counter()
		self.O_Switch = Switch(KeyPressEvent=[])
		self.O_Switch.SwitchEvent = [] 

		#self.O_Switch.Update() shuold be call every frame

		self.Save1 = False
		self.Save2 = False
		self.Save3 = False
		self.Save4 = False
		self.Save5 = False

	def IsTrue(self, GlobalInput):
		self.Save1 = self.IsInActiveWindow(GlobalInput)
		self.Save2 = self.IsInBox(GlobalInput)
		self.Save3 = self.IsHoldKey(GlobalInput)
		self.Save4 = self.IsSwich()
		self.Save5 = self.IsActiveTime()

		if self.IsInActiveWindow(GlobalInput) and self.IsInBox(GlobalInput) and self.IsHoldKey(GlobalInput) and self.IsSwich() and self.IsActiveTime():
			return True
		else:
			return False

	def IsInActiveWindow(self, GlobalInput):
		if self.ActiveWindow == None:
			return True
		elif self.ActiveWindow == str(GlobalInput):
			return True
		else:
			return False
	def IsSwich(self):
		if self.O_Switch.SwitchEvent ==[]:
			return True
		else:
			return self.O_Switch.GetState()
	def IsInBox(self, GlobalInput):
		if self.Box == None:
			return True
		elif self.Box[0][0] <= Global_MousePos[0] <= self.Box[1][0]:
			if self.Box[0][1] <= Global_MousePos[1] <= self.Box[1][1]:
				return True
		return False

	def IsHoldKey(self, GlobalInput):
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

