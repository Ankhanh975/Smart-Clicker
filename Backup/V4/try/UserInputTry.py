class GetInput():
	def __init__(self, data: dict):
		self.screenSize = [pyautogui.size()[0], pyautogui.size()[1]]
		self.NeedCheckedKey = []
		self.UsingKey(data)
		self.VK_CODE_REVERSE = _List.VK_CODE_REVERSE
		self.VK_CODE = _List.VK_CODE

		self.Global_HoldKey = []
		self.Global_MousePos = [-1,-1]
		self.Global_ActiveWindow = "None"

		
	def Update(self):
		flags, hcursor, self.Global_MousePos = win32gui.GetCursorInfo()
		self.Global_ActiveWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
		self.Global_HoldKey = self.getKeyState()

	def UsingKey(self, data):
		def KeyboardInUse(data, turnToNumbers=True):
			# data is a json from original .yaml->dict file
			Z=[]
			data = JsonToTxt(data)
			data = data.split("\n")
			for x in data:
				if ("keypress" in x) or ("switchevent" in x):
					n = x
					n = n.replace("keypress", "")
					n = n.replace("switchevent", "")
					n = n.replace('"', "")
					n = n.replace(" ", "")
					n = n.replace(",", "")
					n = n.replace(":", "")
					Z+=Loadyaml.LoadKeyStrokes(n)

			Z.append("lbutton")
			Z.append("rbutton")
			Z.append("mbutton")
			if turnToNumbers:
				import _List
				Z2=[]
				for x in range(len(Z)):
					Z2.append(self.VK_CODE_REVERSE.index(Z[x]))

				return Z2
			else:
				return Z
		self.NeedCheckedKey = KeyboardInUse(data)
		return KeyboardInUse(data)

	def IsPressed(CheckKeyStrokes):
	    for x in CheckKeyStrokes:
	        if x not in self.Global_HoldKey:
	                return False
	    return True

	def getKeyState(self):
	    keyPressed = []
	    if self.NeedCheckedKey==[]:
	        for x in range(256):
	            a = win32api.GetKeyState(x)
	            if a<0 and self.VK_CODE_REVERSE[x] !=None:
	                keyPressed.append(self.VK_CODE_REVERSE[x])
	    else:
	        for x in self.NeedCheckedKey:
	            a = win32api.GetKeyState(x)
	            if _List.VK_CODE_REVERSE[x] !=None:
	                if a<0: 
	                    keyPressed.append(self.VK_CODE_REVERSE[x])
	            else:
	                print(self.NeedCheckedKey, keyPressed, x, "What wrong?, why you requst a None keyNumber ")
	    return keyPressed
	def __str__(self):
		return "Global_ActiveWindow: " + str(self.Global_ActiveWindow) + ", Global_HoldKey: " + str(self.Global_HoldKey) + ", Global_MousePos: " + str(self.Global_MousePos)

	def debug(self):
		print("screenSize:", self.screenSize)
		print("NeedCheckedKey:", self.NeedCheckedKey )
		print("Global_HoldKey:", self.Global_HoldKey )
		print("Global_MousePos:", self.Global_MousePos )
		print("Global_ActiveWindow:", self.Global_ActiveWindow )
		print("\n\n\n" )