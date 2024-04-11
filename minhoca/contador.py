import random

numeros = [random.randint(-10, 10) for _ in range(100)]

contador_positivos = 0

for numero in numeros:
    if numero > 0:
        contador_positivos += 1

print("Os números positivos da lista é:", contador_positivos)
