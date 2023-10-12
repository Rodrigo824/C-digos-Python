# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:52:36 2023

@author: 192462-2
"""

#Calcular la sumatoria con un vector y una i dada sin if
#Calcular la sumatoria con un vector y una i dada
def vectorSuma(tamañoVector,i):
    vector = []
    s = 0
    for index in range(0,tamañoVector+1):
        vector.append(index)

    vector = vector [0:i] + vector[i+1:]

    for suma in vector:
        s+=suma
      
    print("La sumatoria de",tamañoVector,"hasta 0 sin contar i es:",s)