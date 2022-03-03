# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#2
per1= int(input('Ingrese el dinero invertido por la primera persona: '))
per2= int(input('Ingrese el dinero invertido por la segunda persona: '))
per3= int(input('Ingrese el dinero invertido por la segunda persona: '))

total = per1+per2+per3
p1= (per1/total)*100
p2= (per2/total)*100
p3= (per3/total)*100
print( "La persona 1 invirtió un %", p1)
print("La persona 2 invirtió un %", p2)
print( "La persona 3 invirtió un %", p3 ,"El valor total invertido es:", total)

