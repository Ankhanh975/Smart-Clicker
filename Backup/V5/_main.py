import pygame, random, time
from os import system as OsCmdControl
from sys import exit as TheadExit
from threading import Thread
from win32api import keybd_event as Control_KeyBoard
import win32con #For win32gui argument

import UserInput, Condition, O_Clicker
import resorce
import ClipBoard
import _List

# TODO: realtime read: C:\Users\Admin\AppData\Roaming\.minecraft\logs\latest.log to find chatClipBoard
# TODO: Color cónsle

def setup():
	OsCmdControl("mode con cols=32 lines=15")
	OsCmdControl("cd C:\\src\\Python\\Smart Clicker\\V4_1_thread")
	OsCmdControl("color 2d")

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

class Suond:
	def __init__(self): #A place to save all suond
		pygame.mixer.init(44100, -16, 2, 64)
		self.PressSound = pygame.mixer.Sound("Resources/Press2.mp3") #TODO: loop sound with getter in aready suond lib
		self.PressSound.set_volume(0.15)
		self.PressSound.fadeout(50)
		self.ClickSound = pygame.mixer.Sound("Resources/Press2.mp3") #TODO: loop sound with getter in aready suond lib
		self.ExitSound = pygame.mixer.Sound("Resources/Press1.mp3")
		self.ErrorSound = pygame.mixer.Sound("Resources/Error_Sound.mp3")
		self.ErrorSound.set_volume(0.15)
		self.ErrorSound.fadeout(50)
O_Sound = Suond()
userInput = UserInput.GetInput()

'''
def MinecraftAutoChat(text: str="."): 
#TODO: 
	#Release all potentiality key can mess thing up

	#Open chat
	resorce.press("/")
	

	#ClipBoard.Set_Clip_Board(text)
	O_Sound.PressSound.play()
	resorce.Sleepp(1/20.5) #Sleep so minecraft can progress, also do something

	resorce.press("backspace")
	resorce.Sleepp(1/100)
	
	#Really write text
	resorce.pressHoldRelease("control", "v")
	#resorce.typer(text) 

	resorce.Sleepp(1/100)
	#Close chat
	resorce.press("enter")
'''