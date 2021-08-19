from threading import Thread
import pygame, random, time


class RunThread:
	stop = False
	def __init__(self, name: str, FPS=[13,17]):
		self.clock = pygame.time.Clock()
		self.name = name
		if type(FPS)==int:
			self.FPSMin = self,FPSMax = FPS
		elif type(FPS)==list or type(FPS)==tuple:
			self.FPSMin = min(FPS[0], FPS[1])
			self.FPSMax = max(FPS[0], FPS[1])

	def loop(self):
		while self.stop == False:
			self.RunFPS = round(random.uniform(self.FPSMin, self.FPSMax), 2)
			self.clock.tick(self.RunFPS)
			print(self.name, self.RunFPS, self.clock.get_fps())
			self.Stuff()

	def Stuff(self):
		pass

	def get_fps(self):
		return round(self.clock.get_fps(), 2)

	def debug(self):
		print("Clock:", self.clock)
		print("FPS:", [self.FPSMin, self.FPSMax], "Intended FPS:", self.RunFPS, "Real FPS:", self.get_fps())
		print("Name:", self.name) 
		print()


Thread1 = RunThread("Thread1")
Thread2 = RunThread("Thread2")
Thread(target = Thread1.loop).start()
Thread(target = Thread2.loop).start()
