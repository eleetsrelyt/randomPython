import random
import csv

def flip(count=10):
    i = 0
    while i < count:
        print random.choice([1,-1])
        i += 1

def flipaverage(count=100):
    i = 1
    t = float(random.choice([1,-1]))
    print t
    while i < count:
        f = random.choice([1,-1])
        i += 1
        t += f
        a = t/i
        print a

def flipcount(count=10000):
    i = 0
    pos = 0
    neg = 0
    while i < count:
        f = random.choice([1,-1])
        i += 1
        if f == 1:
            pos += 1
        else:
            neg += 1
    return " 1:", float(pos)/(pos + neg) * 100, "%"
    return "-1:", float(neg)/(pos + neg) * 100, "%"



    
