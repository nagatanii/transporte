#   Sistema de controle de transporte: Gerenciar horários, itinerários e veículos.	
#   Data: 06/06/2025
#   Gabriel Nagatani Campos, Vinicius Garcia Moreira Madalosso, Kauan Santos Pereira 

print('------ Transporte ------')



#Biblioteca
import os
import time

#variaveis
login1 = 0
carrinho = []

#senhas
senha_motorista = '1234567'
login_motoriostaa = 'kauan'


#Listas

saida = ['06:00', '07:30', '09:00', '10:30', '12:00']
chegada = ['07:30', '09:00', '10:30', '12:00', '13:30']

#lista de compra da passagem
carrinho = []
valores = 55.00
va = 0
poltronas = [1, 2 ,3 , 4 ,5 , 6, 7, 8, 9, 10]
#veiculos, selecionar horarios, comprar passagem, poltronas disponiveis  


#Funções
def m_usuario():
    while True:
        os.system('cls')
        print('----- Menu Usuário -----\n')
        print('1. Itinerários')
        print('2. Comprar Passagem') 
        print('3. Carrinho')
        print('4. Sair')
        
        usu = int(input('\nDigite o número correspondente: '))

        if usu == 1: itinierarios()
        elif usu == 2: passagem()
        elif usu == 3: bilhetes() 
        elif usu == 4: 
            print('Fechando o Programa...')
            break

def login_motorista():
    os.system('cls')
    print('---------LOGIN MOTORISTA---------')
    print ('\n')
    while True:
        login =  input('Digite seu login de usuário: ')
        if login == login_motoriostaa:
            print ('login correto')
        else:
            print ('login incorreto!! ')
        senha = input('Digite a sua senha: ')
        if senha == senha_motorista:
            print ('senha correta!! Caregando....')
            time.sleep(3)
            m_motorista()
            os.system('cls')
        else:
            print ('senha incorreta!! ')
            break
        



def m_motorista():
    while True:
        print('----- Menu Motorista -----')
        print('1. Veículos Disponíveis')
        print('2. Rotas') 
        print('3. Sair')
        moto = int(input('Digite o número correspondente ao que Deseja: '))

        if moto == 1:
            itinierarios()
        elif moto == 2: 
            onibus()
        elif moto == 3: '' 
        elif moto == 4: 
            print('Fechando o Programa')
            break
    
def onibus(): 
    print('opa, só pra testar')




def m_admin():
    while True:
        print('----- Menu Administrador -----')
        print('1. Remover Veículos')
        print('2. Trocar Rotas') 
        print('3. Sair')

        adm= int(input('Digite o número correspondente: '))

        if adm == 1: itinierarios()
        elif adm == 2: ''
        elif adm == 3:  ''  
        elif adm == 4: 
            print('Fechando o Programa')
            break


def login():
   while True: 
    
        print('---- Selecione o Seu Perfil ----')
        print('1. Usuário')
        print('2. Motorista')
        print('3. Administrador')
        print('4. Sair')

        
        login1 = int(input('Digite o Número correspondente: '))

        if login1 == 1:
            m_usuario()
        elif login1 == 2:
            m_motorista()
        elif login1 == 3:
            m_admin()
        elif login1 == 4:
            print('Fechando...')
            break 
        else:
            print('Nenhuma Correspondência, Digite Novamente!')

    

def itinierarios():
    os.system('cls')
    print('---- Itinerários ----\n')

    while True:
        for i in range(len(saida)):
                
            print(f'Horário de Saída: {saida[i]} --> Horário de Chegada: {chegada[i]}')
    
    
        opcao = input("\nDigite 0 para voltar ao menu anterior: ")

        if opcao == '0':
            break  # Sai do loop e retorna ao menu anterior
        else:
            print("Opção inválida ou apenas visualização. Tente novamente.\n")

    

def passagem():
    os.system('cls')
    while True:
        print('---- Compra do Bilhete de Embarque ----\n')

        if not poltronas:
            print("Todas as poltronas estão ocupadas.")
            break

        print('----- Poltronas Disponíveis -----')
        for p in poltronas:
            print(f'Poltrona: {p}')

        print('\n---- Valor Unítario da Passagem: R$ 55,00 ----\n')
        escolha = int(input('Digite o número da poltrona desejada:'))
        
        if escolha in poltronas: 
            poltronas.remove(escolha)
            carrinho.append({'poltrona': escolha, 'valor': valores})
            print(f'\nPoltrona {escolha} adicionada ao carrinho.')
        else:
            print("\nPoltrona indisponível ou inválida.\n")
        
        continuar = input("\nDeseja escolher outra poltrona? (s/n): ").lower() #transforma a string em minusculo para não dar erro
        if continuar != 's':
            break

def bilhetes():
    os.system('cls')
    while True:
        total = 0
        print('----- Seu Carrinho -----')
        for item in carrinho:
            print(f"Poltrona {item['poltrona']} - R$ {item['valor']:.2f}")
            total += item['valor']

        print(f"\nTotal: R$ {total:.2f}")
        continuar = input("\nDeseja voltar? (s/n): ").lower()
        if continuar != 's':
            break



        
    
    




def alguma():
    pass
    
os.system('cls') # Limpa a tela
login()
    
    


