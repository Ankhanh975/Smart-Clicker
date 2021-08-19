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

def GetData():
	file = "C:/src/Pythovn/Smart Clicker/V3/instruction.yaml"
	data = LoadFile(file)
	print(data)
	lower_dict(data)
	checkSytax(data)
	return data

if __name__ == '__main__':
	O_control = Global()
	O_control.KillCondition.KeyPressCondition = ["f4"]
	Clicker = O_Clicker("Join", 30)
	Clicker.EventCondition.O_Switch.SwitchEvent = ["v"]
	Clicker.PosPrecise = 50

	while True:
		O_control.Update()

		print(Clicker.CreatedEvent)
		Clicker.Update(O_control.Global_HoldKey, O_control.Global_MousePos, O_control.Global_ActiveWindow)
