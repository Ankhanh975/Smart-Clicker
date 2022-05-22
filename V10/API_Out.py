
import os


def terminal(command):
    print("command", command)
    os.system(command)


def click(state, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool click {opt}{state}")


def key(key, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool key {opt}{key}")


def keydown(key, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool keydown {opt}{key}")


def keyup(key, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool keyup {opt}{key}")


def mousemove(x, y, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool mousemove {opt}{x} {y}")


def mousemove_relative(dx, dy, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool mousemove_relative {opt}{dx} {dy}")


def mousedown(state, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool mousedown {opt}{state}")


def mouseup(state, window=None):
    opt = ""
    if window:
        opt += f"--window {window} "
    terminal(f"xdotool mouseup {opt}{state}")


def mousescroll(dx, window=None):
    opt = ""
    state = 4 if dx > 0 else 5
    dx = abs(dx)
    if window:
        opt += f"--window {window} "
    if dx != 1 and dx != -1:
        opt += f"--repeat {dx} --delay 0 "
    print(f"xdotool click {opt}{state}")
    os.system(f"xdotool click {opt}{state}")


def get_mincraft_window_id() -> int:
    return


# import mouse
# Button is a button number. Generally, left = 1, middle = 2,
# right = 3, wheel up = 4, wheel down = 5
# You specified the wrong number of args.
all = [f"xdotool click", f"xdotool mousedown",
       f"xdotool mousemove",
       f"xdotool mouseup",
       f"xdotool set_num_desktops",
       f"xdotool windowsize", f"xdotool keydown",
       f"xdotool keyup", ]
