import yaml
import traceback
import sys

def LoadFile(file):
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

	elif isinstance(txt,list):
		for item in txt:
			lower_dict(item)


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

if __name__ == '__main__':
	a = LoadFile("instruction.yaml")
	print(a)
	print(type(a))

	lower_dict(a)
	print(a)
