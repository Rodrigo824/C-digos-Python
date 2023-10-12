# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:16:17 2023

@author: 192462-2
"""

#Calcular el factorial de un numero dado
def Factorial(num):
    factorial = 1
    for index in range(1,num+1):
        factorial*=index
    
    print("El factorial de",num,"es:",factorial)