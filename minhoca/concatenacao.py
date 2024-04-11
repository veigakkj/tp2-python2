lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()

lista_concatenada = lista1 + lista2

lista_concatenada = [int(elemento) for elemento in lista_concatenada]

lista_concatenada.sort()

print("Lista concatenada em ordem crescente:", lista_concatenada)