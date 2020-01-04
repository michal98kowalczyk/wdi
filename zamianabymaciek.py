# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:37:59 2019

@author: micha
"""

numbers='0123456789abcdefghijklmnopqrstuvwxyz'
system_z=int(input('Podaj system z którego chcesz konwertować: '))
system_na=int(input('Podaj system na który chcesz konwertować: '))
liczba=input('Podaj liczbe w systemie: ')
def na_dziesietny(system,liczba,numbers):
    liczba_w_dzies=0
    for i in range(0,len(liczba)):
        for j in range(0,len(numbers)):
            if (liczba[i]==numbers[j]):
                liczba_w_dzies=j*pow(system,len(liczba)-1-i)+liczba_w_dzies
    return liczba_w_dzies
def z_dziesietnego(system,liczba,numbers):
    A=[]
    while (liczba>0):
        A.append(numbers[liczba%system])
        liczba=int(liczba/system)
    return A

liczba_w_dzies=na_dziesietny(system_z,liczba,numbers)
A=[]
A=z_dziesietnego(system_na,liczba_w_dzies,numbers)
for i in range(len(A)-1,-1,-1):
    print(A[i], end='')