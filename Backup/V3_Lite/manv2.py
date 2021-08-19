import pyautogui, keyboard
import pygame
import array
import time, random, sys, os, math

from Vector2d import * # Class Vector
from instruction_loader import *
from O_Clicker import *
from O_Global import *
from Sub_Method import *

pyautogui.FAILSAFE = False

def GetData(file = "instruction.yaml"):
	data = LoadFile(file)
	lower_dict(data)
	#checkSytax(data)

	return data

if len(sys.argv) == 1: #If input in cmd with 1 parameter is instruction file then loat that instead
	data = GetData()
else:
	data = GetData(sys.argv[1])

#print(KeyboardInUse(data))

Object = []
for x in data:
	if x== "global":
		O_control = Loadyaml.Load_O_Global(data[x])
		O_control.NeedCheckedKey = KeyboardInUse(data)

	elif x== "o.clicker":
		#print(data[x])
		Object.append(Loadyaml.Load_O_Clicker(data[x]))

if __name__ == '__main__':
	while True:
		O_control.Update()
		#print(O_control.Global_HoldKey,  O_control.Global_MousePos)
		#print(O_control.KillCondition.KeyPressCondition)
		print(Object[0].EventCondition)
		#print(O_control.KillCondition, Object[0].KillCondition)
		for x in range(len(Object)):
			Object[x].Update(O_control.Global_HoldKey, O_control.Global_MousePos, O_control.Global_ActiveWindow)