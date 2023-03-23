#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:48:39 2023

@author: thebugbattler
"""

from numpy import *


#Problema 3
#Datos

v=10**(-5) #m²*s⁻1

epsi=array([10**-1, 10**-3, 10**-5]) #m²*s⁻3
#FOrmulas pag 21

l0=(v**3/epsi)**(1/4)
t0=(v/epsi)**(1/2)
u0=l0/t0

print(l0)
print(t0)
print(u0)



