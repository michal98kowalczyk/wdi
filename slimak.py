# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:37:43 2019

@author: micha
"""

def slimak(h,x,y,z):
    
    
    dni=0
    postep=0
    polka=[]
    i=0
    while (i<h):
        i+=z
        polka.append(i)
    
    while(postep<h ):
        postep +=  x
        if(postep not in polka):
            postep -=y
            
        dni+=1
    return dni

h = int(input("Jak wysoki jest slup:"))
x = int(input("O ile przesuwa sie w dzien:"))        
y = int(input("O ile spada w nocy:"))    
z = int(input("co ile rozstawione sa polki:"))

print("Zajmie mu to:",slimak(h,x,y,z),"dni")
