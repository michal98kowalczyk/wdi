# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:40:25 2019

@author: micha
"""

#lata od 2000 do 2018
nazwy = ["styczen","luty","marzec",\
         "kwiecien","maj","czerwiec","lipiec","sierpien","wrzesien","pazdziernik","listopad","grudzien"]
miesiace=[31,28,31,30,31,30,31,31,30,31,30,31]

day_of_week = 1
day_of_month=1
piatki13 = 0

print("Piatki 13 w latach 2000-2018 byly w nastepujacyhc miesiacach:")

for i in range(2000,2018+1):
    print("\nRok" + str(i))
    
    miesiace[1]=28
    if(i%4==0):
        miesiace[1]=29
    obecny=0 #obliczany miesiac
    while obecny <12 :
        day_of_week +=1
        day_of_month +=1
        
        if day_of_week >7 :
            day_of_week = 1
        if day_of_month > miesiace[obecny] : 
            day_of_month = 1
            obecny += 1
        if day_of_month==13 and day_of_week==5 :
            piatki13 +=1
            print("piatek 13 byl w ",nazwy[obecny])
    
print("W latach 2000-2018 piatek 13 wystapil lacznie " + str(piatki13) + " razy")            