# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:08:13 2019

@author: micha
"""

def dzielniki(i):       #szuka dzielnikow mniejszych od danej liczby
    dzielniki =[]
   
    for j in range(1,i):    #zaczynamy od 1 boo nei dzielimy przez 0
        if(i%j==0):
            dzielniki.append(j)
    return dzielniki

n = int(input("Podaj zakres!"))
zaprzyjaznione=[]
for i in range(1,n+1):
    sum1 = sum(dzielniki(i))
    sum2 = sum(dzielniki(sum1))
    
    
    if(i==sum2 and i!=sum1):
        if((sum1 in zaprzyjaznione) and (i in zaprzyjaznione)):
            continue
        #print(i,sum1)
        zaprzyjaznione.append(i)
        zaprzyjaznione.append(sum1)

for i in range(0,len(zaprzyjaznione)-1,2):
        print(zaprzyjaznione[i]," i ",zaprzyjaznione[i+1])    
        
print("Oto wszystkie liczby zaprzyjaznione z zakresu od 1 do ",n)