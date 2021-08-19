import time
from threading import Thread
import datetime as dt
import win32gui, win32api
import win32con #For win32gui argument

class ReadMinecreaftLog: 
	#Might break in anthor version (cần tùy chỉnh theo log của từng phiên bản)
	#mincraft reset latest.log every day
	file = "C:\\Users\\Admin\\AppData\\Roaming\\.minecraft\\logs\\latest.log"
	#file = "C:\\Users\\Admin\\Desktop\\2021-07-13-3.log"
	
	AllMode = ["3fmc Before Login", "3fmc Login Lobby", "3fmc Bedwars Lobby", "3fmc Bedwars Waiting", "3fmc Bedwars Mode", "3fmc Bedwars (Died)", "3fmc Bedwars Mode (Bed Destroyed)", "3fmc Bedwars Ended", "Minecraft Skyblock Mode"]
 
	sleepTime=0
	stop = False

	def __init__(self):
		self.mode = "3fmc Before Login"
		self.allowClick = True
		self.NotAllowClickTime = time.perf_counter()

		self.today = dt.datetime.now()  #Date this being read
		self.currentTime =  dt.time(self.today.hour, self.today.minute, self.today.second) #Init time

		self.line=""
		self.FiltedLog = []

		self.Up_KIEM = False
		self.Up_GIAP = [0,1,2,3,4][0]
		self.ACTIVE_IT_TRAP = [None, dt.time(13, 00, 00)][0]
		self.IT_TRAP = 0

		self.DEAD = 0
		self.KILL = 0
		self.LastChatSpam = [None, dt.time(self.today.hour, self.today.minute, self.today.second)][0]
		self.LastDEAD = dt.datetime.now()
		self.LastKILL = dt.datetime.now()
		self.GameStartedTime = dt.datetime.now()
		self.GameEndedTime = dt.datetime.now()

	def loop(self):
		if self.allowClick == False and time.perf_counter()-self.NotAllowClickTime > (1/20)*3:
			self.allowClick = True

		with open(self.file, "r") as self.f:
			while (not self.stop):
				time.sleep(self.sleepTime)
				self.line = self.f.readline()

				if self.line!="":
					self.sleepTime=0
					if "[Client thread/INFO]: [CHAT]" in self.line:
						self.line = self.line.replace("[Client thread/INFO]: [CHAT]", "")
						self.line = self.line.replace("\n", "")
						self.progess(self.line)
				elif self.line=="":
					self.sleepTime=1/40

	def progess(self, line):
		time1 = dt.time(int(line[1:3]), int(line[4:6]), int(line[7:9])) #[14:36:26] 
		line = line.replace(line[0:12], "")
		self.FiltedLog.append([time1, line])

		print(time1, self.mode, self.Up_KIEM, self.Up_GIAP, self.ACTIVE_IT_TRAP, self.IT_TRAP, line, sep=",")
		if "Hãy ??ng nh?p b?ng l?nh /login <m?t kh?u>" in line:
			self.__init__()
			self.mode = "3fmc Before Login"

		elif "? ??ng nh?p thành công!" in line:
			self.mode = self.AllMode[1]

		elif "GoldAppleVn ?ã vào tr?n ??u" in line or "Green_Apple_Vn ?ã vào tr?n ??u" in line:
			self.__init__()
			self.mode = self.AllMode[3]

		elif "??i th?. Nâng c?p v? khí và trang b? b?ng" in line:
			if "B?o v? gi??ng c?a b?n và phá gi??ng c?a" in self.FiltedLog[-2][1]:
				self.mode = self.AllMode[4]
				self.GameStartedTime = dt.datetime.now()

		elif "Discord https://discord.gg/Zehw9wP" in line and len(self.FiltedLog)>5:
			if "Facebook" in self.FiltedLog[-2][1]:
				if "MAKE 3F GREAT AGAIN" in self.FiltedLog[-3][1]:
					self.__init__()
					self.mode = self.AllMode[2]
		
		elif "?ã mua Sharpened Swords" in line:
			self.Up_KIEM = True
		elif "?ã mua Reinforced Armor" in line:
			line = line.split("?ã mua Reinforced Armor ")[1]
			if line=="I":
				self.Up_GIAP = 1
			elif line=="II":
				self.Up_GIAP = 2
			elif line=="III":
				self.Up_GIAP = 3
			elif line=="IV":
				self.Up_GIAP = 4

		elif "Không ?? tài nguyên! B?n c?n thêm " in line: #"3fmc Bedwars Trading without resources", 
			self.allowClick = False
			self.NotAllowClickTime = time.perf_counter()
			
		elif "It's a trap! ?ã ???c kích ho?t!" in line:
			self.ACTIVE_IT_TRAP = time1
			self.IT_TRAP -=1

		elif "?ã mua It's a trap!" in line:
			self.IT_TRAP +=1
		elif "BED > Gi??ng c?a b?n ?ã b? phá b?i" in line:
			self.mode = "3fmc Bedwars Mode (Bed Destroyed)"

		elif "???????????????????????????????????????????????????????????????????????????" in line and len(self.FiltedLog)> 5:
			if self.FiltedLog[-2][1]=="":
				if "Top 3 Kill" in self.FiltedLog[-3][1]:
					if "Top 2 Kill" in self.FiltedLog[-4][1]:
						self.mode = "3fmc Bedwars Ended"
						self.GameEndedTime = dt.datetime.now()


		elif "B?n ph?i ??i 5 giây m?i l?n dùng l?nh này!" in line:
			self.LastChatSpam = time1
		elif "b?i GoldAppleVn." in line:
			self.KILL +=1
			self.LastDEAD = time1

		elif "GoldAppleVn ?ã " in line:
			self.DEAD +=1
			self.LastKILL = time1

		#elif "GoldAppleVn", "FINAL KILL" ""3fmc Bedwars Mode (Bed Destroyed)":
		#	self.GameEndedTime = dt.datetime.now()

if __name__ == '__main__':
	LogReader = ReadMinecreaftLog()
	Thread(target = LogReader.loop).start()

	time.sleep(5)
	print( time.time())
	LogReader.stop = True
	
'''
  ----------------------------------------------------- #In "3fmc Bedwars Lobby"

                  MAKE 3F GREAT AGAIN
      Facebook https://fb.com/groups/LeagueOf3F
      Discord https://discord.gg/Zehw9wP

  -----------------------------------------------------

#In "3fmc Bedwars Mode"
  ??????????????????????????????????????????????????????????????????????????? 
                                     BedWars

       B?o v? gi??ng c?a b?n và phá gi??ng c?a
       ??i th?. Nâng c?p v? khí và trang b? b?ng
       cách thu th?p các tài nguyên.

  ???????????????????????????????????????????????????????????????????????????

"Không ?? tài nguyên! B?n c?n thêm " #Stop left click (if not click untid relase Mbutton)when have this log
"?ã mua Sharpened Swords" #Thoi said up kIEM
Noob_TGminh ?ã mua Reinforced Armor I

  ???????????????????????????????????????????????????????????????????????????
                                     BedWars

            Blue - namanh14072007 Im_Chien BeCanTapChoi ltz_Josio2


                      Top 1 Kill: GoldAppleVn - 13
                      Top 2 Kill: Im_Chien - 7
                      Top 3 Kill: BeCanTapChoi - 7

  ???????????????????????????????????????????????????????????????????????????
'''
