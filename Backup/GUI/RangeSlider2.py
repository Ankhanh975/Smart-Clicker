import pygame
from _main2 import *
import win32gui
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
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200,300), DOUBLEBUF|NOFRAME) #
switch = Switch((20,20), "Ctrl+C")
clickSound = ClickSound()

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