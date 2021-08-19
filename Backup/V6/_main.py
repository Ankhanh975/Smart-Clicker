import pygame, random, time
from os import system as OsCmdControl
from sys import exit as TheadExit
from threading import Thread
from win32api import keybd_event as Control_KeyBoard
import win32con #For win32gui argument

import UserInput, O_Clicker
import resorce
import _List
import MinecraftWriteChat

# TODO: realtime read: "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log to find chatClipBoard
# TODO: Color cónsle

def setup():
	def CheckOpen(Window: str = "Minecraft"):
		AllWin = UserInput.GetInput().list_window_names()
		AllWin = str(AllWin)
		if Window in AllWin:
			return True
		return False

	if CheckOpen("Auto Clicker"):
		print("Already open this program.")
		O_Sound.ErrorSound.play()

		time.sleep(5)
		TheadExit() #Stop everything beause no thread started yet
	else:
		OsCmdControl("title "+"Auto Clicker")

	if CheckOpen()==False: 
		pass
		#OsCmdControl("C:\\Users\\Admin\\Documents\\Bi\\MinecraftLauncher.exe") #Free Minecraft
		#OsCmdControl('"C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"') #Mojang Minecraft

class Suond:
	def __init__(self): #A place to save all suond
		pygame.mixer.init(44100, -16, 2, 64)
		self.PressSound = pygame.mixer.Sound("Resources/Press2.mp3") #TODO: loop sound with getter in aready suond lib
		self.PressSound.set_volume(0.15)
		self.PressSound.fadeout(50)
		self.ClickSound = pygame.mixer.Sound("Resources/Press2.mp3") #TODO: loop sound with getter in aready suond lib
		self.ClickSound.set_volume(0.15)
		self.ClickSound.fadeout(50)
		self.ExitSound = pygame.mixer.Sound("Resources/Press1.mp3")
		self.ErrorSound = pygame.mixer.Sound("Resources/Error_Sound.mp3")
		self.ErrorSound.set_volume(0.15)
		self.ErrorSound.fadeout(50)
		
O_Sound = Suond()
userInput = UserInput.GetInput()
