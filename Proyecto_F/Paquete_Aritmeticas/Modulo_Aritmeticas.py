from collections import Counter

#Modulo Aritmeticas

def media_aritmetica(a, b, c):
    return (a + b + c) / 3

def moda_aritmetica(a, b, c):
    numeros = [a, b, c]
    frecuencia = Counter(numeros)
    moda = frecuencia.most_common(1)[0][0]
    return moda

def promedio_aritmetico(a, b, c):
    return (a + b + c) / 3