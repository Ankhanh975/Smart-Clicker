import pygame
from pygame.locals import *
import random, sys, os, math, time
import Vector2d

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
		self.ClickIndex = 0 # Run Sound sample from 0 to 19 and angain

	def Load(self):
		ClickSound = []
		for x in range(1, 20):
			a=pygame.mixer.Sound("Resources/Sample "+str(x)+".mp3")
			a.set_volume(0.22)
			ClickSound.append(a)
		return ClickSound
	def play(self):
		self.Sound[self.ClickIndex].play()
		self.ClickIndex +=1
		if self.ClickIndex==19:
			self.ClickIndex = 1 #TODO: if click too fast then self.Sound[self.ClickIndex].play() run with 1/2 clicked 

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
		

if __name__=="__main__":
	'''FONT = pygame.font.Font(None, 20)
	txt_surface = FONT.render("Afg", True, (150,150,150))

	text_x=100
	text_y=10
	surface = pygame.Surface((text_x+7, text_y+12), pygame.SRCALPHA)
	surface.fill((255,255,255,230))
	rect = pygame.Rect(0, 0, surface.get_rect()[2], surface.get_rect()[3])
	pygame.draw.rect(surface, (0,0,0, 200), rect,  1)
	
	surface.blit(txt_surface, (3,5))

	#surface.fill((255,255,255,255))

	screen.blit(surface, (10,10))'''

	screen = pygame.display.set_mode((200,300), DOUBLEBUF|RESIZABLE)
	a= TextBox(100,100, "Ctrl+C")
	while True:
		pygame.display.update()
		events = pygame.event.get()
		for event in events:
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit()

		#a.update()
		a.draw(screen)
		#print(a.IsPressed([pygame.K_LCTRL, pygame.K_TAB]))
		#print(pygame.key.get_pressed())


'''class GetInput():
	def __init__(self):
		self.screenSize = None, None
		self.MousePos = -1, -1

		import _List
		self.VK_CODE_REVERSE = _List.VK_CODE_REVERSE
		self.HoldKey = []
		
	def update(self, events):
		for event in events:
			if event.type in [pygame.MOUSEMOTION, MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
				self.MousePos=event.pos

			elif event.type==pygame.ACTIVEEVENT and event.gain==0:
				self.MousePos=[-1,-1]

			elif event.type == pygame.VIDEORESIZE:
				self.screenSize=event.size

	def IsPressed(self, CheckKeyStrokes):
		# Validity input: https://www.pygame.org/docs/ref/key.html
		keys = pygame.key.get_pressed()
		for x in CheckKeyStrokes:
			if keys[x]==False:
				return False
		return True

	def __str__(self):
		return "screenSize:" + str(self.screenSize) + ", HoldKey:" + str(self.HoldKey) + ", MousePos:" + str(self.MousePos)

	def debug(self):
		print("screenSize:", self.screenSize)
		print("HoldKey:", self.HoldKey )
		print("MousePos:", self.MousePos )
		print("\n")'''