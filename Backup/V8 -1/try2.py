from pynput.mouse import Button, Controller
from _main import *

mouse = Controller()

class getMinecraftSlot:
	scroll = 0
	def __init__(self):
		self.listener = pynput.mouse.Listener(on_scroll=self.on_scroll)

	def start(self):
		self.listener.start()

	def on_scroll(self, _, __, dx, dy):
		self.scroll += dy 
		print("Detext: ", time.perf_counter(), dx, dy, self.scroll)

scrollTheard = getMinecraftSlot()
scrollTheard.start()

# Scroll two steps down
for i in range(10):
	time.sleep(0.5)
	start = time.perf_counter()
	#mouse.scroll(0, -1)
	print("Scroll")
	win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,+200)
	end = time.perf_counter()
	print(end-start)
#time.sleep(100)
