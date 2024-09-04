"""
Ejercicio 2
Calcula el area de un circulo
con un radio dado
"""

import math

radio = input('Introduce el radio del circulo: ')
radio = int(radio)
area = math.pi * radio **2

print(f'El area del circulo es: {area}')