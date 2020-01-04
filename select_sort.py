# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:01:55 2019

@author: micha
"""

from random import randint

ile = int(input("Ile liczb chcesz sortowac:"))
zakres = int(input("Podaj gorna granice zakresu liczb:"))
A = []

for i in range(ile):
    A.append(randint(1,zakres))

print("Nieposortowana:",A)

def minimum_index(array,j):
    
    mini=j
    for i in range(j+1,len(array)):
        if(A[i]<A[mini]):
            mini=i
    #print(mini)
    return mini
def select_sort(array):
    n=len(array)
    
    for i in range(n):
        x=minimum_index(array,i)
        
        A[i],A[x] = A[x],A[i]
    return A    
print("Posortowana:",select_sort(A))    