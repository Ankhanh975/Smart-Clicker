import win32gui, time

for i in range(1000):
	print(win32gui.GetCursorInfo())
	time.sleep(1/60)
