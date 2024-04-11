
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros_primos = []

for numero in range(1, 101):
    if eh_primo(numero):
        numeros_primos.append(numero)

print("Lista de números primos de 1 a 100:")
print(numeros_primos)
