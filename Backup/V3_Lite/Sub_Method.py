import _List, win32api

def getKeyState(keyRequire=[]):
    #print(keyRequire)
    keyPressed = []
    if keyRequire==[]:
        for x in range(256):
            a = win32api.GetKeyState(x)
            if a<0 and _List._z[x] !=None:
                keyPressed.append(_List._z[x])
    else:
        for x in keyRequire:
            a = win32api.GetKeyState(x)
            if _List._z[x] !=None:
                if a<0: 
                    keyPressed.append(_List._z[x])
            else:
                print(keyRequire, keyPressed, x, "What wrong?, why you requst a None keyNumber ")
    return keyPressed

#if __name__ == '__main__':
#    import time
#    for a in range(30):
#        print(getKeyState())
#        time.sleep(1/30)
        
import time
def Sleep(duration): #High accurate sleep
    now = time.perf_counter()
    end = now + duration
    while now < end:
        if end-now >= 1/61:
            time.sleep(1/1000)
        now = time.perf_counter()

def IsPressed(Global_holdKey, CheckKeyStrokes):
    for x in CheckKeyStrokes:
        if x not in Global_holdKey:
                return False
    return True

def SmallestRunFPS(List):
    # List is a list of n number to find GCD
    def GCD(a, b):
        if a%b==0:
            return b
        else:
            return GCD(b, a % b)

    def GCDn(list):
        g = GCD(List[0], List[1])
        for i in range(2, len(List)):
            g=GCD(g, List[i])
        return g

    return GCDn(List)

def PrintJson(data):
    import json
    print(json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
    a={'global': {'start': {'init_time': '>2s'}, 'kill': {'keypress': 'Ctrl+Shift+Esc', 'activetime': '>1000'}}, 'o.clicker': {'name': 'Clicker1', 'clickevent': 'Click', 'tps': 5, 'button': 'Left', 'pos': [100, 100], 'condition': {'box': [[100, 100], [200, 200]], 'activewindow': '(716) YouTube - Brave', 'o.switch': {'switchsound': '10%', 'switchevent': 'c'}}, 'kill': {'keypress': 'Ctrl+Shift+Esc', 'activetime': '>1000'}, 'posprecise': '5pixel'}}
    PrintJson(a)