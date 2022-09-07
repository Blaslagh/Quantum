# -*- coding: utf-8 -*-


def sumuj():
    m, n = input().split()
    s=0
    w = input().split()
    for i in range(int(m)*int(n)):
        s+=int(w[i])
    return s

        
def sumuj_z_tablicy(x, s=0):
    for i in x:
        s += sum(i)
    return s        
