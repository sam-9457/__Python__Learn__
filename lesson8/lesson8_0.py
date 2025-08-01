import random
cash = 500

def gambling():
    times = int(input("Times:"))
    times1 = times
    while (True):
        if times > 0:
            times -= 1
            val = int(input("Number:"))
        else:
            break
gambling()