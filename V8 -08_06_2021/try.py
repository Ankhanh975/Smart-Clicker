from _main import *

#Done: pynput: nhẹ hơn, delay thấp
#Done: test xem win32api relase có ảnh hưởng tới input ko (yes: giống hệt nhả chuột)
#TODO: google vision nhận dạng tên
#TODO: dừng mua hàng 


from pynput.mouse import Controller
mouse = Controller()

import pygame
class Switch:
	def __init__(self, KeyPressEvent=[], playsuond=False):
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
		elif self.TwoLastState==[True,False]:
			self._Event()

	def _Event(self):
		self.State = not self.State
		if self.playsuond:
			self.Sound[0 if self.State==True else 1].play()

		
		if self.State == True:
			scrollTheard.scroll = 0
			HighPerformanceStuff.scroll = 0
			print("Down")

	def GetState(self):
		return int(self.State)

class HighPerformStuff(RunThread):
	def __init__(self):
		super().__init__("HighPerformStuff", 120)
		self.scroll = 0
		self.Switch = UserInput.Switch(["mbutton"])

	def Stuff(self):
		print("scroll:", num, "self.scroll=", self.scroll)
		
		userInput.Update(0)
		self.Switch.Update(userInput)
		if userInput.IsPressed(["mbutton"]):
			if self.scroll!=scrollTheard.scroll:
				scroll = abs(scrollTheard.scroll - self.scroll)
				scroll *= 1 if self.scroll < scrollTheard.scroll else -1

				self.scrollEvent(scroll)

	def scrollEvent(self, num):
		absScroll = abs(num)
		if num != int(num):
			return
		if num>0:
			print("scroll:", num, "self.scroll=", self.scroll)
			for i in range(absScroll):
				win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -100)
				resorce.Sleepp(1/500)
		elif num<0:
			print("scroll:", num, "self.scroll=", self.scroll)
			for i in range(absScroll):
				win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 200)
				resorce.Sleepp(1/500)
		else:
			return

class getMinecraftSlot:
	scroll = 0
	def __init__(self):
		self.listener = pynput.mouse.Listener(on_scroll=self.on_scroll)

	def start(self):
		self.listener.start()

	def on_scroll(self, _, __, dx, dy):
		#self.scroll += int(dy / abs(dy))
		self.scroll += dy
		print("Detext: ", time.perf_counter(), dx, dy, self.scroll)


scrollTheard = getMinecraftSlot()
scrollTheard.start()

HighPerformanceStuff = HighPerformStuff()
Thread(target = HighPerformanceStuff.loop).start()
