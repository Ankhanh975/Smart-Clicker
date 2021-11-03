# Interact with Minecraft 1.8.9
import numpy as np
import winAPI


class OnChatMessage():
    file = "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log"
    sleepTime = 0
    stop = False

    def __init__(self):
        self.id = []
        self.chatHistory = []
        self.chatHistory.append(text)

    def addListener(self, callback):
        self.id.append(id(callback))

    def hasListener(self, callback):
        if (id(callback) in self.id):
            return True
        else:
            return False

    def removeListener(self, callback):
        self.id.remove(id(callback))
    callback(self.chat)


class Minecraft:
    def __init__(self):
        self.onChatMessage = OnChatMessage()

    def chat(self, text="."):
        # Type text: str to Minecraft console
        # Release all potentiality key can mess thing up then press back
        for i in MinecraftAutoChatUserInput.Global_HoldKey:
            winAPI.Sleepp(1/500)

            try:
                Control_KeyBoard(
                    _List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
            except KeyError as p:
                print(p)
        # Open chat
        winAPI.press("/")
        # Sleep so minecraft can progress
        winAPI.Sleepp(1/20)
        if text == -1:
            # -1 = last command send
            winAPI.press("up_arrow")
            winAPI.Sleepp(1/500)

        elif type(text) == str:
            # Open chat
            if text[0] == "/":
                text = text[1:]
                winAPI.typer(text)
            else:
                winAPI.Sleepp(0.004)
                winAPI.press("backspace")
                winAPI.Sleepp(1/500)
                winAPI.typer(text)

        # Close chat
        winAPI.press("enter")
        winAPI.Sleepp(1/25)

        for i in MinecraftAutoChatUserInput.Global_HoldKey:
            winAPI.Sleepp(1/500)
            try:
                Control_KeyBoard(_List.VK_CODE[i], 0, 0, 0)
            except KeyError as p:
                print(p)

    def isFocused(self):
        from win32gui import GetWindowText, GetForegroundWindow
        if "Minecraft 1.8.9" in GetWindowText(GetForegroundWindow()):
            return True
        else:
            return False

    def takeScreenShot(self):
        return np.array(1920, 1080)


minecraft = Minecraft()
def onChatMessage(self):
    print("onChatMessage", self.text)
    print("onChatMessage", self.history)
    

minecraft.onChatMessage.addListener(onChatMessage)
