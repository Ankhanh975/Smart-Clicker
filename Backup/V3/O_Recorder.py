from O_Control import Base
import logging
import os, sys
import random

def SetClipboard(text):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(str(text))
	win32clipboard.CloseClipboard()

def ReadClipBoard():
	try:
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		return data
	except :
		return None

def _setup_logger(tlogger_name, tlog_file, tlevel=logging.INFO, tformat='%(asctime)s - %(message)s', tfilemode='a'):
	import win32clipboard
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
	import win32clipboard
	_setup_logger(tlogger_name, tlog_file, tlevel=logging.INFO, tformat='%(asctime)s - %(message)s', tfilemode='a')
	return logging.getLogger(tlogger_name)
OOO=[]

class O_Recorder(Base):
	def __init__(self, tName, tOutputFile):
		super().__init__(tName)
		self.OutputFile = str(tOutputFile)
		self.logger = setup_logger(self.Name, self.OutputFile)

		self.LogD_ActiveWindow = False
	   	self.LogD_ClipBoard = False
	   	self.LogD_MousePos = False
	   	self.LogD_MouseDown = False
	   	self.LogD_MouseUp = False
	   	self.LogD_MouseClick = False
	   	self.LogD_Keyboard = False

	def Update(self):
		self.logger.info()
		if self.LogD_ActiveWindow:

	   	if self.LogD_ClipBoard:

	   	if self.LogD_MousePos:

	   	if self.LogD_MouseDown:

	   	if self.LogD_MouseUp:

	   	if self.LogD_MouseClick:

	   	if self.LogD_Keyboard:

	def _log(self, text):
		self.logger.info(text)




if __name__ == '__main__':
