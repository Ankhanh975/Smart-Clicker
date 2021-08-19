import yaml
import traceback
import sys

def LoadFile(file= "instruction.yaml"):
	stream = open(file, 'r')

	try:
		dictionary = yaml.load(stream, Loader=yaml.FullLoader)
		return dictionary
	except yaml.parser.ParserError:#, yaml.scanner.ScannerError, yaml.YAMLError:
		try:
			exc_info = sys.exc_info()
		finally:
			traceback.print_exception(*exc_info)
			del exc_info
		print("Your input file is in wrong format")
		return None

def JsonToTxt(data):
    import json
    return json.dumps(data, indent=4, sort_keys=True)

def lower_dict(data):
	# Lower all string in tag name for easier use 
	if isinstance(data,dict):
		for key in list(data.keys()):
			if key.islower():
				lower_dict(data[key])
			else:
				key_lower = key.lower()
				data[key_lower] = data[key]
				del data[key]
				lower_dict(data[key_lower])

	elif isinstance(data,list):
		for item in data:
			lower_dict(item)



def GiveNameToNotNamedObject(data): #TODO
	return data

def RunningObject(data): #TODO
	return NumRunningObject, RunningObjectNames

def Filter(data): #TODO for v4
	def Filter_ActiveTime(data):
		if ">" in data[x]:
			data = data.replace(">","")
		elif "<" in data[x]:
			data = data.replace("<","")
		elif ">=" in data[x]:
			data = data.replace(">=","")
		elif ">=" in data[x]:
			data = data.replace(">=","")

		data = data.replace("s","")
		if "ms" in data:
			data = data.replace("ms","")
			data = float(data)/1000
		return float(data)

	def Filter_PosPrecise(data):
		if "pixel" in data:
			data = data.replace(" pixels","")
			data = data.replace(" pixel","")
			data = data.replace("pixels","")
			data = data.replace("pixel","")
			data = int(data)
		return data
	return data

from O_Clicker import *
from O_Global import *

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

	@staticmethod
	def Load_O_Recorder(data): #TODO
		a=None
		return a

def KeyboardInUse(data, turnToNumbers=True):
	# data is a json from original .yaml->dict file
	Z=[]
	data = JsonToTxt(data)
	data = data.split("\n")
	for x in data:
		if ("keypress" in x) or ("switchevent" in x):
			n=x
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
			Z2.append(_List._z.index(Z[x]))

		return Z2
	else:
		return Z


if __name__ == '__main__':
	data = LoadFile()
	lower_dict(data)
	print(KeyboardInUse(data, False))

'''
def main():
	for _Object in data:
		if data[_Object] != "global":
			control.running_object +=1

		if data[_Object] == "global":
			for details in data[_Object]:
				if data["global"][details] == "kill":
					for x in data[_Object][details]:
						for y in x:
							if y == None:
								pass 
					if data["global"][details] == "kill":
					if KeyPress
					O_control.KillCondition
				elif data["global"][details] == "start":
					O_control
				elif data["global"][details] == "o.logger":
					O_control

		elif data[_Object] == 'o.clicker': 
			Object.append(O_Clicker())
			Object[-1].TPS = data[_Object]["tps"]
			Object[-1].Name = data[_Object]["name"]
			for x in data[_Object]["clickevent"]:
				pass

			elif data[_Object] == "condition":
				for x in data[_Object]["condition"]:
					if data[_Object]["condition"] == "box":
						Object[-1].EventCondition.Box = data[_Object]["condition"]["box"]
					elif data[_Object]["condition"] ==	"activewindow":
						Object[-1].EventCondition.ActiveWindow = data[_Object]["condition"]["activewindow"]
					elif data[_Object]["condition"] ==	"o.switch":
						Object[-1].EventCondition.O_Switch = data[_Object]["condition"]["o.switch"]
					elif data[_Object]["condition"] ==	"keypress":
						Object[-1].EventCondition.KeyPressCondition = data[_Object]["condition"]["o.switch"]

			elif data[_Object] == "kill":
				for x in data[_Object]["kill"]:
					if data[_Object]["kill"] == "box":
						Object[-1].KillCondition.Box = data[_Object]["kill"]["box"]
					elif data[_Object]["kill"] ==	"activewindow":
						Object[-1].KillCondition.ActiveWindow = data[_Object]["kill"]["activewindow"]
					elif data[_Object]["kill"] ==	"o.switch":
						Object[-1].KillCondition.O_Switch = data[_Object]["kill"]["o.switch"]
			elif data[_Object] == "TimePrecise":
				Object[-1].Name = data[_Object]["Name"]
			elif data[_Object] == "PosPrecise":
				Object[-1].Name = data[_Object]["Name"]
			elif data[_Object] == "ClickSound":
				Object[-1].Name = data[_Object]["Name"]
		
		elif data[_Object] == "o.recorder":

	while True:
		for x in range(len(data)):
			data[x].Update()
			
		control.Update()'''
'''
def checkSyntax(data):
	def SingalStringCheck(data, InstructionSytax):
		for 
		return True
		SingalStringCheck(data, InstructionSytax)
		else:
			return False

	def contentCheck():
		Keywords = {"Kill": dict, "KeyPress": str, "ActiveTime": str, "Name": str, "ClickEvent": dict, "Click_Record": dict, 
					"Button": str, "Pos": list, "HoldTime": float, "TPS": float, "Condition": dict, 
					"Box": list, "ActiveWindow": str, "O.Switch": dict, "SwitchSound": str, 
					"ClickCount": str, "TimePrecise": str, "PosPrecise": str, "ClickSound": str,
					"O.Typist": int, "PressEvent": int, "Press": int, "O.Recorder": int, "D.ActiveWindow": int, 
					"Setting": dict, "OnlyNewEvent": bool, "Log_Time": bool}

	#Keywords[]: All Keywords to start a configuration
	Keywords = ["Kill", "KeyPress", "ActiveTime", "Name", "ClickEvent", "Click_Record", "Click", "Button", "Pos", "HoldTime", "TPS", "Condition", 
				"Box", "ActiveWindow", "O.Switch", "SwitchSound", "SwitchEvent", "Kill", "ClickCount", "TimePrecise", "PosPrecise", "ClickSound",
				"O.Typist", "PressEvent", "Press", "O.Recorder", "RecordEvent", "D.ActiveWindow", "Setting", "OnlyNewEvent", "Log_Time", "Output"]

	#InstructionSyntax: the Syntax of string input
	InstructionSytax = ["${file_name}", "${numbers}", "${letters}", "${keybotton}", 
						">", "<", ">=", "<=",
						"ms", "ns", "s", "cm", "m", "%", "b", "bt", " pixel"]

	if False:
		raise Exception("Your given instruction created combine error")
		return False
	else:
		return True
'''


