"""
Calcula el promedio de una lista de numeros

"""
numeros = input("Ingrese los valores separados por un espacio: ")

lista = numeros.split()
lista = [int(valor) for valor in lista] #convierte los valores a flotantes 

print(f'La lista ingresada es: {lista}')

promedio = sum(lista) / len(lista)

print(f'El promedio es: {promedio}')