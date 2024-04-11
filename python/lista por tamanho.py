def ordenar_por_tamanho(lista_palavras):
    
    return sorted(lista_palavras, key=len)


palavras = input("Digite as palavras separadas por espaço: ").split()
palavras_ordenadas = ordenar_por_tamanho(palavras)
print("Palavras organizadas por tamanho:", palavras_ordenadas)
