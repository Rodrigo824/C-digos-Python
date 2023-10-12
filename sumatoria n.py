# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:20:45 2023

@author: 192462-2
"""

#Calcular la sumatoria de  n
def sumatoria(num):
    s = 0
    for index in range(0,num+1):
        s+=index
    
    print("La sumatoria de",num,"hasta 0 es:",s)