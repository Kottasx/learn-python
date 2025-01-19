# Mensagem de boas vindas:
print('Seja bem-vindo(a) a calculadora!')

# Tabela de Valores:
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

# Mensagens de sobre metodos de calculo:
print('Selecione o metodo de calculo.')
print('1 - Soma (+)')
print('2 - Subtração (-)')
print('3 - Multiplicação (x)')
print('4 - Divisão (:)')

# Funções:
operação = input('Digite o numero desejado: ')

if operação == '1':
  resultado = num1 + num2
  print(f'[resultado]: {num1} + {num2} = {resultado}')

elif operação == '2':
  resultado = num1 - num2
  print(f'[resultado]: {num1} - {num2} = {resultado}')

elif operação == '3':
  resultado = num1 * num2
  print(f'[resultado]: {num1} * {num2} = {resultado}')

elif operação == '4':
  if num1 != 0:
    resultado = num1 / num2 # Não entendi o que cê tava querendo fazer com um input() aqui então eu tirei
    print(f'Resultado final: {num1} / {num2} = {resultado}')
  else:
    print('Divisão por zero é não é possivel!')

else:
  print('Operação invalida!')


# Adeus:
print('Obrigado por utilizar a calculadora!.')

# --- Correção de erros ---:
# 1. O código não estava indentado corretamente.
  # A indentação é um pequeno espaço que fica no inicio de cada linha de código, é ela que define o bloco de código.
# 2. Toda vez que for usar um if, elif, else, while, for, def, class, etc, você deve colocar dois pontos (:) no final da linha.
# 3. O "else" é usado apenas uma vez e por último, ele é a condição final que roda caso as outras não rodarem.
# 4. Toda vez que querer usar {} dentro de uma string, você deve colocar um "f" antes da string, senão não funciona.

# 5. Alterei o texto de alguns inputs pra deixar melhor a estética.
