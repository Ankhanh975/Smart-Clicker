import sys
from os import system as OsCmd

sys.stdout = open("log.txt", 'a')
sys.stderr = open("log.txt", 'a')
print("4")
OsCmd("echo 1")
print(sys.__stdout__)
0/0
sys.stdout = sys.__stdout__
print("4")

