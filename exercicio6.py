import math

num = int(input('Digite um número entre 10 e 15: '))

while num < 10 or num > 15:
    print('Número inválido. Tente novamente.')
    num = int(input('Digite um número entre 10 e 15: '))

raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é: {raiz}')


    