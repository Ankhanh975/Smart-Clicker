import pygame, random
import UserInput, Condition, O_Clicker
import os,sys
from threading import Thread

exKey = ["f4"]

pygame.mixer.init(44100, -16, 2, 64)
os.system("mode con cols=32 lines=15")
os.system("title "+"Auto Clicker")
os.system("color 21")
#os.system("C:\\Users\\Admin\\Documents\\Bi\\MinecraftLauncher.exe")

P_State1 = P_Switch1 = P_State2 = P_Switch2 = ""
userInput = UserInput.GetInput()
userInput.NeedCheckedKey =  ["control", "x", "f4", "c", "mbutton"] 

import itertools
class ClickSound:
	def __init__(self):
		self.type = [""]
		self.Sound = self.Load()
		self.ClickIndex = itertools.cycle(range(1,18)) # Run Sound sample from 0 to 19 and angain
		self.Play = itertools.cycle(range(2))
		

	def Load(self):
		ClickSound = []
		for x in range(1, 20):
			a=pygame.mixer.Sound("Resources/Sample "+str(x)+".mp3")
			a.set_volume(0.001)
			ClickSound.append(a)
		return ClickSound
	def play(self):
		if next(self.Play):
			self.Sound[next(self.ClickIndex)].play()
def Print():

	describe = " Press Ctrl+X to change state,	 F4 to exit"
	global P_State1, P_Switch1, P_State2, P_Switch2, exKey, userInput
	ExSound=pygame.mixer.Sound("Resources/Press1.mp3")
	clock = pygame.time.Clock()
	a=""
	frame = 0
	while True:
		frame+=1
		if userInput.IsPressed(exKey):
			ExSound.play()
			sys.exit() # not run userInput.Update so 2 main theard never miss exit
		clock.tick(30)
		userInput.Update(frame)

		a1 = describe + "\n"
		a2 = " Thead1: "+  P_Switch1 + ", " + P_State1 + "\n"
		a3 = " Thead2: "+  P_Switch2 + ", " + P_State2 + "\n"
		a4 = " Input: "+ str(userInput.Global_HoldKey) + "\n"
		#a5 = userInput.Global_OnActiveWindow
		a5 = ""
		if a!=a1+a2+a3+a4+a5:
			a=a1+a2+a3+a4+a5
			os.system('cls')
			print(a)

def Thead1():
	global P_State1, P_Switch1, userInput, exKey

	fps = [14.5, 17]
	Switch = Condition.Switch(["control", "x"])
	
	activeButton = "mbutton"
	eventButton = "lbutton"

	clock = pygame.time.Clock()
	clickSound = ClickSound()
	while True:
		FPS = round(random.uniform(fps[0], fps[1]), 1)
		clock.tick(FPS)
		
		Switch.Update(userInput)
		if userInput.IsPressed(exKey):
			break
		if userInput.IsPressed([activeButton]) and Switch.GetState():
			O_Clicker.fastclick(userInput, eventButton)
			#clickSound.play()

		P_State1 = "Done: " + ("Clicked" if userInput.IsPressed([activeButton]) and Switch.GetState() else "None   ")
		P_Switch1 = "St: " + ("On " if Switch.GetState() else "Off")

		#os.system('cls')
		#print("Thead1,",  P_Switch1, ",", P_State1)

def Thead2():
	global P_State2, P_Switch2, userInput, exKey
	fps = [12, 13]
	Switch = Condition.Switch(["control", "x"], False)
	activeButton = "c"
	eventButton = "rbutton"

	clock = pygame.time.Clock()
	
	while True:
		FPS = round(random.uniform(fps[0], fps[1]), 1)
		clock.tick(FPS)
		
		Switch.Update(userInput)
		if userInput.IsPressed(exKey):
			break
		if userInput.IsPressed([activeButton]) and Switch.GetState():
			O_Clicker.fastclick(userInput, eventButton)


		P_State2 = "Done: " + ("Pressed" if userInput.IsPressed([activeButton]) and Switch.GetState() else "None   ")
		P_Switch2 = "St: " + ("On " if Switch.GetState() else "Off")

		#os.system('cls')
		#print("Thead2,",  P_Switch2, ",", P_State2)

Thread(target = Thead1).start()
Thread(target = Thead2).start()
Thread(target = Print).start()