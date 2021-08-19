import time
import cv2
import mss
import numpy

with mss.mss() as sct:
  # Part of the screen to capture
  monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

  while "Screen capturing":
      last_time = time.perf_counter()
      # Get raw pixels from the screen, save it to a Numpy array
      img = numpy.array(sct.grab(monitor))

      # Display the picture
      cv2.imshow("OpenCV/Numpy normal", img)

      # Display the picture in grayscale
      # cv2.imshow('OpenCV/Numpy grayscale',
      #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

      fps = 1 / (time.perf_counter() - last_time)
      fps = round(fps, 2)
      print("fps: {}".format(fps))

      # Press "q" to quit
      if cv2.waitKey(25) & 0xFF == ord("q"):
          cv2.destroyAllWindows()
          break