# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:10:52 2022

@author: jtorres67
"""

#3

sbase=int(input('Ingrese su sueldo base $'))
nv=int(input('Ingrese la cantidad de ventas en el mes '))
porc=(sbase*15)/100
c=porc*nv
totalsueldo= sbase+c
print("El valor total por comision es: $", c, "El dinero total que obtendra en el mes es: $", totalsueldo)

