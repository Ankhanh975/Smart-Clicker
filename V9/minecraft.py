# Interact with Minecraft 1.8.9
import numpy as np


class Minecraft:
    def __init__(self):
        pass

    def chat(self, text="."):
        # Type text: str to Minecraft console
        if text == -1:
			# -1: last command send
			

    def isFocused(self):
        return True

    def takeScreenShot(self):
        return np.array(1920, 1080)

    def onChatMessage(self, callback):
        callback(self.chat)


minecraft = Minecraft()

