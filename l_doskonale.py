# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:27:54 2019

@author: micha
"""

liczba = int(input("Podaj liczbe:"))

def dzielniki(i):       #szuka dzielnikow mniejszych od danej liczby
    dzielniki =[]
   
    for j in range(1,i):    #zaczynamy od 1 boo nei dzielimy przez 0
        if(i%j==0):
            dzielniki.append(j)
    return dzielniki

def doskonale(liczba):
    
    doskonale=[]
    for i in range(1,liczba):
        if(i == sum(dzielniki(i))):
            doskonale.append(i)
    print(doskonale)


#print(dzielniki(liczba))
doskonale(liczba)        


 