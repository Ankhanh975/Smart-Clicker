# Interact with Minecraft 1.8.9
import numpy as np
import win

class Minecraft:
    def __init__(self):
        pass

    def chat(self, text="."):
        # Type text: str to Minecraft console
		# Release all potentiality key can mess thing up then press back
		for i in MinecraftAutoChatUserInput.Global_HoldKey:
			resorce.Sleepp(1/500) 

			try:
				Control_KeyBoard(_List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
			except KeyError as p:
				print(p)
        if text == -1:
			# -1: last command send
			
			#Open chat
			resorce.press("/")
			resorce.Sleepp(1/20) 
			resorce.press("up_arrow")
			resorce.Sleepp(1/500) 
			#Close chat
			resorce.press("enter")
			resorce.Sleepp(1/25) #Sleep so minecraft can progress

			for i in MinecraftAutoChatUserInput.Global_HoldKey:
				resorce.Sleepp(1/500) 
				try:
					Control_KeyBoard(_List.VK_CODE[i], 0, 0 ,0)
				except KeyError as p:
					print(p)
		else:
			
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
			if text[0] =="/":

				text = text[1:]
				resorce.Sleepp(1/22) #Sleep so minecraft can progress
				resorce.typer(text)
			else:
				resorce.Sleepp(1/18.5) #Sleep so minecraft can progress
				resorce.press("backspace")
				resorce.Sleepp(1/500) #Sleep so minecraft can progress

				resorce.typer(text) #Really write text

			#Close chat
			resorce.press("enter")
			resorce.Sleepp(1/30) #Sleep so minecraft can progress

		for i in MinecraftAutoChatUserInput.Global_HoldKey:
			resorce.Sleepp(1/500) 
			try:
				Control_KeyBoard(_List.VK_CODE[i], 0, 0 ,0)
			except KeyError as p:
				print(p)

    def isFocused(self):
        return True

    def takeScreenShot(self):
        return np.array(1920, 1080)

    def onChatMessage(self, callback):
        callback(self.chat)


minecraft = Minecraft()

