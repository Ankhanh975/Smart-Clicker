from _main import *

#TODO: sound: sound bật sẽ vút lên cao độ (dễ phân biệt)
#TODO: sound: sound tắt sẽ vút xuống cao đo
#TODO: 
CommonChat = ["/is home" , "/is value" , "/warp spawn", "/adventure", "/ah "]

title = "Auto Clicker"
exKey = "f4"
describe = '''#Minecraft Bedwars Mode 
Ctrl+x to stop, F4 to exit
Left+Right button to zoom
'''
setup()
#TODO: change FPS realtime, error log
class RunThread:
	stop = False
	error = False
	def __init__(self, name: str, FPS=[13,17], WindowCondition: str=""):
		self.clock = pygame.time.Clock()
		self.name = name
		if type(FPS)==int or type(FPS)==float:
			self.FPSMin = self.FPSMax = FPS
		elif type(FPS)==list or type(FPS)==tuple:
			self.FPSMin = min(FPS[0], FPS[1])
			self.FPSMax = max(FPS[0], FPS[1])

	def loop(self):
		if self.FPSMin == self.FPSMax:
			while self.stop == False:
				self.clock.tick(self.FPSMin)
				self.Stuff()
		else:
			while self.stop == False:
				self.RunFPS = round(random.uniform(self.FPSMin, self.FPSMax), 2)
				self.clock.tick(self.RunFPS)
				self.Stuff()
	def Stuff(self):
		pass

	def get_fps(self):
		return round(self.clock.get_fps(), 2)

	def debug(self):
		print("Clock:", self.clock)
		print("FPS:", [self.FPSMin, self.FPSMax], "Intended FPS:", self.RunFPS, "Real FPS:", self.get_fps())
		print("Name:", self.name) 
		print()

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

		if userInput.Global_OnActiveWindow != "Minecraft 1.8.9":
			return
		if userInput.IsPressed(self.Condition_Button) and self.Switch.GetState()==True:
			if userInput.Global_OnActiveWindow == title:
				if userInput.IsPressed(self.Condition_Button) and self.Switch.GetState()==True:
					O_Sound.ClickSound.play()
					self.done = "Spam!"
				return
			else:
				self.done = "Clicked"
				O_Clicker.fastclick(UserInput, self.Event_Button)
	
	def WarningRelaese(self):
		pass
	def info(self):
		State= "On" if self.Switch.GetState() else "Off"
		State = "("+State+")"
		if userInput.Global_OnActiveWindow != "Minecraft 1.8.9" and State=="(On)":
			State= "On" if self.Switch.GetState() else "Off"
			State = "("+State+"| Outsize Minecraft"+")"
			return State, ""

		FPS = int(self.clock.get_fps())
		FPS = str(FPS) + " CPS"

		Done = "Done: " + (FPS if self.done=="Clicked" else self.done)
		if State=="(Off)":
			Done=""
		return State, Done



Thread1 = ClickerThread("LeftClick", [13, 16.5], ["control", "x"], "mbutton", "lbutton")
Thread2 = ClickerThread("RightClick", [10.5, 13], ["control", "x"], "c", "rbutton" )
Thread2.Switch.playsuond = False
Thread(target = Thread1.loop).start()
Thread(target = Thread2.loop).start()



class HighPerformStuff(RunThread):
	frame = 0
	inzoom = False
	def __init__(self, FPS = 60):
		super().__init__("HighPerformStuff", FPS)

	def Stuff(self):
		self.frame +=1
		userInput.Update(self.frame)
		def zoom():
			if userInput.IsPressed(["lbutton", "rbutton"]):
				self.inzoom=True
				print(1)
				if not userInput.IsPressed(["z"]):
					Control_KeyBoard(0x5A, 0, 0, 0)
			elif self.inzoom==True:
				self.inzoom=False
				Control_KeyBoard(0x5A, 0, win32con.KEYEVENTF_KEYUP ,0)

		zoom()


HighPerformanceStuff = HighPerformStuff()
Thread(target = HighPerformanceStuff.loop).start()

class LowPerformStuff(RunThread):
	"up KIEM nhanh pls" #sau 5p
	"up KIEM nhanh cc" #sau 10p
	"up GIAP di, no trau vcl"
	CommonChat = [["@ghe qua ", "@ghe vay ", "@ghe vay?", "@cc", "@cc?", "@?"], ["up KIEM pls", ],[ "ai bed?", "bed di nhe"], ["E, ve di bed kiaa", "E bedd", "Bed kia ve di", "ve"], ["@gg", "@hay", "@ay"], "/leave"]

	def __init__(self, FPS = 30):
		super().__init__("LowPerformStuff", FPS)

	def Stuff(self): #Todo: Chat
		if userInput.IsPressed([exKey]):
			O_Sound.ExitSound.play()
			Thread1.stop = True
			Thread2.stop = True
			Console_Controller.stop = True
			HighPerformanceStuff.stop = True
			LowPerformanceStuff.stop = True

		if userInput.IsPressed(["control", "l"]):
			Control_KeyBoard(0x11, 0, win32con.KEYEVENTF_KEYUP ,0)
			Control_KeyBoard(0x4C, 0, win32con.KEYEVENTF_KEYUP ,0)
			MinecraftWriteChat.MinecraftAutoChat("/l ak2006@@")

		for i in range(len(self.CommonChat)):
			if userInput.IsPressed(["numpad"+str(i)]):
				Control_KeyBoard(97+i-1, 0, win32con.KEYEVENTF_KEYUP ,0)
				if type(self.CommonChat[i-1])==str:
					CHAT = self.CommonChat[i-1]
				elif type(self.CommonChat[i-1])==list:
					CHAT = random.choice(self.CommonChat[i-1])

				MinecraftWriteChat.MinecraftAutoChat(CHAT)

LowPerformanceStuff = LowPerformStuff()
Thread(target = LowPerformanceStuff.loop).start()


class Screen(RunThread):
	lastThread1Info = None
	lastThread2Info = None
	description = describe
	def __init__(self, title:str =title, winsize: list = [32, 15], FPS = 30):
		super().__init__("ConsoleController", FPS)
		self.title = title
		self.winsize = winsize
		self.FPS = FPS

		#OsCmdControl("mode con cols="+str(self.winsize[0])+" lines="+str(self.winsize[1]))
		OsCmdControl("color 2d")
		OsCmdControl("title "+title)

	def Stuff(self):
		Thread1Info = Thread1.info()
		Thread2Info = Thread2.info()
		
		#OsCmdControl("mode con cols="+str(self.winsize[0])+" lines="+str(self.winsize[1]))

		if Thread1Info==self.lastThread1Info and Thread2Info==self.lastThread2Info:
			return
		else:
			self.lastThread1Info = Thread1Info
			self.lastThread2Info = Thread2Info 
			if Thread1.error==False and Thread2.error==False and Console_Controller.error==False and HighPerformanceStuff.error==False and LowPerformanceStuff.error==False:
				#OsCmdControl("cls")
				pass
			else: #Have some error
				pass
			#print(self.description)
			print("Minecraft Bedwars Mode")
			print("Thead1", Thread1Info[0], "| ", Thread1Info[1], sep="")
			print("Thead2", Thread2Info[0], "| ", Thread2Info[1], sep="")
			print


Console_Controller = Screen()
Thread(target = Console_Controller.loop).start()