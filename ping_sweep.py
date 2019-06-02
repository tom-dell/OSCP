import os
import re

alive = open('alive.txt', 'w+')

ip = ("10.11.1.")

for i in range(6):
    address = ip + str(i)
    response = os.system ("ping -c 3 " + address)
    if response == 0:
        alive.write(address + "\n")
