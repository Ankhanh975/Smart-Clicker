from API_Out import *
import math
import random
import time
# import pyautogui

"home/join/.minecraft/logs/latest.log"
terminal(f"xdotool getmouselocation")

def scan_window():
	all=[]
	while True:
		terminal_with_respone(f"xdotool getmouselocation")
		
def start_minecraft():
	minecraft_window = terminal(f"xdotool windowfocus")
	terminal(f"java -jar Shiginima\ Launcher.jar")
	time.sleep(7)
	click(522,479)
	time.sleep(2)
	click(513,585)
	time.sleep(25)
	click(508,469)
	
def test():
	minecraft_window = None
	minecraft_window = get_mincraft_window_id()
	minecraft_window = terminal_with_respone(f"xdotool getwindowname {minecraft_window}")
	print("Minecraft" in minecraft_window)
	
	for x in range(100):
		time.sleep(0.01)
		mousemove_relative(200, 0, minecraft_window)

	for x in range(100):
		time.sleep(0.01)
		mousemove_relative(-200, 0, minecraft_window)

	for x in range(100):
		time.sleep(0.01)
		mousemove_relative(20, 0, minecraft_window)

	for x in range(100):
		time.sleep(0.01)
		mousemove_relative(-20, 0, minecraft_window)
		
	key("Escape", minecraft_window)
	time.sleep(0.4)
	key("Escape", minecraft_window)
	def test_key(key):
		time.sleep(0.1)
		keydown(key, minecraft_window)
		time.sleep(1)
		keyup(key, minecraft_window)
	test_key("KP_Space")
	test_key("A")
	test_key("D")
	test_key("W")
	test_key("S")
	test_key("Shift_L")
	test_key("Control_L")
	test_key("1")
	test_key("2")
	test_key("3")
	test_key("4")
	test_key("5")
	test_key("6")
	test_key("7")
	test_key("8")
	test_key("9")

def run_random():
	for x in range(100):
		time.sleep(0.1)
		if random.randint(0,100)>90:
			pass
# start_minecraft()
# test()
0/0
# time.sleep(1)
start = time.perf_counter()
# mousescroll(4)
# click(3)
# mousedown(1)
# mouseup(1)
# key("a+b+c+d")

# for x in range(1):
	# time.sleep(0.1)
	# a=os.system(f"xdotool getactivewindow")
	# print(a)

# mousemove_relative(200, 0, 83886082)
# keydown("d+b")
# keyup("d+b")
# TODO: mousemove_relative(100,100)
# mousemove(100,100)

# print(time.perf_counter() - start)
