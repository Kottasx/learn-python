import random
import string

def gerador_de_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

senha = gerador_de_senha(25)
print('Aqui esta a senha de 25 digitos gerada:', senha)