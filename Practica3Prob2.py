#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:50:53 2023

@author: thebugbattler
"""
#Problema 2
'''
El ángulo isoplanático se puede calcular a partir del parámetro de Fried, que está dado por:

$$r_0 = 0.423 \frac{\lambda}{\sqrt{C_n^2}}$$

donde $\lambda$ es la longitud de onda de la luz y $C_n^2$ es la constante de estructura de la capa turbulenta. La constante de estructura es una medida de la variación de la densidad del aire en la capa turbulenta y se puede relacionar con la velocidad del viento $v$ y la altura $h$ de la capa turbulenta mediante:

$$C_n^2 = 1.23\times10^{-14}\left(\frac{v}{h}\right)^{2/3}$$

Para una longitud de onda de 400 nm, el parámetro de Fried es:

$$r_0 = 0.423 \frac{400,\text{nm}}{\sqrt{1.23\times10^{-14}\left(\frac{80,\text{km/h}}{8,\text{km}}\right)^{2/3}}} \approx 8,\text{cm}$$

El ángulo isoplanático se puede calcular como:

$$\theta_0 = 1.22 \frac{\lambda}{r_0} \approx 1.22 \frac{400,\text{nm}}{8,\text{cm}} \approx 0.06,\text{arcsec}$$

El tiempo característico de variación de la turbulencia está dado por:

$$\tau_0 = \frac{r_0}{v}$$

Para una longitud de onda de 400 nm:

$$\tau_0 \approx \frac{8,\text{cm}}{80,\text{km/h}} \approx 0.01,\text{s}$$

Para una longitud de onda de 1.6 micras, el parámetro de Fried se puede calcular como:

$$r_0 = 0.423 \frac{1.6,\mu\text{m}}{\sqrt{1.23\times10^{-14}\left(\frac{80,\text{km/h}}{8,\text{km}}\right)^{2/3}}} \approx 32,\text{cm}$$

El ángulo isoplanático para esta longitud de onda es:

$$\theta_0 \approx 1.22 \frac{1.6,\mu\text{m}}{32,\text{cm}} \approx 0.06,\text{arcsec}$$

El tiempo característico de variación de la turbulencia para esta longitud de onda es:

$$\tau_0 \approx \frac{32,\text{cm}}{80,\text{km/h}} \approx 0.04,\text{s}$$
'''



from numpy import*
from pylab import*

#En una primera aproximacion


v=22.22#m/s
h=8000 #m
r0=0.08 #Parametro de Fried en m
l=array([400*10**-9, 1.6*10**-6]) # longitud de onda en metros


iso=0.31*(r0/h) #Formula angulo isoplanatico #En radianes

t0=0.31*(r0/v) #Tiempo característico
print(iso)

print(t0)


#Segun pdf Jairo
z=0
H=1/cos(z)

v0=0.31*(r0/H)

