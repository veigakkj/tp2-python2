
def condicao_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


numeros_filtrados = list(filter(condicao_par, numeros))


print("Números pares na lista original:", numeros_filtrados)
