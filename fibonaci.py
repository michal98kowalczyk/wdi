# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:29:52 2019

@author: micha
"""

def rekurencyjnie(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return rekurencyjnie(n-1) + rekurencyjnie(n-2)
    
def iteracyjnie(n):
    if(n<2):
        return 1
    else:
        fib1=0
        fib2=1
        for i in range(2,n+1):
            tmp = fib1+fib2
            fib1=fib2
            fib2=tmp
            
        return fib2
n=int(input("Dla ilu liczb chcesz wywolac fibonacii?"))

print("Rekurencyjenie:")
for i in range(n+1):
    print("Dla",i,"wynosi",rekurencyjnie(i))
    

print("Iteracyjnie:")
for i in range(n+1):
    print("Dla",i,"wynosi",iteracyjnie(i))