import pygame
import random
import time
from os import system as OsCmdControl
from sys import exit as TheadExit
from threading import Thread
from win32api import keybd_event as Control_KeyBoard
import win32gui
import win32api
from datetime import datetime
import win32con  # For win32gui argument
import pynput

import UserInput
import O_Clicker
import resorce
import _List
import MinecraftWriteChat
import ReadMinecraftChat

# TODO: Color console


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
        TheadExit()  # Stop everything beause no thread started yet
    else:
        OsCmdControl("title "+"Auto Clicker")

    if CheckOpen() == False:
        pass
        # OsCmdControl("C:\\Users\\Admin\\Documents\\Bi\\MinecraftLauncher.exe") #Free Minecraft
        # OsCmdControl('"C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"') #Mojang Minecraft
        # OsCmdControl("C:\\Users\\Admin\\Documents\\Bi\\MinecraftLauncher.exe") #Free Minecraft
        # OsCmdControl('"C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"') #Mojang Minecraft

        # OsCmdControl('"C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"') #Brave Bwroser
        # OsCmdControl('"C:\\Program Files (x86)\\Bandicam\\bdcam.exe"') #Bandicam
        # OsCmdControl("taskmgr") #Task Manager
        # OsCmdControl("explorer C:\\src\\Python\\Smart Clicker\\V4_1_thread") #File Explorer to a address
        # OsCmdControl("explorer C:\\src\\Python\\Smart Clicker\\V4_1_thread") #File Explorer (Default)
        # OsCmdControl("explorer C:\\Users\\Admin\\Desktop\\Bi") #File Explorer to a address


class Suond:
    def __init__(self):  # A place to save all suond
        pygame.mixer.init(44100, -16, 2, 64)
        # TODO: loop sound with getter in aready suond lib
        self.PressSound = pygame.mixer.Sound("Resources/Press2.mp3")
        self.PressSound.set_volume(0.15)
        self.PressSound.fadeout(50)
        # TODO: loop sound with getter in aready suond lib
        self.ClickSound = pygame.mixer.Sound("Resources/Press2.mp3")
        self.ClickSound.set_volume(0.15)
        self.ClickSound.fadeout(50)
        self.ExitSound = pygame.mixer.Sound("Resources/Press1.mp3")
        self.ErrorSound = pygame.mixer.Sound("Resources/Error_Sound.mp3")
        self.ErrorSound.set_volume(0.15)
        self.ErrorSound.fadeout(50)


O_Sound = Suond()
userInput = UserInput.GetInput()



class RunThread:
    stop = False
    error = False
    measureTime = time.perf_counter()
    measureFPS = 10

    def __init__(self, name: str, FPS=[13, 17], WindowCondition: str = ""):
        self.clock = pygame.time.Clock()
        self.name = name
        if type(FPS) == int or type(FPS) == float:
            self.FPSMin = self.FPSMax = FPS
        elif type(FPS) == list or type(FPS) == tuple:
            self.FPSMin = min(FPS[0], FPS[1])
            self.FPSMax = max(FPS[0], FPS[1])

    def loop(self):
        if self.FPSMin == self.FPSMax:
            while self.stop == False:
                self.clock.tick(self.FPSMin)
                self.Stuff()
        else:
            while self.stop == False:
                RunFPS = random.uniform(self.FPSMin, self.FPSMax)
                self.clock.tick(RunFPS)
                self.Stuff()

    def Stuff(self):
        pass

    def get_fps(self):  # Update every 1 / 1.4 s
        if time.perf_counter()-self.measureTime > 1/1.4:
            self.measureFPS = self.clock.get_fps()
            self.measureTime = time.perf_counter()
            if self.measureFPS < 2.5:
                self.measureFPS = round(self.measureFPS, 1)
            elif self.measureFPS > 150:
                self.measureFPS = ruondToEven(self.measureFPS)
            else:
                self.measureFPS = round(self.measureFPS)

        return self.measureFPS

    def debug(self):
        print("Clock:", self.clock)
        print("FPS:", [self.FPSMin, self.FPSMax], "Intended FPS:",
              self.RunFPS, "Real FPS:", self.get_fps())
        print("Name:", self.name)
        print()


def ruondToEven(x):
    return round(x/2.)*2


def ruondTo5(x):
    return round(x/5.)*5


'''if self.measureFPS < 10: #Round to .2
			self.measureFPS = round(self.clock.get_fps(), 1)*10
			self.measureFPS = ruondToEven(self.measureFPS)/10
		elif self.measureFPS < 70: #Round to 1.0
			self.measureFPS = round(self.clock.get_fps())
		elif self.measureFPS < 140: #Round to 2.0
			self.measureFPS = ruondToEven(self.measureFPS)
		else: #Round to 5.0
			self.measureFPS = ruondTo5(self.measureFPS)

		if self.measureFPS/self.FPSMin < 0.8:
			self.measureFPS = f"{self.measureFPS}!"'''
