import pygame, random, time
from os import system as OsCmdControl
from sys import exit as TheadExit
from threading import Thread
from win32api import keybd_event as Control_KeyBoard
import win32con #For win32gui argument

import UserInput, Condition, O_Clicker
import resorce

# TODO: realtime read: C:\Users\Admin\AppData\Roaming\.minecraft\logs\latest.log
#to find chat

# TODO: Color cónsle
exKey = "f4"
describe = '''#Minecraft Bedwars Mode 
Press ctrl_r+x to pause all, F4 to exit
Hold left + right mouse for zoom  '''
CommonChat = [["@ghe qua ", "@ghe vay ", "@ghe vay ai choi "], "up KIEM pls", "ai bed?", "E, ve di bed kiaa", "@gg", "/leave"]

class Suond:
	def __init__(self): #A place to save all suond
		pygame.mixer.init(44100, -16, 2, 64)
		self.PressSound = pygame.mixer.Sound("Resources/Press2.mp3") #TODO: loop sound with getter in aready suond lib
		self.ClickSound = pygame.mixer.Sound("Resources/Press2.mp3") #TODO: loop sound with getter in aready suond lib
		self.ExitSound = pygame.mixer.Sound("Resources/Press1.mp3")
		self.ErrorSound = pygame.mixer.Sound("Resources/Error_Sound.mp3")
		self.ErrorSound.set_volume(0.15)
		self.ErrorSound.fadeout(50)
O_Sound = Suond()

CRED = '\033[91m'
CEND = '\033[0m'

def MinecraftAutoChat(text: str="."): #TODO: chat dc tiếng việt, đọc được chat 
#TODO: 
	#Release all potentiality key can mess thing up

	#Open chat
	resorce.press("/")
	O_Sound.PressSound.play()
	resorce.Sleepp(1/20.5) #Sleep so minecraft can progress
	resorce.press("backspace")

	resorce.typer(text) #Really write text

	#Close chat
	resorce.press("enter")

def setup():
	OsCmdControl("mode con cols=32 lines=15")
	OsCmdControl("cd C:\\src\\Python\\Smart Clicker\\V4_1_thread")
	OsCmdControl("color ac")

	def CheckOpen(Window: str = "Minecraft"):
		AllWin = UserInput.GetInput().list_window_names()
		AllWin = str(AllWin)
		if Window in AllWin:
			return True
		return False

	if CheckOpen("Auto Clicker")==True:
		OsCmdControl("title "+"Auto Clicker")
		OsCmdControl("mode con cols=30 lines=15")
		OsCmdControl("color ac")
		print("Already open this program.")
		O_Sound.ErrorSound.play()

		time.sleep(5)

		TheadExit() #Stop Everything beause nothing started yet
	else:
		OsCmdControl("title "+"Auto Clicker")

	if CheckOpen()==False: 
		pass
		#OsCmdControl("C:\\Users\\Admin\\Documents\\Bi\\MinecraftLauncher.exe") #Free Minecraft
		#OsCmdControl('"C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"') #Mojang Minecraft
 		
setup()

P_State1 = P_Switch1 = P_State2 = P_Switch2 = ""
userInput = UserInput.GetInput()
userInput.NeedCheckedKey =  ["control", "x", "f4", "c", "mbutton", "lbutton", "rbutton", "l","numpad_1","numpad_2","numpad_3","numpad_4","numpad_5","numpad_6"] 

def Control():
	global P_State1, P_Switch1, P_State2, P_Switch2, exKey, userInput
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
			Control_KeyBoard(0x5A, 0, 0, 0)
		else:
			Control_KeyBoard(0x5A, 0, win32con.KEYEVENTF_KEYUP ,0)

		if userInput.IsPressed(["control", "l"]):
			Control_KeyBoard(0x11, 0, win32con.KEYEVENTF_KEYUP ,0)
			Control_KeyBoard(0x4C, 0, win32con.KEYEVENTF_KEYUP ,0)
			MinecraftAutoChat("/l ak2006@@")

		for i in range(1, 7):
			if userInput.IsPressed(["numpad_"+str(i)]):
				Control_KeyBoard(97+i-1, 0, win32con.KEYEVENTF_KEYUP ,0)
				if type(CommonChat[i-1])==str:
					CHAT = CommonChat[i-1]
				elif type(CommonChat[i-1])==list:
					CHAT = random.choice(CommonChat[i-1])

				MinecraftAutoChat(CHAT)
				print(CHAT)

		a1 = describe 
		a2 = "Thead1| "+  P_Switch1 + ", " + P_State1 + "\n"
		a3 = "Thead2| "+  P_Switch2 + ", " + P_State2 + "\n"
		a4 = " Input: "+ str(userInput.Global_HoldKey) + "\n"
		a5 = userInput.Global_OnActiveWindow
		if a!=a1+a2+a3+a4+a5:
			a=a1+a2+a3+a4+a5
			OsCmdControl('cls')
			print(a)

			#print(CRED + "Error, does not compute!" + CEND)

	if frame%10==0:
		OsCmdControl("mode con cols=32 lines=15")

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