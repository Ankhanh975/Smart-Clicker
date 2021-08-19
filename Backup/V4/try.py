import time
from pygame.time import Clock
class A:
    def __init__(self):
        self.clock = Clock()

    def update(self):
        self.clock.tick(10**6)

    def get_fps(self):
        return round(self.clock.get_fps(), 2)
if __name__ == '__main__':
    a = A()
    for i in range(100):
        time.sleep(1/60)
        if i%2 == 0:
            a.update()

        print(a.get_fps())