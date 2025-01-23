#Modulo: Main.py
from Paquete_Lectura.Lectura import *
from Paquete_Trigonometricas1.Modulo_Trigonometricas import *
from Paquete_Sumatorias.Modulo_Sumatorias import *
from Paquete_Aritmeticas.Modulo_Aritmeticas import *
from Paquete_May_Men.Modulo_May_Men import *
from Paquete_Mensajes.Modulo_Mensajes import *

x=LeerA()
y=LeerB()
z=LeerC()
astericos()
mensaje_funciones_trigonometricas()
print ("logaritmo de", x, ":", logaritmo(x))
print ("logaritmo de", y, ":", logaritmo(y))
print ("logaritmo de", z, ":", logaritmo(z))
mensajito()
print ("tangente de", x, ":", tangente(x))
print ("tangente de", y, ":", tangente(y))
print ("tangente de", z, ":", tangente(z))
mensajito()
print("Contangente de", x, ":", contangente(x))
print("Contangente de", y, ":", contangente(y))
print("Contangente de", z, ":", contangente(z))
astericos()
mensaje_funciones_sumatorias()
print ("Suma de", x, y, z, ":", Suma(x,y,z))
print ("Potencia de", x, y, z, ":", Potencia(x,y,z))
print ("Potencia al cubo de", x, y, z, ":", PotenciaCubo(x,y,z))
astericos()
mensaje_funciones_aritmeticas()
print ("Media aritmetica de",x ,y ,z ,":", media_aritmetica(x,y,z))
print ("Moda aritmetica de",x, y, z, ":", moda_aritmetica(x,y,z))
print ("Promedio aritmetico de", x ,y ,z ,":"  ,promedio_aritmetico(x,y,z))
astericos()
mensaje_funciones_mayor_menor()
print ("El mayor entre:",x, y, z, "es: ", mayor(x,y,z))
print ("El menor entre:",x, y, z, "es: ", menor(x,y,z))
