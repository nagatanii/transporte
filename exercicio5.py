#Elaborar um programa que lê um número N inteiro maior que 2
#(caso N não for maior que 2 deve solicitar outro número). Logo após o programa deve exibir o quadrado e o cubo de 2 até N.
import math

while True: 
    num = int(input('Digite um Número maior que 2: '))
    
    if num > 2:
        quadrado = num ** 2
        cubo = num ** 3

    
    print(f'{quadrado} , {cubo}')
         




