from itertools import count
from time import sleep

delay = int(input())
reload = int(input())

windows = []

for bullet in count():
    if (len(windows) >= 2):
        break
    bullet = (bullet+1)*delay
    if (bullet % (120+reload) >= 120 or bullet % (120+reload) == 0):
        windows.append(bullet)

for window in windows:
    print(window, end=" ")
