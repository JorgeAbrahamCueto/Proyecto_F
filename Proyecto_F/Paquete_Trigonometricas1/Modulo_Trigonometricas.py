#Modulo trigonometricas

import math

#logaritmo
def logaritmo(a):
    return math.log(a)

#para la tangente convertir grados a radianes
def angulo_radianes(a):
    return math.radians(a)

def tangente(angulo_radianes):
    return math.tan(angulo_radianes)

# para la contangente
def contangente(a):
    angulo_rad = angulo_radianes(a)  
    return 1 / tangente(angulo_rad)