print('exercicio 4') 

soma = 0
contador = 0 
a80 = 0 
a10 = 0


while True:
    num = int(input('Digite um Número: '))

    if num == 100:
        break

    soma = soma + num
    contador = contador + 1
    

    if num > 80:
        a80 += 1

    if num < 10:
        a10 += 1

if contador > 0:
        media = soma / contador
        print(f'Média:{media}')
        print(f'Números acima de 80:{a80}')
        print(f'Números abaixo de 10:{a10}')

