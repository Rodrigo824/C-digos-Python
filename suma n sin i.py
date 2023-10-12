# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:43:22 2023

@author: 192462-2
"""

#Calcular la sumatoria con un vector y una i dada
def vectorSinI(tamañoVector,i):
    vector = []
    s = 0
    for index in range(0,tamañoVector+1):
        if index == i:
            continue
        else:
            vector.append(index)
    
    for suma in vector:
        s+=suma
    
    
    print("La sumatoria de",tamañoVector,"hasta 0 sin contar i es:",s)