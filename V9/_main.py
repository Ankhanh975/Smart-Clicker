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


if __name__ == "__main__":
    pass