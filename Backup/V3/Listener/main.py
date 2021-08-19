import time
import array
from threading import Thread
import logging

def _setup_logger(tlogger_name, tlog_file, tlevel=logging.INFO, tformat='%(asctime)s - %(message)s', tfilemode='a'):
	import logging
	l = logging.getLogger(tlogger_name)
	formatter = logging.Formatter(tformat)
	fileHandler = logging.FileHandler(tlog_file, mode=tfilemode)
	fileHandler.setFormatter(formatter)
	streamHandler = logging.StreamHandler()
	streamHandler.setFormatter(formatter)

	l.setLevel(tlevel)
	l.addHandler(fileHandler)
	l.addHandler(streamHandler) 

def setup_logger(tlogger_name, tlog_file, tlevel=logging.INFO, tformat='%(asctime)s - %(message)s', tfilemode='a'):
	import logging
	_setup_logger(tlogger_name, tlog_file, tlevel=logging.INFO, tformat='%(asctime)s - %(message)s', tfilemode='a')
	return logging.getLogger(tlogger_name)

logger = setup_logger("logger", "Out.txt")

OOO=[]
def Get():
	global OOO
	return OOO

def Listener():
	global OOO
	from pynput.keyboard import Key, Listener
	def Event(key, state):
		global O
		if state==1 and (key not in OOO):
			OOO.append(key)
		elif state==0 and (key in OOO):
			OOO.remove(key)
		#logger.info(str(OOO))

	def on_press(key):
		Event(str(key), 1)
		
	def on_release(key):
		Event(str(key), 0)

	with Listener(on_press=on_press, on_release=on_release) as listener:
		#Detect max of 6 key
		listener.join()

Thread(target = Listener).start()
