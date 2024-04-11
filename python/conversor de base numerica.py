def decimal_para_binario(numero):
    
    if numero == 0:
        return "0"  

    binario = ""
    while numero > 0:
        resto = numero % 2  
        binario = str(resto) + binario  
        numero //= 2  
    return binario


numero_decimal = int(input("Digite um número decimal para converter para binário: "))
numero_binario = decimal_para_binario(numero_decimal)
print("O número binário equivalente é:", numero_binario)