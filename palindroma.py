# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:29:18 2023

@author: 192462-2
"""

#Determinar si una palabra es palíndroma
def palindromo(palabra):
    palabra = list(palabra)
    palindroma = palabra.copy()
    palindroma.reverse()

    if palabra == palindroma:
        print("La palabra es palindroma")
    else:
        print("La palabra no es un palindroma")

    