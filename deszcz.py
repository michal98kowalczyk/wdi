# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:13:14 2019

@author: micha
"""

from random import randint
import os
import time

n = int(input("Jak duzy jest deszcz:"))

tab = ["o"]*n
#print(tab)
j=4
while(j):
    for i in range(n):
        x=randint(0,n-1)
        
        
        
        
        tab[x]="*"
        for k in tab:
            print(k, end="")
        print()
        
        tab[x]="o"
        
    time.sleep(0.3)
    os.system('clear')
    j-=1
    print()