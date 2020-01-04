# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:42:18 2019

@author: micha
"""

import random
zakres = int(input("Podaj ile liczb losowych bedzieszz chchial sortowac:"))

A=[]
for liczba in range(zakres):
    A.append(random.randint(1,100))

print("nieposortowana",A)

for i in range(zakres):
    for j in range(zakres-1):
        if(A[j]>A[j+1]):
            A[j],A[j+1] = A[j+1],A[j]

print("posortowana",A)
