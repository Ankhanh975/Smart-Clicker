from pygame.mixer import Sound as pygameSound
from pygame.mixer import init as pygameInit


import threading
# from threading import Timer, Event, Thread
from random import uniform
from pygame.time import Clock as pygameClock


def setTimeout(callback, ms):
    x = threading .Timer(ms / 1000.0, callback)
    x.start()


class setInterval:
    # https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval/14035296
    # use: setInterval(callback, ms, timeout)
    # random FPS value if FPS is a List[2]
    running = True
    FPS = 0

    def __init__(self, callback, interval, randomMs=0, daemon=True, blocking=False, args=tuple(), kwargs={}):
        self.interval = interval / 1000.0
        # Limit -interval <= randomMs <= interval
        if randomMs >= 0:
            self.randomMs = min(randomMs, interval)/1000.0
        else:
            self.randomMs = max(randomMs, interval)/1000.0
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

        self.stopEvent = threading.Event()
        self.clock = pygameClock()
        if blocking:
            self.__setInterval()

        else:
            threading.Thread(target=self.__setInterval,
                             daemon=daemon, kwargs=kwargs).start()

    def __setInterval(self):
        while self.running == True:
            self.FPS = self.clock.get_fps()
            self.FPS = round(self.FPS)
            # Make interval more random.

            randomSleepTime = uniform(0, self.randomMs)
            self.clock.tick(1.0/(self.interval+randomSleepTime))
            self.callback(*self.args, **self.kwargs)
            # print("Interval", randomSleepTime, 1.0 /
            #       (self.interval+randomSleepTime))

    def stop(self):
        self.running = False
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


class Sound:
    def __init__(self):  # A place to save all suond
        pygameInit(44100, -16, 2, 64)
        # TODO: loop sound with getter in aready suond lib
        self.PressSound = pygameSound("Resources/Press2.mp3")
        self.PressSound.set_volume(0.3)
        self.PressSound.fadeout(50)
        self.ClickSound = pygameSound("Resources/Press2.mp3")
        self.ClickSound.set_volume(0.3)
        self.ClickSound.fadeout(50)
        self.ExitSound = pygameSound("Resources/Press1.mp3")
        self.ErrorSound = pygameSound("Resources/Error_Sound.mp3")
        self.ErrorSound.set_volume(0.3)
        self.ErrorSound.fadeout(50)
        self.StartSound = pygameSound("Resources/On.mp3")
        self.StartSound.set_volume(0.3)
        self.StartSound.fadeout(50)


O_Sound = Sound()
