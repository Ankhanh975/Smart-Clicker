from _main2 import *
import win32gui
	
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200,300), DOUBLEBUF|NOFRAME) #
switch = Switch((20,20), "Ctrl+C")
clickSound = ClickSound()

class AnimationCaption: #TODO
	def __init__(self):
		self.text = ["Smart Clicker", "Auto Clicker", "Good Luck!"]
		self.On = 0
	def update(self):
		a = random.choice(self.text)
		print(a)
		pygame.display.set_caption(a)
		
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
	def update(self, events):
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
		
		if self.OnDrag==True:
			#self.Global_MousePos[0] = self.Global_MousePos[1]
			self.Global_MousePos[1] = win32gui.GetCursorInfo()[2]
			#self.mouse_rel = [self.Global_MousePos[1][0] -  self.Global_MousePos[0][0], self.Global_MousePos[1][1] - self.Global_MousePos[0][1]]
			win32gui.MoveWindow(self.hwnd, self.Global_MousePos[1][0] - self.ClickPos[0], self.Global_MousePos[1][1] - self.ClickPos[1], 200, 300, True)

movingWindow = MovingWindow((200,300))
def draw(events, getPFS):
	#print(IsPressed([pygame.K_LCTRL, pygame.K_TAB]))
	for event in events:
		if event.type==pygame.KEYDOWN:
			pass
			#print(event.key)
			#switch.Event()

		elif event.type==pygame.KEYUP:
			#print(event.key)
			pass
		elif event.type==pygame.MOUSEMOTION:
			pass
	switch.UpdateAndDisplay(events, screen)

	

	if frame%8==0 and switch.state==True:
		clickSound.play()

frame = 0
while True:
	frame +=1
	pygame.display.update()
	clock.tick(60)
	screen.fill((0,255,255))

	events = pygame.event.get()
	movingWindow.update(events)
	for event in events:
		if event.type==pygame.QUIT:
			pygame.quit(); sys.exit()

	draw(events, round(clock.get_fps(), 2))

	
		
	