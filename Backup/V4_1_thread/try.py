from os import system as OsCmdControl
from time import perf_counter
import time, random
start = perf_counter()
for i in range(100):
	OsCmdControl("color 21")
print(perf_counter()-start)
print(perf_counter()-start)
print(perf_counter()-start)
print(perf_counter()-start)
time.sleep(50)