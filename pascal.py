# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:53:49 2019

@author: micha
"""

def pascal(n,k):
    if n==k or n==0:
        return 1
    if k==1 or k==n-1:
        return n
    
    return pascal(n-1,k-1) + pascal(n,k-1)

n = int(input("Podaj liczbe:"))

for  i in range(0,n+1):
    for j in range(0,i+1):
        print(pascal(j,i), end=" ")
    print(" ")