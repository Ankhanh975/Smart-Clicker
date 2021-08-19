import time

file = "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log"

old=new=""
def main():
	while True:
		f = open(file, "r")
		new = f.read()
		time.sleep(1/60)
		if new!=old:
			print("changed")
			old=new

start = time.perf_counter()
main()

end = time.perf_counter()
print(end-start)
