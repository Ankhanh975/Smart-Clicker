import pygame
from pygame.locals import *
import random, sys, os, math, time
import Vector2d
import win32gui
import itertools

def SetUp():
	pygame.init()
	pygame.mixer.init(44100, -16, 2, 64)
	programIcon = pygame.image.load('Resources/Logo.png')

	size = programIcon.get_rect().size
	for x in range(size[0]):
		for y in range(size[1]):
			n=programIcon.get_at((x, y))
			programIcon.set_at((x,y), ( n[3], n[3], n[3], 255))

	pygame.display.set_icon(programIcon)
	pygame.display.set_caption("Smart Clicker") #TODO: anime between "Smart Clicker" - " Auto Clicker" - "Good Luck!"

SetUp()

def IsPressed(CheckKeyStrokes):
		# Validity input: https://www.pygame.org/docs/ref/key.html
		keys = pygame.key.get_pressed()
		for x in CheckKeyStrokes:
			if keys[x]==False:
				return False
		return True

class ClickSound:
	def __init__(self):
		self.type = [""]
		self.Sound = self.Load()
		self.ClickIndex = itertools.cycle(range(1,20))
		0 # Run Sound sample from 0 to 19 and angain

	def Load(self):
		ClickSound = []
		for x in range(1, 20):
			a=pygame.mixer.Sound("Resources/Sample "+str(x)+".mp3")
			a.set_volume(0.22)
			ClickSound.append(a)
		return ClickSound
	def play(self):
		#TODO: if click too fast then self.Sound[self.ClickIndex].play() run with 1/2 clicked 
		self.Sound[next(self.ClickIndex)].play()

COLOR_INACTIVE = (255,255,255)
COLOR_ACTIVE = (255,255,255)
FONT = pygame.font.Font(None, 32)

class TextBox:
	def __init__(self, x, y, text='', w=140, h=32):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, False, self.color)
		self.active = False

		width = max(20, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		s = pygame.Surface((self.rect[2], self.rect[3]))  # the size of your rect
		s.set_alpha(150)		 
		s.fill((30,30,30))
		screen.blit(s, (self.rect[0], self.rect[1]))	# (0,0) are the top-left coordinates

		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pygame.draw.rect(screen, self.color, self.rect, 2)

class Switch:
	def __init__(self, pos=[0,0], text=""):
		self.state = False
		self.SwitchSound = None #TODO
		self.SwitchImg = self.LoadImg()
		self.pos = Vector2d.Vector(pos)

		def LoadSound():
			a = pygame.mixer.Sound("Resources/On.mp3")
			a.set_volume(0.4)
			a.fadeout(50)
			b = pygame.mixer.Sound("Resources/Off.mp3")
			b.set_volume(0.4)
			b.fadeout(50)
			return [a,b]
		self.Sound = LoadSound()

		BoxImg=self.SwitchImg[0].get_rect()
		self.rect = BoxImg.move(self.pos[0], self.pos[1])

		self.HoldingTime = 0 #How long mosue have inside Switch also not click
		self.State = ["After Changed", "BeforChanged"][1]
		self.text = TextBox(self.pos.x+30, self.pos.y+50, text=text)
		#self.surface = pygame.Surface(get_rect())
	def LoadImg(self):
		def Load(file):
			SwitchImg = pygame.image.load(file)
			#SwitchImg = pygame.transform.scale(SwitchImg, (60, 60))
			SwitchImg = pygame.transform.rotate(SwitchImg, 90)
			size = SwitchImg.get_rect().size
			for x in range(size[0]):
				for y in range(size[1]): #(255,242,0)
					n=SwitchImg.get_at((x, y))
					if tuple(n) == (255,242,0, 255):
						SwitchImg.set_at((x,y), (255,255, 255, 0))
			return SwitchImg
		return Load("Resources/Off.png"), Load("Resources/On.png") 

	def UpdateAndDisplay(self, events, screen):
		UsingImg = 0 if self.state == False else 1
		screen.blit(self.SwitchImg[UsingImg], (int(self.pos[0]), int(self.pos[1])))

		for event in events:
			if event.type==pygame.MOUSEBUTTONUP:
				if self.rect.collidepoint(event.pos):
					ColorOfClickPos = self.SwitchImg[UsingImg].get_at((event.pos[0]- int(self.pos[0])-1, event.pos[1]- int(self.pos[1])-1))
					if ColorOfClickPos[3] != 0:
						self.Event()
					self.HoldingTime = 0
					self.State = "After Changed"
		
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if self.State == "BeforChanged":
				self.HoldingTime +=1
		else:
			self.HoldingTime = 0
			self.State = "BeforChanged"

		if self.HoldingTime > 70:
			self.text.draw(screen)

	def Event(self):
		self.state = not self.state
		self.Sound[0 if self.state==True else 1].play()

class MovingWindow:
	def __init__(self, winsize, wincaption="Smart Clicker", winpos=(600,300)):
		self.hwnd = win32gui.FindWindow(None, wincaption)
		self.winpos = winpos
		self.winsize = winsize
		self.ControllBar = pygame.Rect(0,0,winsize[1],25)
		self.Border = pygame.Rect(0, 0, winsize[0], winsize[1])

		self.Global_MousePos = [win32gui.GetCursorInfo()[2], win32gui.GetCursorInfo()[2]]

		if winpos != None:
			win32gui.MoveWindow(self.hwnd, self.winpos[0], self.winpos[1], self.winsize[0], self.winsize[1], True)

		self.ClickPos = (10,10)
		self.OnDrag = False
	def update(self, events, screen):
		pygame.draw.rect(screen, (0,10,20), self.ControllBar, width=1)
		pygame.draw.rect(screen, (0,10,20), self.Border, width=1)

		for event in events:
			if event.type==pygame.MOUSEBUTTONDOWN:
				if self.ControllBar.collidepoint(pygame.mouse.get_pos()):
					self.ClickPos = event.pos
					self.OnDrag = True
			if event.type==pygame.MOUSEBUTTONUP:
				if self.ControllBar.collidepoint(pygame.mouse.get_pos()):
					self.OnDrag = False
		
		# if self.OnDrag==True:
		# 	#self.Global_MousePos[0] = self.Global_MousePos[1]
		# 	self.Global_MousePos[1] = win32gui.GetCursorInfo()[2]
		# 	#self.mouse_rel = [self.Global_MousePos[1][0] -  self.Global_MousePos[0][0], self.Global_MousePos[1][1] - self.Global_MousePos[0][1]]
		# 	win32gui.MoveWindow(self.hwnd, self.Global_MousePos[1][0] - self.ClickPos[0], self.Global_MousePos[1][1] - self.ClickPos[1], 200, 300, True)



if __name__=="__main__":
	screen = pygame.display.set_mode((200,300), DOUBLEBUF|RESIZABLE)
	a= TextBox(100,100, "Ctrl+C")
	while True:
		pygame.display.update()
		events = pygame.event.get()
		for event in events:
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit()

		a.draw(screen)
