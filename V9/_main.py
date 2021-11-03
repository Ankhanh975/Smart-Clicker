import time
import threading
from pygame.time import Clock as pygameClock


def setTimeout(callback, ms):
    x = threading .Timer(ms/1000.0, callback)
    x.start()


class setInterval:
    # https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval/14035296
    # use: setInterval(callback, ms, timeout)
    def __init__(self, callback, interval, timeout=float("inf")):
        self.interval = interval / 1000.0
        self.timeout = timeout/1000.0
        self.FPS = 1.0 / self.interval
        self.callback = callback
        self.stopEvent = threading.Event()
        self.clock = pygameClock()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        loopTime = self.timeout/self.interval
        if loopTime != float("inf"):
            loopTime = int(loopTime)
        else:
            loopTime = 10**100
        for _ in range(loopTime):
            self.clock.tick(self.FPS)
            self.callback()

def Sleepp(duration):  # High accurate sleep
    now = time.perf_counter()
    end = now + duration
    while now < end:
        if end-now >= 1/61:
            time.sleep(1/1000)
        now = time.perf_counter()

if __name__ == "__main__":
    last=0
    conut=0
    def main():
        global conut, last
        conut += 1
        print(conut, time.perf_counter()-last)
        last=time.perf_counter()
        
    setInterval(main, 1, 1000)