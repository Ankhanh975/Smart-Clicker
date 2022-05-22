# Smart-Clicker

# Dependent

Core: python, pygame, win32api 
AI: numpy, cv2, tensorflow, ...
Screenshot: Bandicam

V9 is the most stable version & most features
V8 is a stable version as well
V9 is 3 times easier to understand than previous versions!

# Features (V9)
# When Minecraft in focus
- Auto Clicker
- Chat bot
- Sort Inventory
https://www.facebook.com/100015299741261/videos/1197714240753955/
https://www.facebook.com/100015299741261/videos/604836490764131/
# Global
- Log Mouse Pos
 
Wait for me document more
import math, random, time
# import pyautogui
import os
# import mouse
# Button is a button number. Generally, left = 1, middle = 2, 
# right = 3, wheel up = 4, wheel down = 5
# You specified the wrong number of args.

def click(state, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool click {opt}{state}")
	os.system(f"xdotool click {opt}{state}")

def key(key, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool key {opt}{key}")
	os.system(f"xdotool key {opt}{key}")

def keydown(key, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool keydown {opt}{key}")
	os.system(f"xdotool keydown {opt}{key}")

def keyup(key, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool keyup {opt}{key}")
	os.system(f"xdotool keyup {opt}{key}")

def mousemove(x,y, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool mousemove {opt}{x} {y}")
	os.system(f"xdotool mousemove {opt}{x} {y}")

def mousemove_relative(dx,dy, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool mousemove_relative {opt}{dx} {dy}")
	os.system(f"xdotool mousemove_relative {opt}{dx} {dy}")

def mousedown(state, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool mousedown {opt}{state}")
	os.system(f"xdotool mousedown {opt}{state}")

def mouseup(state, window= None):
	opt = ""
	if window: opt += f"--window {window} "
	print(f"xdotool mouseup {opt}{state}")
	os.system(f"xdotool mouseup {opt}{state}")

def mousescroll(dx, window= None):
	opt = ""
	state = 4 if dx > 0 else 5
	dx = abs(dx)
	if window: opt += f"--window {window} "
	if dx != 1 and dx != -1:
		opt += f"--repeat {dx} --delay 0 "
	print(f"xdotool click {opt}{state}")
	os.system(f"xdotool click {opt}{state}")

all=[f"xdotool click",
f"xdotool keydown",
f"xdotool keyup",
f"xdotool mousedown",
f"xdotool mousemove",
f"xdotool mouseup",
f"xdotool set_num_desktops",
f"xdotool windowsize"]

time.sleep(1)
start = time.perf_counter()
# mousescroll(4)
# click(3)
# mousedown(1)
# mouseup(1)
# key("a+b+c+d")

for x in range(1):
	time.sleep(0.1)
	# a=os.system(f"xdotool getactivewindow")
	# print(a)

	mousemove_relative(200, 0, 83886082)
# keydown("d+b") 
# keyup("d+b")

# TODO: mousemove_relative(100,100)
# mousemove(100,100)

print(time.perf_counter() - start)


# pyautogui.click()
# time.sleep(0.1)
# mouse.move("500", "500")
# mouse.left_click()
# pyautogui.click()

# from Xlib import X, display
# d = display.Display()
# s = d.screen()
# root = s.root
# root.warp_pointer(300,300)
# d.sync()
# print(1)a
