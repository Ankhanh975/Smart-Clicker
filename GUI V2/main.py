from _main2 import *

#TODO: switch button: đẹp như window switch
# Chú thích: như ưindow
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
		

movingWindow = MovingWindow((200,300))
print(movingWindow)

from pynput.mouse import Button, Controller
import pynput
import win32gui

mouse = Controller()
class getMinecraftSlot:
	def __init__(self):
		self.pos = (0, 0)
		self.listener = pynput.mouse.Listener(on_move=self.on_move)

	def start(self):
		self.listener.start()

	def on_move(self, x, y):
		print(movingWindow)
		if movingWindow.OnDrag==True:
			movingWindow.Global_MousePos[0] = movingWindow.Global_MousePos[1]
			movingWindow.Global_MousePos[1] = [x,y]
			movingWindow.mouse_rel = [movingWindow.Global_MousePos[1][0] -  movingWindow.Global_MousePos[0][0], movingWindow.Global_MousePos[1][1] - movingWindow.Global_MousePos[0][1]]
			win32gui.MoveWindow(movingWindow.hwnd, movingWindow.Global_MousePos[1][0] - movingWindow.ClickPos[0], movingWindow.Global_MousePos[1][1] - movingWindow.ClickPos[1], 200, 300, True)

scrollTheard = getMinecraftSlot()
scrollTheard.start()

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
	movingWindow.update(events, screen)
	for event in events:
		if event.type==pygame.QUIT:
			pygame.quit(); sys.exit()

	draw(events, round(clock.get_fps(), 2))

	
		
	