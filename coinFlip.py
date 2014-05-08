import random
import csv

def flip(count=10, heads=False):
    i = 0
    output = []
    while i < count:
        if heads == False:
            output.append(random.choice([10,-10]))
        else:
            output.append(random.choice(['Heads','Tails']))
        i += 1
    return output

def flipaverage(count=100):
    i = 1
    t = float(random.choice([10,-10]))
    print t
    while i < count:
        f = random.choice([10,-10])
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
    print "heads:", float(pos)/(pos + neg) * 100, "%"
    print "tails:", float(neg)/(pos + neg) * 100, "%"

def writeflipaverage(flips=10, count=10):
    o = open(str(flips) + ' flips x ' + str(count) + 'coins.csv', 'w')
    i = 1
    c = 0
    header = []
    header.append('coinXflip')
    while c < flips:
        c += 1
        header.append('flip' + str(c))
    o.write(str(header) + '\n')
    while i <= count:
        j = 1
        out = []
        out.append('coin' + str(i))
        t = float(random.choice([1,-1]))
        out.append(t)
        while j < flips:
            j += 1
            f = float(random.choice([1,-1]))
            t += f
            a = t/j
            out.append(a)
        o.write(str(out) + '\n')
        i += 1
    o.close()
    
