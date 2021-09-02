# 24/07/2021 : project have 1095 line of code
from _main import *

# TODO: sound: sound bật sẽ vút lên cao độ (dễ phân biệt)
# TODO: sound: sound tắt sẽ vút xuống cao đo

CommonChat = ["/is home", "/is value", "/warp spawn", "/adventure", "/ah "]
CommonChat = ["/pm ", "/reply", "/kill"]

title = "Auto Clicker"
exKey = "f4"
describe = '''#Minecraft Bedwars Mode 
Ctrl+x to stop, F4 to exit
Left+Right button to zoom
'''
setup()
# TODO: change FPS realtime (Performance), error log


class ClickerThread(RunThread):
	done = "Na"

	def __init__(self, name: str, FPS, Switch_Condition, Condition_Button: str, Event_Button: str):
		super().__init__(name, FPS)
		self.Switch_Condition = Switch_Condition
		self.Condition_Button = [Condition_Button]
		self.Event_Button = Event_Button

		self.Switch = UserInput.Switch(Switch_Condition)
		self.Switch._Event()

	def Stuff(self):
		self.Switch.Update(userInput)
		self.done = "Na"

		# if userInput.Global_OnActiveWindow != "Minecraft 1.8.9":
		# return
		# if not LogReader.allowClick:
		#	return
		if userInput.IsPressed(self.Condition_Button) and self.Switch.GetState() == True:
			if userInput.Global_OnActiveWindow == title:
				if userInput.IsPressed(self.Condition_Button) and self.Switch.GetState() == True:
					O_Sound.ClickSound.play()
					self.done = "Spam!"
				return
			else:
				self.done = "Clicked"
				O_Clicker.fastclick(UserInput, self.Event_Button)

	def WarningRelaese(self):
		pass

	def info(self):
		State = "On" if self.Switch.GetState() else "Off"
		State = f"({State})"
		# if userInput.Global_OnActiveWindow != "Minecraft 1.8.9" and State=="(On)":
		#	State= "On" if self.Switch.GetState() else "Off"
		#	State = "("+State+"| Outsize Minecraft"+")"
		#	return State, ""

		FPS = self.get_fps()
		FPS = f"{FPS} CPS"

		Done = "Done: " + (FPS if self.done == "Clicked" else self.done)
		if State == "(Off)":
			Done = ""
		return State, Done


class HighPerformStuff(RunThread):
	frame = 0
	inzoom = False

	def __init__(self, FPS=60):
		super().__init__("HighPerformStuff", FPS)

	def Stuff(self):
		self.frame += 1
		userInput.Update(self.frame)

		def zoom():
			if "Minecraft" not in userInput.Global_OnActiveWindow:
				#print("Outsize Minecraft, so don't zoom")
				return
			if userInput.IsPressed(["lbutton", "rbutton"]):
				self.inzoom = True
				if not userInput.IsPressed(["z"]):
					Control_KeyBoard(0x5A, 0, 0, 0)
			elif self.inzoom == True:
				self.inzoom = False
				Control_KeyBoard(0x5A, 0, win32con.KEYEVENTF_KEYUP, 0)

		zoom()


def WhatToChat(LogReader, KeyPressed: int, mode=["Bedwars", "Skyblock"][0]):
	if "3fmc Bedwars Mode" not in LogReader.Mode:  # Not in mincraft bedwar game
		return ""

	def NowAndLogTime(LogTime):
		now = datetime.now()
		LogTime = datetime.now()
		return 0  # in minnite
	print()
	if KeyPressed == 1:
		if LogReader.KILL != 0 and LogReader.DIED != 0:
			if now - LogReader.LastDEAD < 4:
				pass
			if LogReader.KILL / LogReader.DIED < 1.2:
				return random.choice(["@cc?", "@lag ..."])
			elif 1.7 > LogReader.KILL / LogReader.DIED > 1.2:
				return random.choice(["@haha", "@@ghe qua co"])
			elif 2.0 < LogReader.KILL / LogReader.DIED:
				return random.choice(["@haha", "@hay lam"])
	elif KeyPressed == 2:
		PlayedTime = NowAndLogTime(LogReader.GameStartedTime)

		if PlayedTime < 0.6:
			if LogReader.Up_KIEM == False:
				return random.choice(["Ai lay kc, up KIEM?", "nho up KIEM, GIAP nhe", "up IT TRAP pls", "up KIEM pls"])
			elif LogReader.IT_TRAP == 0:
				return random.choice(["up IT TRAP di "])

		elif 0.6 < PlayedTime < 4.5:
			return random.choice(["up KIEM pls", "up KIEM nhanh nhe", "up KIEM pls"])
		elif PlayedTime > 4.5:
			return random.choice(["up KIEM pls", "up KIEM nhanh len", "cc kc dau? up KIEMMM", "up KIEMMM cc"])
		elif PlayedTime > 6:
			return random.choice(["up KIEM pls", "up KIEM nhanh len", "cc kc dau? up KIEMMM", "up KIEMMM cc"])


def WhatToChat(LogReader, KeyPressed: int, mode=["Bedwars", "Skyblock"][0]):
	print(LogReader, KeyPressed)
	if KeyPressed == 2:
		if LogReader.Up_KIEM == False:
			return ["up KIEM pls", "up KIEM pls", "up KIEM pls", "up KIEM pls", "up KIEM"]
		else:
			if LogReader.Up_GIAP == 3:
				return ["up GIAP IV nua"]
			elif LogReader.Up_GIAP == 2: 
				return ["up GIAP III nua pls", "ai lay kc up GIAP III ho"]
			else:
				return ["up GIAP pls"]
	elif KeyPressed == 3:
		if LogReader.ACTIVE_IT_TRAP == None:
			return ["ai bed?", "ai bed?", "ai bed day", "bed di nhe"]
		else:
			return ["bed lai di", "bed 1 lop nua vcl", "bed 1 lop nua di"]
	elif KeyPressed == 1:
		return ["@hmm", "@toan pro ", "@tha t", "@c", "@cc?", "@?"]
	elif KeyPressed == 4:
		return ["no qua bed kia", "ve.", "bed", "no qua", "no"]
	elif KeyPressed == 5:
		return ["@gg", "@good", "@non", "@gg/"]
	elif KeyPressed == 6:
		return ["/leave"]
	elif KeyPressed == 0:
		return
	else:
		raise ValueError()


class LowPerformStuff(RunThread):
	"up KIEM nhanh pls"  # sau 5p
	"up KIEM nhanh cc"  # sau 10p
	"up GIAP di, no trau vcl"

	def __init__(self, FPS=30):
		super().__init__("LowPerformStuff", FPS)

	def Stuff(self):
		if userInput.IsPressed([exKey]):
			O_Sound.ExitSound.play()
			Thread1.stop = True
			Thread2.stop = True
			Console_Controller.stop = True
			HighPerformanceStuff.stop = True
			LowPerformanceStuff.stop = True
			LogReader.stop = True

		if userInput.IsPressed(["control", "l"]):
			Control_KeyBoard(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
			Control_KeyBoard(0x4C, 0, win32con.KEYEVENTF_KEYUP, 0)
			MinecraftWriteChat.MinecraftAutoChat("/l ak2006@@")
			time.sleep(1/3.5)
			O_Clicker.fastclick("mbutton")
			return 

		for i in range(1, 7):
			if userInput.IsPressed(["numpad"+str(i)]):
				Control_KeyBoard(97+i-1, 0, win32con.KEYEVENTF_KEYUP, 0)

				CHAT = WhatToChat(LogReader, i)
				CHAT = random.choice(CHAT)
				MinecraftWriteChat.MinecraftAutoChat(CHAT)

		if userInput.IsPressed(["numpad0"]):
			Control_KeyBoard(96, 0, win32con.KEYEVENTF_KEYUP, 0)
			MinecraftWriteChat.doLastCommand()


class Screen(RunThread):
	lastThread1Info = None
	lastThread2Info = None
	description = describe

	def __init__(self, title: str = title, winsize: list = [32, 15], FPS=30):
		super().__init__("ConsoleController", FPS)
		self.title = title
		self.winsize = winsize
		self.PixelwinSize = (280, 279)
		self.FPS = FPS

		#OsCmdControl("mode con cols="+str(self.winsize[0])+" lines="+str(self.winsize[1]))
		OsCmdControl("color 2d")
		OsCmdControl("title "+title)
		self.hwnd = win32gui.FindWindow(None, title)
		# self.SelfResize()

	def Stuff(self):
		Thread1Info = Thread1.info()
		Thread2Info = Thread2.info()

		if Thread1Info == self.lastThread1Info and Thread2Info == self.lastThread2Info:
			return
		else:
			self.lastThread1Info = Thread1Info
			self.lastThread2Info = Thread2Info
			if Thread1.error == False and Thread2.error == False and Console_Controller.error == False and HighPerformanceStuff.error == False and LowPerformanceStuff.error == False:
				# OsCmdControl("cls")
				pass
			else:  # Have some error
				pass
			# print(self.description)
			print("Minecraft Bedwars Mode")
			print("Thead1", Thread1Info[0], "| ", Thread1Info[1], sep="")
			print("Thead2", Thread2Info[0], "| ", Thread2Info[1], sep="")
			print

	def SelfResize(self):  # TODO: Performance
		x0, y0, x1, y1 = win32gui.GetWindowRect(self.hwnd)
		win32gui.MoveWindow(self.hwnd, x0, y0,
							self.PixelwinSize[0], self.PixelwinSize[1], True)


Console_Controller = Screen()
LogReader = ReadMinecraftChat.ReadMinecreaftLog()
HighPerformanceStuff = HighPerformStuff()
LowPerformanceStuff = LowPerformStuff()
Thread1 = ClickerThread("LeftClick", [14.5, 17.5], [
						"shift", "x"], "mbutton", "lbutton")
Thread2 = ClickerThread("RightClick", [13.5, 15.5], [
						"shift", "x"], "c", "rbutton")
Thread2.Switch.playsuond = False

#scrollTheard = UserInput.getMinecraftSlot()
# scrollTheard.start()


Thread(target=Console_Controller.loop).start()
Thread(target=LogReader.loop).start()
Thread(target=Thread1.loop).start()
Thread(target=Thread2.loop).start()
Thread(target=HighPerformanceStuff.loop).start()
Thread(target=LowPerformanceStuff.loop).start()


def Getinput():
	while True:
		a = input("")
		a = a.lstrip().rstrip()
		if a != "":
			print(f"You input: {a}")


Thread(target=Thread1.loop, daemon=True).start()
