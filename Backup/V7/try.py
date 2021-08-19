from _main import *
#TODO: kiểm tra respown speed of pynput
#TODO: google vision nhận dạng tên
#TODO: test xem win32api relase có ảnh hưởng tới input ko
class ClickerThread(RunThread):
	def __init__(self, FPS=13):
		super().__init__("Click", FPS)

	def Stuff(self):
		if userInput.IsPressed(["lbutton"]):
			print("CLicked")
			win32api.mouse_event(_ButtonDown,0, 0)
			resorce.Sleepp(duration) 
			win32api.mouse_event(_ButtonUp, 0, 0)
			_ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP

			O_Clicker.fastclick(None, "lbutton")
			self.stop=True
			return
	
class HighPerformStuff(RunThread):
	frame = 0
	def __init__(self, FPS = 120):
		super().__init__("HighPerformStuff", FPS)

	def Stuff(self):
		self.frame +=1
		userInput.Update(self.frame)
		print(userInput.Global_HoldKey)
		if userInput.IsPressed(["c"]):
			_ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
			win32api.mouse_event(_ButtonUp, 0, 0)


HighPerformanceStuff = HighPerformStuff()
Thread(target = HighPerformanceStuff.loop).start()

# Thread1 = ClickerThread()
# Thread(target = Thread1.loop).start()
