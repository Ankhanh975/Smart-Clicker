from _main import *
import _List

exKey = "f4"
describe = '''#Minecraft Bedwars Mode 
Press ctrl_r+x to pause all, F4 to exit
Hold Left+Right mouse for zoom
'''

CRED = '\033[91m'
CEND = '\033[0m'

CommonChat = [["@ghe qua ", "@ghe vay ", "@ghe vay ai choi?", "@ghe vay.", "@cc", "@cc?"], ["up KIEM pls", "up KIEM nhe", "ai up KEIm?", "up KIEm cc"],[ "ai bed?", "bed di", "bed nhanh", "cc bed"], ["E, ve di bed kiaa", "E bedd", "Bed nhanh", "ve"], ["@gg", "hay", "ay"], "/leave"]

def MinecraftAutoChat(text: str="."): #TODO: chat dc tiếng việt, đọc được chat 
#TODO: 
	#Release all potentiality key can mess thing up
	userInput.Update(0)
	for i in userInput.Global_HoldKey:
		resorce.Sleepp(1/500) 

		try:
			Control_KeyBoard(_List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP ,0)
			print(i, _List.VK_CODE[i])
		except KeyError as p:
			print(p)

			#O_Sound.ErrorSound.play()

	#Open chat
	resorce.press("/")
	O_Sound.PressSound.play()
	resorce.Sleepp(1/20.5) #Sleep so minecraft can progress
	resorce.press("backspace")

	resorce.typer(text) #Really write text

	#Close chat
	resorce.press("enter")
	resorce.Sleepp(1/20.5) #Sleep so minecraft can progress

	for i in userInput.Global_HoldKey:
		resorce.Sleepp(1/500) 
		try:
			Control_KeyBoard(_List.VK_CODE[i], 0, 0 ,0)
			print(i, _List.VK_CODE[i])
		except KeyError as p:
			print(p)

P_State1 = P_Switch1 = P_State2 = P_Switch2 = ""
#userInput.NeedCheckedKey =  ["control", "x", "f4", "c", "mbutton", "lbutton", "rbutton", "l","numpad_1","numpad_2","numpad_3","numpad_4","numpad_5","numpad_6"] 

def Control():
	global P_State1, P_Switch1, P_State2, P_Switch2, exKey, userInput
	clock = pygame.time.Clock()
	a=""
	frame = 0
	while True:
		frame+=1
		if userInput.IsPressed([exKey]):
			ExSound.play()
			TheadExit() # not run userInput.Update so 2 main theard never miss exit
		clock.tick(30)
		userInput.Update(frame)

		if userInput.IsPressed(["lbutton", "rbutton"]):
			Control_KeyBoard(0x5A, 0, 0, 0)
		else:
			Control_KeyBoard(0x5A, 0, win32con.KEYEVENTF_KEYUP ,0)

		if userInput.IsPressed(["control", "l"]):
			Control_KeyBoard(0x11, 0, win32con.KEYEVENTF_KEYUP ,0)
			Control_KeyBoard(0x4C, 0, win32con.KEYEVENTF_KEYUP ,0)
			MinecraftAutoChat("/l ak2006@@")

		for i in range(1, 7):
			if userInput.IsPressed(["numpad"+str(i)]):
				print(1)
				Control_KeyBoard(97+i-1, 0, win32con.KEYEVENTF_KEYUP ,0)
				if type(CommonChat[i-1])==str:
					CHAT = CommonChat[i-1]
				elif type(CommonChat[i-1])==list:
					CHAT = random.choice(CommonChat[i-1])

				MinecraftAutoChat(CHAT)
				print(CHAT)

		a1 = describe 
		a2 = "Thead1| "+  P_Switch1 + ", " + P_State1 + "\n"
		a3 = "Thead2| "+  P_Switch2 + ", " + P_State2 + "\n"
		a4 = " Input: "+ str(userInput.Global_HoldKey) + "\n"
		a5 = userInput.Global_OnActiveWindow
		if a!=a1+a2+a3+a4+a5:
			a=a1+a2+a3+a4+a5
			OsCmdControl('cls')
			print(a)

			#print(CRED + "Error, does not compute!" + CEND)

	if frame%10==0:
		OsCmdControl("mode con cols=32 lines=15")

def Thead1():
	global P_State1, P_Switch1, userInput, exKey

	fps = [14, 16.5]
	Switch = Condition.Switch(["control", "x"])
	Switch._Event()
	activeButton = "mbutton"
	eventButton = "lbutton"

	clock = pygame.time.Clock()
	while True:
		FPS = round(random.uniform(fps[0], fps[1]), 1)
		clock.tick(FPS)
		
		Switch.Update(userInput)
		if userInput.IsPressed([exKey]):
			TheadExit()
		if userInput.IsPressed([activeButton]) and Switch.GetState():
			O_Clicker.fastclick(userInput, eventButton)

		P_State1 = "Done: " + ("Clicked" if userInput.IsPressed([activeButton]) and Switch.GetState() else "None   ")
		P_Switch1 = "St: " + ("On " if Switch.GetState() else "Off")

def Thead2():
	global P_State2, P_Switch2, userInput, exKey
	fps = [11, 13]
	Switch = Condition.Switch(["control", "x"], False)
	Switch._Event()
	
	activeButton = "c"
	eventButton = "rbutton"

	clock = pygame.time.Clock()
	
	while True:
		FPS = round(random.uniform(fps[0], fps[1]), 1)
		clock.tick(FPS)
		
		Switch.Update(userInput)
		if userInput.IsPressed([exKey]):
			TheadExit()
		if userInput.IsPressed([activeButton]) and Switch.GetState():
			O_Clicker.fastclick(userInput, eventButton)


		P_State2 = "Done: " + ("Pressed" if userInput.IsPressed([activeButton]) and Switch.GetState() else "None   ")
		P_Switch2 = "St: " + ("On " if Switch.GetState() else "Off")


Thread(target = Thead1).start()
Thread(target = Thead2).start()
Thread(target = Control).start()