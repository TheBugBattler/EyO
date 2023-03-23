#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:38:42 2023

@author: thebugbattler
"""



from numpy import*
from pylab import*



zd=array([10.0, 16.5, 22.5, 31.2, 36.8, 48.0, 51.7, 57.0, 62.0])
y=array([7.77, 7.76, 7.77, 7.78, 7.79, 7.82, 7.85, 7.87, 7.93])

zdrad=zd*((2*pi)/360) #Pasamos a radianes para poder calcular seno y cose
    
x=1/cos(zdrad) #Formula masa de aire


a,b=polyfit(x, y, 1) #x,y

y_ajuste=a*x+b #a, b



p_datos=plot(x, y, "r.")

p_ajuste=plot(x, y_ajuste, "b-")

grid()
xlabel("Masa de aire")
ylabel("Magnitud")
legend(("Datos", "Recta ajuste"), loc="best")


print(a) #Extincion

print(b) #Magnitud


# Cálculo del error de mínimos cuadrados
error = np.sum((y - (a*x + b))**2)

# Cálculo de la matriz de covarianza
n = len(x)
x_mean = np.mean(x)
SS_xx = np.sum((x - x_mean)**2)
s_sq = error/(n-2)
var_a = s_sq/SS_xx
var_b = s_sq*(1/n + x_mean**2/SS_xx)

cov_matrix = np.array([[var_a, 0], [0, var_b]])

# Cálculo del error de los parámetros
print("Error de a:", np.sqrt(cov_matrix[0, 0]))
print("Error de b:", np.sqrt(cov_matrix[1, 1]))


