import json

def FromPythonSytleToJson(txt){
	
}
def LoadFile(file): #file = "instruction.h"
	f = open(file)
	data = json.load(f)
	return data

def lower_json(txt):
	# Lower all string input
	if isinstance(txt,dict):
		for key in list(txt.keys()):
			if key.islower():
				lower_json(txt[key])
			else:
				key_lower = key.lower()
				txt[key_lower] = txt[key]
				del txt[key]
				lower_json(txt[key_lower])

	elif isinstance(txt,list):
		for item in txt:
			lower_json(item)

data = LoadInstruction()
lower_json(data)
