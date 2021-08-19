# Being import as global read-only object thread to all file and thread
# This get all input from keyboard, mouse, active window, ...
import pygame
import win32gui
import win32api


def __init__():
    global userInput
    userInput = UserInput.GetInput()


class GetInput():
    def __init__(self):
        import pyautogui
        self.screenSize = [pyautogui.size()[0], pyautogui.size()[1]]
        self.NeedCheckedKey = []

        self.Global_HoldKey = []
        self.Global_MousePos = [-1, -1]
        self.Global_ActiveWindow = []
        self.Global_OnActiveWindow = "None"

    def Update(self, frame):
        self.Global_MousePos = win32gui.GetCursorInfo()[2]
        #self.Global_MousePos = (0,0)
        self.Global_OnActiveWindow = win32gui.GetWindowText(
            win32gui.GetForegroundWindow())
        self.Global_HoldKey = self.getKeyState()
        if frame % 100 == 0:
            self.Global_ActiveWindow = self.list_window_names()

    def IsPressed(self, CheckKeyStrokes):
        for x in CheckKeyStrokes:
            if x not in self.Global_HoldKey:
                return False
        return True

    def getKeyState(self):
        keyPressed = []
        if self.NeedCheckedKey == []:
            for x in range(256):
                a = win32api.GetKeyState(x)
                if a < 0 and _List.VK_CODE_REVERSE[x] != None:
                    keyPressed.append(_List.VK_CODE_REVERSE[x])
        else:
            for x in self.NeedCheckedKey:
                a = win32api.GetKeyState(_List.VK_CODE[x])
                if _List.VK_CODE[x] != None:
                    if a < 0:
                        keyPressed.append(x)
                else:
                    print(self.NeedCheckedKey, keyPressed, x,
                          "What wrong?, why you requst a None keyNumber ")
        return keyPressed

    def list_window_names(self):
        All = []

        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                Wintitle = win32gui.GetWindowText(hwnd)
                if Wintitle != "" and Wintitle not in All:
                    if Wintitle not in ["Program Manager", "Settings"]:
                        All.append(Wintitle)
        win32gui.EnumWindows(winEnumHandler, None)
        return All

    def __str__(self):
        return f"Global_ActiveWindow: {self.Global_OnActiveWindow}, Global_HoldKey:  {self.Global_HoldKey}, Global_MousePos: {self.Global_MousePos}"


class Switch:
    def __init__(self, KeyPressEvent=[], playsuond=True):
        self.SwitchEvent = list(KeyPressEvent)
        self.playsuond = playsuond
        self.TwoLastState = [False, False]
        self.State = False

        def LoadSound():
            a = pygame.mixer.Sound("Resources/On.mp3")
            a.set_volume(0.15)
            a.fadeout(50)
            b = pygame.mixer.Sound("Resources/Off.mp3")
            b.set_volume(0.15)
            b.fadeout(50)
            return [a, b]
        self.Sound = LoadSound()

    def Update(self, GlobalInput):
        if self.SwitchEvent != [] and GlobalInput.IsPressed(self.SwitchEvent):
            Now = True
        else:
            Now = False
        self.TwoLastState = [self.TwoLastState[1], Now]

        if self.TwoLastState == [False, True]:
            self._Event()

    def _Event(self):
        self.State = not self.State
        if self.playsuond:
            self.Sound[0 if self.State == True else 1].play()

    def GetState(self):
        return int(self.State)

# class getMinecraftSlot:
# 	scroll = 0
# 	def __init__(self):
# 		self.listener = mouse.Listener(on_scroll=self.on_scroll)

# 	def start(self):
# 		self.listener.start()

# 	def on_scroll(self, _, __, ___, dy):
# 		self.scroll += dy
# 		#print(self.scroll)


if __name__ == "__main__":
    import time
    time.sleep(3)
    a = GetInput()
    for i in range(300):
        time.sleep(1/60)
        a.Update(i)
        print(a.Global_HoldKey)
