import pygame, random
import UserInput, Condition, O_Clicker
from os import system as OsCmdControl
from sys import exit as TheadExit
from threading import Thread
import win32api, win32con

exKey = "f4"
describe = " Press Ctrl+X to change state,	 F4 to exit" + "\n"

def setup():
	pygame.mixer.init(44100, -16, 2, 64)
	OsCmdControl("mode con cols=32 lines=15")
	OsCmdControl("title "+"Auto Clicker")
	OsCmdControl("color 21")

	def CheckOpen(Window: str = "Minecraft 1.8.9"):
		AllWin = UserInput.GetInput().list_window_names()
		AllWin = str(AllWin)
		print(AllWin)

		
		if "Minecraft" in AllWin:
			return True
		'''for a in AllWin:
			if Window in a:
				return True'''
		return False


	if CheckOpen()==False:
		OsCmdControl("C:\\Users\\Admin\\Documents\\Bi\\MinecraftLauncher.exe")

setup()

P_State1 = P_Switch1 = P_State2 = P_Switch2 = ""
userInput = UserInput.GetInput()
userInput.NeedCheckedKey =  ["control", "x", "f4", "c", "mbutton", "lbutton", "rbutton"] 

def Control():
	global P_State1, P_Switch1, P_State2, P_Switch2, exKey, userInput
	ExSound=pygame.mixer.Sound("Resources/Press1.mp3")
	clock = pygame.time.Clock()
	a=""
	frame = 0
	while True:
		frame+=1
		if userInput.IsPressed([exKey]):
			ExSound.play()
			TheadExit() # not run userInput.Update so 2 main theard never miss exit
		clock.tick(30)
		userInput.Update(frame)

		if userInput.IsPressed(["lbutton", "rbutton"]):
			win32api.keybd_event(0x5A, 0, 0, 0)
		else:
			win32api.keybd_event(0x5A, 0, win32con.KEYEVENTF_KEYUP ,0)

		a1 = describe 
		a2 = "Thead1| "+  P_Switch1 + ", " + P_State1 + "\n"
		a3 = "Thead2| "+  P_Switch2 + ", " + P_State2 + "\n"
		a4 = " Input: "+ str(userInput.Global_HoldKey) + "\n"
		#a5 = userInput.Global_OnActiveWindow
		a5 = ""
		if a!=a1+a2+a3+a4+a5:
			a=a1+a2+a3+a4+a5
			OsCmdControl('cls')
			print(a)


def Thead1():
	global P_State1, P_Switch1, userInput, exKey

	fps = [14.5, 17]
	Switch = Condition.Switch(["control", "x"])
	
	activeButton = "mbutton"
	eventButton = "lbutton"

	clock = pygame.time.Clock()
	while True:
		FPS = round(random.uniform(fps[0], fps[1]), 1)
		clock.tick(FPS)
		
		Switch.Update(userInput)
		if userInput.IsPressed([exKey]):
			TheadExit()
		if userInput.IsPressed([activeButton]) and Switch.GetState():
			O_Clicker.fastclick(userInput, eventButton)

		P_State1 = "Done: " + ("Clicked" if userInput.IsPressed([activeButton]) and Switch.GetState() else "None   ")
		P_Switch1 = "St: " + ("On " if Switch.GetState() else "Off")

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
		if userInput.IsPressed([exKey]):
			TheadExit()
		if userInput.IsPressed([activeButton]) and Switch.GetState():
			O_Clicker.fastclick(userInput, eventButton)


		P_State2 = "Done: " + ("Pressed" if userInput.IsPressed([activeButton]) and Switch.GetState() else "None   ")
		P_Switch2 = "St: " + ("On " if Switch.GetState() else "Off")


Thread(target = Thead1).start()
Thread(target = Thead2).start()
Thread(target = Control).start()