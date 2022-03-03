# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:16:06 2022

@author: jtorres67
"""
#1
redes = int(input('ingrese la cantidad de alumnos en redes: '))
contabilidad = int(input('ingrese la cantidad de alumnos en contabilidad: '))
diseno = int(input('ingrese la cantidad de alunmos en diseño: '))

total = redes + contabilidad + diseno 

porcentajeRedes = (redes/total)*100
porcentajeContabilidad = (contabilidad/total)*100
porcentajeDiseno = (diseno/total)*100

print('el porcentaje de estudiantes que estudian redes es: ',porcentajeRedes, '%' )
print('el porcentaje de estudiantes que estudian contabilidad es: ',porcentajeContabilidad, '%' )
print('el porcentaje de estudiantes que estudian redes es: ',porcentajeDiseno, '%' )