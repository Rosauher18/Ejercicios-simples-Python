"""
Realiza la potencia de un numero 
"""

print("Calculadora de potencias")
num = input('Ingresa el numero que vas a potenciar: ')
num = int(num)
potencia = input('Ingresa el valor del exponente: ')
potencia = int(potencia)

resultado = num ** potencia

print(f"El resultado de la potenciacion es: {resultado}")
