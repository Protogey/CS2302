def discover(trig, tries=1000,tolerance=0.0001):#used a similar way like given in class
    for i in range(tries):#this allows us to iterate mutiple times
        t = random.uniform(-math.pi, math.pi)#random number for t from -pi to pi
        f1 = trig[random.randrange(0, len(trig))]#gives a random trig function
        f2 = trig[random.randrange(0, len(trig))]#gives a random trig function
        if f1 != f2:#if f1 and f2 are the same we do not do anything else
            y1 = eval(f1)#we evaluate
            y2 = eval(f2)#we evaluate 
            if np.abs(y1-y2)>tolerance:#if they are the same, we return
                print(f1," and ",f2," are the same")
                return False
    return True

def subsetsum(S,last,goal):#modified given subset from class and updated last by -1
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last-1])
    if res:
        subset.append(S[last-1])
        return True, subset
    else:
        return subsetsum(S,last-1,goal)

def partition(S):
    s = 0#we partition and check if our number is even, if it is not, we cannot continue
    for i in range(len(S)):
        s += S[i]
    if s%2 == 0:
        return subsetsum(S, len(S), s/2)
    return False

import math
from math import *
from mpmath import *
import random
import numpy as np
trig = ['sin(t)','cos(t)','tan(t)','sec(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)',
        'tan(-1*t)','sin(t)/cos(t)','2*sin(t/2)*cos(t/2)','sin(t)*sin(t)','1-(cos(t)*cos(t))','1-cos(2*t)/2','1/cos(t)']
print(discover(trig))
S = [2, 4, 5, 9, 12]
print(partition(S))
