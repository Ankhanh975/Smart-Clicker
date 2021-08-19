def Filter(data): #TODO
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

def JsonToTxt(data):
	# Load python dict to nicely fomart text 
    import json
    return json.dumps(data, indent=4, sort_keys=True)

def PrintJson(data):
    print(JsonToTxt(data))

def WrireYaml(data, file = 'ProcessedData.yaml'):
	import yaml
	with open(file, 'w') as outfile:
	    yaml.dump(data, outfile, default_flow_style=False)

def checkSytax(data):
	return None #TODO
	raise Exception("None")

def Preprocess_instruction(file = "instruction.yaml"):
	data = LoadFile(file)
	lower_dict(data)
	checkSytax(data)

	data = GiveNameToNotNamedObject(data)
	Get = RunningObject(data)

	WrireYaml(data)

	return data, Get

'''if __name__ == '__main__':
	 a, b = Preprocess_instruction()
	 print(b)'''