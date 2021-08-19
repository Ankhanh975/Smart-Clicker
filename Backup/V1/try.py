import time, win32api, win32con
from keycode import Get
# odr(), hr(	

get_now = time.perf_counter

def _sleep(duration): 
	now = get_now()
	
	end = now + duration
	while now < end:
		now = get_now()

def push_button(button):
    win32api.keybd_event(button, 0, 0, 0)
    _sleep(0.05)
    win32api.keybd_event(button, 0, win32con.KEYEVENTF_KEYUP, 0) 

_sleep(2)
push_button(Get(";"))