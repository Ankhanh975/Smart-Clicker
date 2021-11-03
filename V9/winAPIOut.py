import win32api
from Lib import _List
from win32api import keybd_event
import win32con
import ctypes
import time

# pygame.time.delay()


def Sleepp(duration):  # High accurate sleep
    now = time.perf_counter()
    end = now + duration
    while now < end:
        if end-now >= 1/61:
            time.sleep(1/1000)
        now = time.perf_counter()


def turn_capslock(state: bool = False):
    dll = ctypes.WinDLL('User32.dll')
    VK_CAPITAL = 0X14
    if dll.GetKeyState(VK_CAPITAL):
        dll.keybd_event(VK_CAPITAL, 0X3a, 0X1, 0)
        dll.keybd_event(VK_CAPITAL, 0X3a, 0X3, 0)

    return dll.GetKeyState(VK_CAPITAL)


def press(args, duration: float = 1/500):
    keybd_event(_List.VK_CODE[args], 0, 0, 0)
    Sleepp(duration)
    keybd_event(_List.VK_CODE[args], 0, win32con.KEYEVENTF_KEYUP, 0)


def pressAndHold(*args):
    '''
    press and hold. Do NOT release.
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
    '''
    for i in args:
        keybd_event(_List.VK_CODE[i], 0, 0, 0)
        time.sleep(.05)


def release(*args):
    for i in args:
        keybd_event(_List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


def pressHoldRelease(*args):
    for i in args:
        keybd_event(_List.VK_CODE[i], 0, 0, 0)
        Sleepp(1/500)

    Sleepp(1/100)
    for i in args:
        keybd_event(_List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
        Sleepp(1/500)


def typer(string=None, *args):
    # time.sleep(4)
    turn_capslock()
    for i in string:
        if i == ' ':
            keybd_event(_List.VK_CODE['spacebar'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['spacebar'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '!':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['1'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['1'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '@':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['2'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['2'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '{':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['['], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['['], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '?':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['/'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['/'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == ':':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE[';'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE[';'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '"':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['\''], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['\''], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '}':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE[']'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE[']'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '#':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['3'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['3'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '$':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['4'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['4'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '%':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['5'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['5'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '^':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['6'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['6'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '&':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['7'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['7'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '*':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['8'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['8'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '(':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['9'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['9'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == ')':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['0'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['0'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '_':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['-'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['-'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '=':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['+'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['+'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '~':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['`'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['`'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '<':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE[','], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE[','], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == '>':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['.'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['.'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'A':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['a'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['a'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'B':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['b'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['b'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'C':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['c'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['c'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'D':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['d'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['d'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'E':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['e'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['e'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'F':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['f'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['f'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'G':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['g'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['g'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'H':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['h'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['h'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'I':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['i'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['i'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'J':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['j'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['j'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'K':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['k'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['k'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'L':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['l'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['l'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'M':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['m'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['m'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'N':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['n'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['n'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'O':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['o'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['o'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'P':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['p'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['p'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'Q':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['q'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['q'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'R':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['r'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['r'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'S':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['s'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['s'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'T':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['t'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['t'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'U':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['u'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['u'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'V':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['v'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['v'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'W':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['w'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['w'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'X':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['x'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['x'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'Y':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['y'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['y'], 0, win32con.KEYEVENTF_KEYUP, 0)

        elif i == 'Z':
            keybd_event(_List.VK_CODE['left_shift'], 0, 0, 0)
            keybd_event(_List.VK_CODE['z'], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            keybd_event(
                _List.VK_CODE['z'], 0, win32con.KEYEVENTF_KEYUP, 0)

        else:
            keybd_event(_List.VK_CODE[i], 0, 0, 0)
            Sleepp(1/500)
            keybd_event(
                _List.VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    time.sleep(4)
    press("/")
    Sleepp(1/20)
    press("backspace")
    typer("Hello World")
    press("enter")


def fastclick(button="lbutton", duration=0.005):
    # Click
    if button.lower() == "lbutton":
        _ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
    elif button.lower() == "rbutton":
        _ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP
    elif button.lower() == "mbutton":
        _ButtonDown, _ButtonUp = win32con.MOUSEEVENTF_MIDDLEDOWN, win32con.MOUSEEVENTF_MIDDLEUP
    win32api.mouse_event(_ButtonDown, 0, 0)
    Sleepp(duration)
    win32api.mouse_event(_ButtonUp, 0, 0)
