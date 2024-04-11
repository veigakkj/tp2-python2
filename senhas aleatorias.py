import random
import string

def gerar_senha(tamanho=12):
   
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    caracteres = letras_maiusculas + letras_minusculas + digitos + simbolos

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha


print("Senha Aleatória:", gerar_senha())
