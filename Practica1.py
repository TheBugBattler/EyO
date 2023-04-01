    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Programa Entregable 1 EyO

from numpy import*
from pylab import*
from pandas import*
from scipy import *
from scipy.integrate import quad


#Datos filtro H

filtroh = loadtxt('H_trans.dat', skiprows=2)
# Acceder a la primera columna (x)
xh = filtroh[:, 0] #Numero de onda
# Acceder a la segunda columna (y) transmision filtro
yh = filtroh[:, 1]

#Datos filtro J
filtroj=loadtxt("J_trans.dat", skiprows=2)
xj = filtroj[:, 0] #Numero de onda
# Acceder a la segunda columna (y)
yj = filtroj[:, 1]


#Datos filtros K

filtrok=loadtxt("Kshort_trans.dat", skiprows=2)
xk=filtrok[:,0]
yk=filtrok[:,1]


#Datos Vega

vega=loadtxt("vegfluxtot.dat", skiprows=2)
vegax=vega[:,0]
vegay=vega[:,1]


#Datos ukA0V
ukA0v=loadtxt("uka0v.dat", skiprows=2)
ukxan=ukA0v[:,0] #Longitud de onda en angstrom
ukx=ukxan/10000 #Pasamos a micras
uky=ukA0v[:,1] #Flujo


#Datos ukk5iii
ukk5=loadtxt("ukk5iii.dat", skiprows=2)
ukk5a=ukk5[:,0]
ukk5x=ukk5a/10000 #Pasamos a micras longitud de onda
ukky=ukk5[:,1] #Flujo


p1,p2,p3=plot(xh, yh, "r-", xj, yj, "b-", xk, yk, "g-") #Representacion ventana de los filtros
fill(xh,yh, "r", xj, yj ,"b", xk,yk, "g")
legend(("Filtro H", "Filtro J", "Filtro K"), loc="upper left")
xlabel("Longitud de onda ${\mu m}$")
ylabel("Transmisión tanto por uno")



# Interpolacion

Fint_veg = interpolate.interp1d(vegax,vegay, kind = 'cubic')
Fint_k5iii = interpolate.interp1d(ukk5x, ukky, kind = 'cubic')
Fint_a0v = interpolate.interp1d(ukx, uky, kind = 'cubic')


# Interpolacion

Jint = interpolate.interp1d(xj, yj, kind = 'cubic')
Hint = interpolate.interp1d(xh, yh, kind = 'cubic')
Kint = interpolate.interp1d(xk, yk, kind = 'cubic')



def F_veg(l): 

        return Fint_veg(l) 

def Fn_k5iii(l): 

        return Fint_k5iii(l)

def Fn_a0v(l):
    
        return Fint_a0v(l)

def J(l): 
        if xj[0]<= l <= xj[-1]:
            return Jint(l)
        else:
            return 0.

def H(l):
        if xh[0]<= l <= xh[-1]:
            return Hint(l)
        else:
            return 0.

def K(l):
        if xk[0]<= l <= xk[-1]:
            return Kint(l)
        else:
            return 0.
 
    
# Integracion flujo de vega en cada filtro


JF_0 = quad(lambda l: 0.3*F_veg(l)*J(l),  1.03000 , 1.44700)[0] 

HF_0 = quad(lambda l: 0.3*F_veg(l)*H(l), 1.36500, 1.88000)[0]

KF_0 = quad(lambda l: 0.3*F_veg(l)*K(l), 1.89000, 2.39700)[0]


### Apartado A ###

def E(m, F0):
        return 25. * np.pi * F0 * 10**(-m/2.5)

mag = np.array([10., 15., 20.]) 



E_J = E(mag, JF_0); print(E_J)
E_H = E(mag, HF_0); print(E_H) # W m^-2 um^-1
E_K = E(mag, KF_0); print(E_K)

#APARTADO B------------------------------------------------------------------------------------------------------------------------------------------------------

masaire=1.5

mprima=array([10., 15., 20.])

#PARA EJ
print("EJ")
### 0.2###

ext1=0.2
m1=mprima+ext1*masaire

def E2J(m1,F0):
        return 25. * np.pi * F0 * 10**(-m1/2.5)
E_J2= E2J(m1,JF_0); print(E_J2)

###0.15###

ext2=0.15
m2=mprima+ext2*masaire

def E15J(m2,F0):
        return 25. * np.pi * F0 * 10**(-m2/2.5)
E_J3=E15J(m2,JF_0); print(E_J3)

### 0.1
ext3=0.1
m3=mprima+ext3*masaire


def E1J(m3,F0):
        return 25. * np.pi * F0 * 10**(-m3/2.5)
E_J1=E1J(m3,JF_0); print(E_J1)

print("EH")

#PARA EH
##0.2

def E2H(m1,F0):
    
        return 25. * np.pi * F0 * 10**(-m1/2.5)
    
E_H2= E2H(m1,HF_0); print(E_H2)


#0.15
def E15H(m2,F0):
        return 25. * np.pi * F0 * 10**(-m2/2.5)
E_H3=E15H(m2,HF_0); print(E_H3)


#0.1
def E1H(m3,F0):
        return 25. * np.pi * F0 * 10**(-m3/2.5)
E_H1=E1J(m3,HF_0); print(E_H1)


##PARA EK
print("EK")
#0.2

def E2K(m1,F0):
        return 25. * np.pi * F0 * 10**(-m1/2.5)
    
E_K2= E2K(m1,KF_0); print(E_K2)


#0.15

def E15K(m2,F0):
        return 25. * np.pi * F0 * 10**(-m2/2.5)
E_K3=E15K(m2,KF_0); print(E_K3)

#0.1

def E1K(m3,F0):
        return 25. * np.pi * F0 * 10**(-m3/2.5)
E_K1=E1K(m3,KF_0); print(E_K1)

#CALCULO DE ENERGIA EN FOTONES --------------------------------------------------------------------------------------------------------------------------

hc=1.98*10**(-19) 

JF_0P = quad(lambda l: (0.3*F_veg(l)*J(l))*l/hc,  1.03000 , 1.44700)[0] 

HF_0P = quad(lambda l: (0.3*F_veg(l)*H(l))*l/hc, 1.36500, 1.88000)[0]

KF_0P = quad(lambda l: (0.3*F_veg(l)*K(l))*l/hc, 1.89000, 2.39700)[0]

#SIN EXTINCION
print("Energia en fotones sin extincion")

E_JP = E(mag, JF_0P); print(E_JP)
E_HP = E(mag, HF_0P); print(E_HP) 
E_KP = E(mag, KF_0P); print(E_KP)



#PARA EJ fotones
print("EJ fotones")
### 0.2###


def E2JP(m1,F0):
        return 25. * np.pi * F0 * 10**(-m1/2.5)
E_J2P= E2JP(m1,JF_0P); print(E_J2P)
    
###0.15###



def E15JP(m2,F0):
        return 25. * np.pi * F0 * 10**(-m2/2.5)
E_J3P=E15JP(m2,JF_0P); print(E_J3P)

### 0.1
ext3=0.1
m3=mprima+ext3*masaire


def E1JP(m3,F0):
        return 25. * np.pi * F0 * 10**(-m3/2.5)
E_J1P=E1JP(m3,JF_0P); print(E_J1P)

print("EH fotones")

#PARA EH
##0.2

def E2HP(m1,F0):
    
        return 25. * np.pi * F0 * 10**(-m1/2.5)
    
E_H2P= E2HP(m1,HF_0P); print(E_H2P)


#0.15
def E15HP(m2,F0):
        return 25. * np.pi * F0 * 10**(-m2/2.5)
E_H3P=E15HP(m2,HF_0P); print(E_H3P)


#0.1
def E1HP(m3,F0):
        return 25. * np.pi * F0 * 10**(-m3/2.5)
E_H1P=E1JP(m3,HF_0P); print(E_H1P)


##PARA EK
print("EK fotones")
#0.2

def E2KP(m1,F0):
        return 25. * np.pi * F0 * 10**(-m1/2.5)
    
E_K2P= E2KP(m1,KF_0P); print(E_K2P)



#0.15

def E15KP(m2,F0):
        return 25. * np.pi * F0 * 10**(-m2/2.5)
E_K3P=E15KP(m2,KF_0P); print(E_K3P)

#0.1

def E1KP(m3,F0):
        return 25. * np.pi * F0 * 10**(-m3/2.5)
E_K1P=E1KP(m3,KF_0P); print(E_K1P)



#APARTADO C----------------------------------------------------------------------------------------------------------------------------



#Procedemos a calcular en primer lugar el flujo total para cada filtro

FtotalJ=JF_0 *10**(-10/2.5)

print(FtotalJ) #Flujo total filtro J

FtotalH=HF_0 *10**(-10/2.5)

print(FtotalH) #Flujo total filtro H

FtotalK=KF_0 *10**(-10/2.5)

print(FtotalK) #Flujo0 total filtro K

#Calculamos ahora las constantes de normalizacion
#A0V



JFN_0 = quad(lambda l: 0.3*Fn_a0v(l)*J(l), 1.03000 , 1.44700)[0]
print(JFN_0)


CJ=(FtotalJ/JFN_0) 

print(CJ)


HFN_0 = quad(lambda l: 0.3*Fn_a0v(l)*H(l), 1.36500, 1.88000)[0] 
CH=FtotalH/HFN_0
print(CH)


KFN_0 = quad(lambda l: 0.3*Fn_a0v(l)*K(l), 1.89000, 2.39700)[0]
CK=FtotalK/KFN_0
print(CK)

#Calculamos ahora las constantes de normalizacion
#K5III

JFK_0=quad(lambda l: 0.3*Fn_k5iii(l)*J(l), 1.03000 , 1.44700)[0]
CJK=FtotalJ/JFK_0
print(CJK)

HFNK_0 = quad(lambda l: 0.3*Fn_k5iii(l)*H(l), 1.36500, 1.88000)[0]
CHK=FtotalH/HFNK_0
print(CHK)

KFNK_0 = quad(lambda l: 0.3*Fn_k5iii(l)*K(l), 1.89000, 2.39700)[0]
CKK=FtotalK/KFNK_0
print(CKK)


#Ya tenemos el valor de las constantes de normalizacion ahora simplemente las multiplicamos for el flujo normalizado de cada estrella y ya tendriamos el flujo
#Para A0V en w


FlujoA0VJ=uky*CJ
FlujoA0VH=uky*CH
FlujoA0VK=uky*CK


p4=plot(ukx, FlujoA0VJ, "r")
p5=plot(ukx, FlujoA0VH, "b")
p6=plot(ukx, FlujoA0VK, "g")

title("A0V")
xlabel("Longitud de onda ${\mu m}$ ")
ylabel('Flujo (W m$^{-2}$ μm$^{-1}$)')
legend(("Filtro J", "Filtro H", "Filtro K"))
#Vemos que son todos iguales

#Para K5III en W

FlujoK5J=ukky*CJK
FlujoK5H=ukky*CHK
FlujoK5K=ukky*CKK

p7=plot(ukk5x, FlujoK5J)
p8=plot(ukk5x, FlujoK5H)
p9=plot(ukk5x, FlujoK5K)

title("K5III")
xlabel("Longitud de onda ${\mu m}$ ")
ylabel('Flujo (W m$^{-2}$ μm$^{-1}$)')
legend(("Filtro J", "Filtro H", "Filtro K"))




#Ahora tenemos que calcularlo para fotones

#A0V

JFN_0P = quad(lambda l: (0.3*Fn_a0v(l)*J(l))*l/hc,  1.03000 , 1.44700)[0] 

HFN_0P = quad(lambda l: (0.3*Fn_a0v(l)*H(l))*l/hc, 1.36500, 1.88000)[0]

KFN_0P = quad(lambda l: (0.3*Fn_a0v(l)*K(l))*l/hc, 1.89000, 2.39700)[0]


#Flujos en fotones

FtotalJP=JF_0P*10**(-10/2.5) 
print(FtotalJP)

FtotalHP=HF_0P*10**(-10/2.5) 
print(FtotalHP)

FtotalKP=KF_0P*10**(-10/2.5) 
print(FtotalKP)

#Calculamos constantes de normalizacion en fotones

CJP=FtotalJP/JFN_0P

print(CJP)

CHP=FtotalHP/HFN_0P
print(CHP)

CKP=FtotalKP/KFN_0P
print(CKP)

FlujoA0VJP=uky*CJP
FlujoA0VJP=(FlujoA0VJP/0.5556) #Normalizamos 
FlujoA0VHP=uky*CHP
FlujoA0VHP=(FlujoA0VHP/0.5556)
FlujoA0VKP=uky*CKP
FlujoA0VKP=(FlujoA0VKP/0.5556)



p4P=plot(ukx, FlujoA0VJP, "r")
p5P=plot(ukx, FlujoA0VHP,"b")
p6P=plot(ukx, FlujoA0VKP,"g")

title("A0V")
xlabel("Longitud de onda ${\mu m}$ ")
ylabel("Flujo (ph $s^{-1}$ $m^{-2} \mu m^{-1}$)")
legend(("Filtro J", "Filtro H", "Filtro K"))

#UK en fotones
#Obtenemos las constantes de normalizacion en fotones

JFNK_0P = quad(lambda l: (0.3*Fn_k5iii(l)*J(l))*l/hc,  1.03000 , 1.44700)[0] 

HFNK_0P = quad(lambda l: (0.3*Fn_k5iii(l)*H(l))*l/hc, 1.36500, 1.88000)[0]

KFNK_0P = quad(lambda l: (0.3*Fn_k5iii(l)*K(l))*l/hc, 1.89000, 2.39700)[0]

CJPK=FtotalJP/JFNK_0P
print(CJPK)
CHPK=FtotalHP/HFNK_0P
print(CHPK)
CKPK=FtotalKP/KFNK_0P
print(CKPK)

FlujoVJP=ukky*CJPK

FlujoVJP=(FlujoVJP/0.5556) #Normalizamos 

FlujoVHP=ukky*CHPK

FlujoVHP=(FlujoVHP/0.5556)

FlujoVKP=ukky*CKPK
FlujoVKP=(FlujoVKP/0.5556)

p7P=plot(ukk5x, FlujoVJP, "r")
p8P=plot(ukk5x, FlujoVHP, "b")
p9P=plot(ukk5x, FlujoVKP,"g")

title("K5III")
xlabel("Longitud de onda ${\mu m}$ ")
ylabel("Flujo (ph $s^{-1}$ $m^{-2} \mu m^{-1}$)")
legend(("Filtro J", "Filtro H", "Filtro K"))
