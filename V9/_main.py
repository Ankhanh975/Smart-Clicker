import threading
# from threading import Timer, Event, Thread
from random import uniform
from pygame.time import Clock as pygameClock


def setTimeout(callback, ms):
    x = threading .Timer(ms/1000.0, callback)
    x.start()


class setInterval:
    # https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval/14035296
    # use: setInterval(callback, ms, timeout)
    # random FPS value if FPS is a List[2]

    def __init__(self, callback, interval, timeout=float("inf"), randomMs=0):
        self.interval = interval / 1000.0
        self.timeout = timeout/1000.0
        1.0 / self.interval
        # Limit -interval <= randomMs <= interval
        if randomMs >= 0:
            self.randomMs = min(randomMs, interval)/1000.0
        else:
            self.randomMs = max(randomMs, interval)/1000.0
        self.callback = callback
        self.stopEvent = threading.Event()
        self.clock = pygameClock()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        # calculate the run time by self.timeout
        loopTime = self.timeout/self.interval
        if loopTime != float("inf"):
            loopTime = int(loopTime)
        else:
            loopTime = 10**100
        for _ in range(loopTime):
            # Make interval more random.

            randomSleepTime = uniform(0, self.randomMs)
            self.clock.tick(1.0/(self.interval-randomSleepTime))
            self.callback()
            # print("Interval", randomSleepTime, 1.0 /
            #       (self.interval+randomSleepTime))
            
# class OnChatMessage():
#     file = "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log"
#     sleepTime = 0
#     stop = False

#     def __init__(self, callback):
#         self.id = []
#         self.chatHistory = []
#         # self.chatHistory.append(text)

#     def addListener(self, callback):
#         self.id.append(id(callback))

#     def hasListener(self, callback):
#         if (id(callback) in self.id):
#             return True
#         else:
#             return False

#     def removeListener(self, callback):
#         self.id.remove(id(callback))
#     # callback(self.chat)
