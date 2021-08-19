def FirstProcess(file = "instruction.yaml"):
	# Watch return data to know what this do
	def updateTxtFromSplit(split):
		txt = ""
		for x in split:
			txt+=  x + "\n"
		return txt
	def updateSplitFromTxt(txt):
		return txt.split("\n")

	def TxtposFromLinePos(Line, Column, split, txt):
		return n
	def LinePosFromTxtpos(Column, split, txt):
		NumberOfSplitBeforeColumn = 0
		return Line, Column

	txt = open(file, "r")
	txt = txt.read()
	split = updateSplitFromTxt(txt)

 	# Not do this Yaml loader will overwrite "o.clicker"
	if txt.count("o.clicker") >= 2:
		Appear = txt.count("o.clicker")

		for x in range(Appear):
			NewName = "o.clicker" + str(x +1) + ":"
			NewName = NewName if x!= 0 else "o.clicker:"
			txt = txt.replace("o.clicker:", NewName, 1)

	#This fix not allow structure of "o.clicker" line 
	for x in range(len(split)):
		if "o.clicker:" in split[x] and len(split[x]) > len("o.clicker: "):
			split[x] = split[x].replace("o.clicker: ", "o.clicker: \n")
			txt = updateTxtFromSplit(split)
			split = updateSplitFromTxt(txt)

	for x in range(len(split)):
		if split[x].find(":") == -1 and len(split[x])>1:
			CountLeftSpace = 2 #split[x].lstrip().len() - split[x].len()
			data = split[x].split(" ")
			split[x] = " "*CountLeftSpace + "tps: "+data[0] + "\n" + " "*CountLeftSpace + "KeyPress: "+data[1] + "\n" 

			txt = updateTxtFromSplit(split)
			split = updateSplitFromTxt(txt)

	return txt

def LoadFile(file= "instruction.yaml"):
	# Load file to python dict
	import yaml, traceback, sys
	stream = open(file, 'r')

	try:
		dictionary = yaml.load(stream, Loader=yaml.FullLoader)
		return dictionary
	except yaml.parser.ParserError: #, yaml.scanner.ScannerError, yaml.YAMLError:
		try:
			exc_info = sys.exc_info()
		finally:
			traceback.print_exception(*exc_info)
			del exc_info
		print("Your input file is in wrong format")
		return None

def lower_dict(data: dict):
	def _lower_dict(data):
		# Lower all string in tag name for easier use 
		if isinstance(data,dict):
			for key in list(data.keys()):
				if key.islower():
					_lower_dict(data[key])
				else:
					key_lower = key.lower()
					data[key_lower] = data[key]
					del data[key]
					_lower_dict(data[key_lower])

		elif isinstance(data,list):
			for item in data:
				_lower_dict(item)
	_lower_dict(data)
	return data

def GiveNameToNotNamedObject(data: dict): #TODO
	NumRunningObject = 0
	for a in data:
		if a in ["o.clicker", "o.logger", "o.recorder", "None"]:
			if "name" not in data[a].keys():
				data[a]["name"] = "id: " + str(NumRunningObject)
				NumRunningObject +=1


def RunningObject(data):
	NumRunningObject=len(data) -1 #-1 for Global
	RunningObjectNames=[]
	for a in data:
		if a!="global":
			RunningObjectNames.append(data[a]["name"])
	return NumRunningObject, RunningObjectNames # int, list

class Loadyaml:
	@staticmethod
	def Load_O_Clicker(data):
		a = O_Clicker()
		for x in data:
			if x =="name":
				a.name = str(data[x])
			elif x == "tps":
				a.TPS = float(data[x])
			elif x == "condition":
				a.EventCondition = Loadyaml.Load_Condition(data[x])
			elif x == "kill":
				a.KillCondition = Loadyaml.Load_Condition(data[x])
			elif x == "posprecise":
				a.PosPrecise = int(data[x])
			elif x == "button":
				a.button = data[x].lower()
			elif x == "pos":
				a.x = int(data[x][0])
				a.y = int(data[x][1])
		return a

	@staticmethod
	def Load_O_Global(data):
		a = Global()
		for x in data:
			
			if x=="kill":
				a.KillCondition = Loadyaml.Load_Condition(data[x])
			elif x=="start":
				# TODO: if x=="init_time"
				a.StartCondition = Loadyaml.Load_Condition(data[x])
		return a

	@staticmethod
	def Load_Condition(data):
		a= Condition()
		for x in data:
			if x=="box":
				a.Box = data[x]
			elif x=="activeWindow":
				a.ActiveWindow = data[x]
			elif x=="o.switch":
				for x2 in data[x]:
					if x2=="switchsound":
						a.O_Switch.SwitchSound = data[x][x2]
					elif x2=="switchevent":
						a.O_Switch.SwitchEvent = data[x][x2]
			elif x=="keypress":
				a.KeyPressCondition = Loadyaml.LoadKeyStrokes(data[x])
			elif x=="activetime":
				
				a.ActiveTime = float(data[x])
			elif x=="createdevent":
				pass #TODO
		return a

	@staticmethod
	def LoadKeyStrokes(data: str):
		#Load from nomal KeyStrokes to list
		data = data.replace("Caps", "capital")
		data = data.replace("Ctrl", "control")
		data = data.replace("Esc", "escape")
		data = data.replace("Alt", "menu")
		data = data.replace("SELECT", "K_SELECT")
		data = data.replace("INSERT", "K_INSERT")
		data = data.replace("DELETE", "K_DELETE")
		data = data.replace("Backspace", "BACK")
		if "Fn"in data: 
			raise Exception("Sorry, we don't support Fn key")

		a= data.split("+")

		for x in range(len(a)):
			a[x] = a[x].lower()

		return a
		
def Preprocess_instruction(file = "instruction.yaml"):
	data = LoadFile(file)
	lower_dict(data)

	#data = GiveNameToNotNamedObject(data)
	#Get = RunningObject(data)

	#WrireYaml(data)

	return data#, Get
	
if __name__ == '__main__':
	a = FirstProcess()
	print(a)