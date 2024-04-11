def fatorial(numero):
    
    if numero < 0:
        return None  
    elif numero == 0:
        return 1  
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
if resultado is not None:
    print("O fatorial de", numero, "é:", resultado)
else:
    print("Erro: Não é possível calcular o fatorial de um número negativo.")