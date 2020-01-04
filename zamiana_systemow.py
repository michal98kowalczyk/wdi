# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:26:53 2019

@author: micha
"""

#zamiana systemow z "dowolnego na dowolny" z ogrniczeniem do co najwyzej dziesietnego


def dziesietny(liczba,sys1):
    potega=0
    n=len(liczba)
    nowa = 0
    for i  in range(n-1,-1,-1):
        
        nowa += (int(liczba[i]) * (sys1**potega))
        
        
        potega+=1
    print()    
    print("W systemie dziesietnym:",nowa)
    return nowa
 


def zamiana(liczba,sys1,sys2):
    nowa = dziesietny(liczba,sys1)
    inna=""
    while nowa>0 : 
        inna += str(nowa%sys2)
        nowa //= sys2
    gotowa=""
    for i in range (len(inna)-1,-1,-1):
        gotowa += inna[i]
    #print(gotowa)   
    return gotowa
    
sys1 = int(input("Podaj system w ktorym wprowadzisz liczbe:"))
liczba = input("Podaj swoja liczbe w systemie:" + str(sys1)+" ")

    
#nowa=dziesietny(liczba,sys1)
sys2=int(input("Na jaki system chcesz zamienic owa liczbe?"))

print("W systemie ",sys2,"liczba wyglada tak:",zamiana(liczba,sys1,sys2))