from math import *

def tinhsincos (n):
    y = []
    z = []
    for i in range(len(n)):
        y.append(pi/2 - n[i])
        z.append(cos(n[i]) -  sin(n[i]))

    return y,z
