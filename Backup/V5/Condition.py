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
