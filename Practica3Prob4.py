#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:35:23 2023

@author: thebugbattler
"""
'''
La diferencia cuadrática media de las fluctuaciones se puede calcular como:

σ2 = 1.23 C2n2 k7/6 r5/3

donde σ es la diferencia cuadrática media de las fluctuaciones, Cn es la constante de estructura del índice de refracción, k es el número de onda, y r es la distancia entre los dos sensores de temperatura.

Para el caso de turbulencia intensa, Cn = 10^-13 m^-2/3, y para el caso de turbulencia pequeña, Cn = 10^-17 m^-2/3. Para una temperatura de 0°C y una presión atmosférica de 1000, 100, o 10 mbar, podemos asumir una velocidad del sonido de 331, 311, o 289 m/s respectivamente.

Usando la fórmula anterior, y asumiendo una longitud de onda de 1 cm (k = 2π/λ), y una distancia entre los sensores de temperatura de 10 cm (r = 0.1 m), podemos calcular los valores medios de la diferencia cuadrática media de las fluctuaciones para los dos casos de turbulencia y las tres presiones atmosféricas:

Para turbulencia intensa:

A una presión atmosférica de
    '''

from numpy import*

Cn=array([10**-17])# 10**-17]) #Turbulencia intensa y turbulencia pequeña

r=0.1 #Distancia entre los dos sensores en metros 
T=273 #Kelvin
P=array([100000, 10000, 1000]) #En pascales

sigma=((2*Cn)/(77.6*10**-6 *(P/T**2))**2)*r**(2/3)

print(sigma)