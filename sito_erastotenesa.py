# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:05:06 2019

@author: micha
"""
from math import sqrt

n = int(input("Podaj zakres:"))

def sito(n):
    A=[False]*2
    #print(A)
    for i in range(2,n+1):
        A.append(True)
    #print(A)
    for i in range(2,int(sqrt(n))):
        if(A[i]==True):
            j=2*i
            while(j<=n):
                A[j]=False
                j+=i
    #print(A)
    pierwsze = []       
    for i in range(len(A)-1):
        if(A[i]==True):
            pierwsze.append(i)
            
                
    
    return pierwsze
        
pierwsze = sito(n)    
print("Liczby pierwsze z zakresu od 2 do ",n," to: ",pierwsze)