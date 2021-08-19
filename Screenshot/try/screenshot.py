import time, pygame
import cv2
import mss
import numpy

clock =  pygame.time.Clock()
with mss.mss() as sct:
  # Part of the screen to capture
  monitor = {"top": 0, "left": 0, "width": 100, "height": 100}

  while True:
      clock.tick(60)
      print(round(clock.get_fps(), 2))

      img = numpy.array(sct.grab(monitor))

      cv2.imshow("OpenCV/Numpy normal", img)
      if cv2.waitKey(25) & 0xFF == ord("q"):
          cv2.destroyAllWindows()
          break


'''
from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time

mon = {'top': 100, 'left':200, 'width':1600, 'height':1024}

sct = mss()

while 1:
    begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('test', np.array(img_bgr))
    print('This frame takes {} seconds.'.format(time()-begin_time))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break'''
