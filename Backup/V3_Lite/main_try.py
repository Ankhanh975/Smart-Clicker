import pyautogui, keyboard
import pygame
import array
from threading import Thread
import time, random, sys, os, math

from Vector2d import * # Class Vector
from instruction_loader import *
from O_Clicker import *
from O_Control import *
from Sub_Method import *

pyautogui.FAILSAFE = False

def GetData():
	file = "C:/src/Python/Smart Clicker/V3/instruction.yaml"
	data = LoadFile(file)
	lower_dict(data)
	checkSytax(data)
	return data

data = GetData()
Object=[]

O_control = Global()
def main():
	for _Object in data:
		if data[_Object] != "global":
			control.running_object +=1

		if data[_Object] == "global":
			for details in data[_Object]:
				if data["global"][details] == "kill":
					for x in data[_Object][details]:
						for y in x:
							if y 
					if data["global"][details] == "kill":
					if KeyPress
					O_control.KillCondition
				elif data["global"][details] == "start":
					O_control
				elif data["global"][details] == "o.logger":
					O_control

		elif data[_Object] == 'o.clicker': 
			Object.append(O_Clicker())
			Object[-1].TPS = data[_Object]["tps"]
			Object[-1].Name = data[_Object]["name"]
			for x in data[_Object]["clickevent"]:
				pass

			elif data[_Object] == "condition":
				for x in data[_Object]["condition"]:
					if data[_Object]["condition"] == "box":
						Object[-1].EventCondition.Box = data[_Object]["condition"]["box"]
					elif data[_Object]["condition"] ==	"activewindow":
						Object[-1].EventCondition.ActiveWindow = data[_Object]["condition"]["activewindow"]
					elif data[_Object]["condition"] ==	"o.switch":
						Object[-1].EventCondition.O_Switch = data[_Object]["condition"]["o.switch"]
					elif data[_Object]["condition"] ==	"keypress":
						Object[-1].EventCondition.KeyPressCondition = data[_Object]["condition"]["o.switch"]

			elif data[_Object] == "kill":
				for x in data[_Object]["kill"]:
					if data[_Object]["kill"] == "box":
						Object[-1].KillCondition.Box = data[_Object]["kill"]["box"]
					elif data[_Object]["kill"] ==	"activewindow":
						Object[-1].KillCondition.ActiveWindow = data[_Object]["kill"]["activewindow"]
					elif data[_Object]["kill"] ==	"o.switch":
						Object[-1].KillCondition.O_Switch = data[_Object]["kill"]["o.switch"]
			elif data[_Object] == "TimePrecise":
				Object[-1].Name = data[_Object]["Name"]
			elif data[_Object] == "PosPrecise":
				Object[-1].Name = data[_Object]["Name"]
			elif data[_Object] == "ClickSound":
				Object[-1].Name = data[_Object]["Name"]
		
		elif data[_Object] == "o.recorder":

	while True:
		for x in range(len(data)):
			data[x].Update()
			
		control.Update()

			
			
def Listener():
	class KeyPressed:
		def __init__(self):
			from pynput.keyboard import Key, Listener
			self.PressedKey = []

			with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
				#Detect max of 6 key
				listener.join()

		def Event(self, key, state):
			if state==1 and (key not in self.PressedKey):
				self.PressedKey.append(key)
			elif state==0:
				if key in self.PressedKey:
					self.PressedKey.remove(key)

			O_control.Global_HoldKey = self.PressedKey

		def on_press(self, key):
			self.Event(str(key), 1)

		def on_release(self, key):
			self.Event(str(key), 0)

	Ob = KeyPressed() 

if __name__ == '__main__':
	Thread(target = main())
    Thread(target = Listener())


