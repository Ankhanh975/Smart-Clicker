import pygame
from pygame.locals import *
import random, sys, os, math, time
import Vector2d

def SetUp():
	pygame.init()
	pygame.mixer.init(44100, -16, 2, 64)
	programIcon = pygame.image.load('Logo.png')
	pygame.display.set_icon(programIcon)
	pygame.display.set_caption("Smart Clicker") #TODO: anime between "Smart Clicker" - " Auto Clicker" - "Good Luck!"

SetUp()

class GetInput():
	def __init__(self):
		self.screenSize = None, None
		import _List
		self.VK_CODE_REVERSE = _List.VK_CODE_REVERSE

		self.HoldKey = []
		self.MousePos = -1, -1
		
	def Update(self, events):
		for event in events:
			if event.type==pygame.KEYDOWN:
				try:
					self.HoldKey.append(pygame.key.name(event.key))
				except:
					self.HoldKey.append(event.key)
				
			elif event.type==pygame.KEYUP:
				try:
					self.HoldKey.remove(pygame.key.name(event.key))
				except:
					self.HoldKey.remove(event.key)
				
			elif event.type in [pygame.MOUSEMOTION, MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
				self.MousePos=event.pos

			elif event.type==pygame.ACTIVEEVENT and event.gain==0:
				if event.state==1:
					self.MousePos=[-1,-1]
				else:
					self.HoldKey=[]
					self.MousePos=[-1,-1]

			elif event.type == pygame.VIDEORESIZE:
				self.screenSize=event.size
						   
			if event.type==pygame.MOUSEBUTTONDOWN:
				#Users_Input["Mouse"]["Hold_Mode"][event.button-1]=1
				pass
			elif event.type==pygame.MOUSEBUTTONUP:
				#Users_Input["Mouse"]["Hold_Mode"][event.button-1]=0
				pass
			elif event.type==pygame.MOUSEMOTION:
				#Users_Input["Mouse"]["Hold_Mode"]=list(event.buttons)
				pass


	def IsPressed(CheckKeyStrokes):
		for x in CheckKeyStrokes:
			if x not in self.HoldKey:
					return False
		return True

	def __str__(self):
		return "screenSize:" + str(self.screenSize) + ", HoldKey:" + str(self.HoldKey) + "MousePos:" + str(self.MousePos)

	def debug(self):
		print("screenSize:", self.screenSize)
		print("HoldKey:", self.HoldKey )
		print("MousePos:", self.MousePos )
		print("\n")

if __name__=="__main__":
	screen = pygame.display.set_mode((200,300), DOUBLEBUF|RESIZABLE)
	a= GetInput()
	while True:
		pygame.display.update()
		events = pygame.event.get()
		for event in events:
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit()
		a.Update(events)
		print(a)