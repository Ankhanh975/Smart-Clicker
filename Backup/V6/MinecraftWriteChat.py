import UserInput, resorce
MinecraftAutoChatUserInput = UserInput.GetInput()
import _List
from win32api import keybd_event as Control_KeyBoard
import win32con #For win32gui argument

def MinecraftAutoChat(text: str="."): #TODO: chat dc tiếng việt, đọc được chat 
#TODO: 
	#Release all potentiality key can mess thing up
	MinecraftAutoChatUserInput.Update(0)
	for i in MinecraftAutoChatUserInput.Global_HoldKey:
		resorce.Sleepp(1/500) 

		try:
			Control_KeyBoard(_List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP ,0)
		except KeyError as p:
			print(p)

			#O_Sound.ErrorSound.play()

	#Open chat
	resorce.press("/")
	resorce.Sleepp(1/19.5) #Sleep so minecraft can progress
	resorce.press("backspace")

	resorce.typer(text) #Really write text

	#Close chat
	resorce.press("enter")
	resorce.Sleepp(1/20.5) #Sleep so minecraft can progress

	for i in MinecraftAutoChatUserInput.Global_HoldKey:
		resorce.Sleepp(1/500) 
		try:
			Control_KeyBoard(_List.VK_CODE[i], 0, 0 ,0)
		except KeyError as p:
			print(p)

import win32api, win32clipboard

def Set_Clip_Board(txt: str):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(txt, win32clipboard.CF_UNICODETEXT)
	win32clipboard.CloseClipboard()

def Read_Clip_Board():
	try:
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		return data
	except TypeError as p:
	    return ""

#https://stackoverflow.com/questions/7050448/write-image-to-windows-clipboard-in-python-with-pil-and-win32clipboard

