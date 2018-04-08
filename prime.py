# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 19:40:48 2018

@author: Stephen Hill
2
find monisen

"""
from math import sqrt


def prime(n):
    if n == 1:
        return False
    else:
        k = int(sqrt(n))+1
        for i in range(2,k):
            if n%i == 0:
                return False
            else:
                return True,n

def monisen(x):    
    count = 0
    while count < x:
        if prime(x):
            M = 2**x -1
        else:
            continue
        if prime(M):
            count += count
        else:
            continue
    else:
        print(M)
 
    
print(mon)
#print(monisen(int(input())))