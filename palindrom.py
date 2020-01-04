# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:42:51 2019

@author: micha
"""

zdanie = input("Podaj ciag znakow i sprawdz czy jest to palindrom:")#'Napotkala typa. Zapytala "Kto pan?"'
#print(ord('a'))
#print(ord('z'))



def palindrom(zdanie):
    zdanie = zdanie.lower()
    
    nowe =""
    
    for i in zdanie:
        if (ord(i)>=97 and ord(i)<=122):
            nowe += i
    #print(nowe)
    sprawdz=""
    for i in range(len(nowe)-1,-1,-1):
        sprawdz += nowe[i]
    if(sprawdz == nowe):
        print("Zdanie jest palindromem!")
    else:
        print("Zdanie nie jest palindromem!")
    
        
        
    
palindrom(zdanie)
    