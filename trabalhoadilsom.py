#   Sistema de controle de transporte: Gerenciar horários, itinerários e veículos.	
#   Data: 06/06/2025
#   Gabriel Nagatani Campos, Vinicius Garcia Moreira Madalosso, Kauan Santos Pereira 

print('------ Transporte ------')



#Biblioteca
import os
import time

#variaveis
login1 = 0

#senhas
senha_motorista = '1234567'
login_motoristaa = 'kauan'

senha_administrador = '7654321'
login_administradorr = 'vinicius'

#Listas

saida = ['06:00', '07:30', '09:00', '10:30', '12:00']
chegada = ['07:30', '09:00', '10:30', '12:00', '13:30']

#lista de compra da passagem
carrinho = []
valores = 55.00
va = 0
poltronas = [1, 2 ,3 , 4 ,5 , 6, 7, 8, 9, 10]

#veiculos
onibus1 = 0
onibus2 = 0
microonibus = 0
van = 0


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
            os.system('cls')
            break

def login_motorista():
    os.system('cls')
    print('---------LOGIN MOTORISTA---------')
    print ('\n')
    while True:
        login =  input('Digite seu login de usuário: ')
        senha = input('Digite a sua senha: ')
        if login == login_motoristaa and senha == senha_motorista:
            print ('login \033[32mcorreto!!\033[m Carregando...')
            time.sleep(3)
            return m_motorista()
        else: print('login \033[31mincorreto!\033[m Tente outra vez')
        time.sleep(2)
        os.system('cls')
        login_motorista
        

def login_administrador():
    os.system('cls')
    print('---------LOGIN ADMINISTRADOR---------')
    print ('\n')
    while True:
        login =  input('Digite seu login de usuário: ')
        senha = input('Digite a sua senha: ')
        if login == login_administradorr and senha == senha_administrador:
            print ('login \033[32mcorreto!!\033[m Carregando...')
            time.sleep(3)
            return m_admin()
        else: print('login \033[31mincorreto!\033[m Tente outra vez')
        time.sleep(2)
        os.system('cls')
        login_administrador


def m_motorista():
    while True:
        os.system('cls')
        print('----- Menu Motorista -----')
        print('1. Veículos Disponíveis')
        print('2. Rotas Disponiveis') 
        print('3. Paradas')
        print('4. Sair')
        moto = int(input('Digite o número correspondente ao que Deseja: '))

        if moto == 1:
            veiculos_d()
        elif moto == 2: 
            rotas_d()
        elif moto == 3: 
            paradas_d()
        elif moto == 4:
            print('Fechando o Programa')
            os.system('cls')
            break
    
def veiculos_d(): 
    os.system('cls')

    v_escolhido = 0


    while True:
        if escolha_feita :
            print("\nVocê já escolheu um veículo. Não é possível escolher novamente.")
            time.sleep(2)
            break
        else:

            print('----- Menu veículos -----')
        print('1. Ônibus 1')
        print('2. Ônibus 2') 
        print('3. Micro-õnibus')
        print('4. Van')
        print('0. Sair')

        ve = int(input("Digite o numero correspondente ao veiculo Que Deseja!! "))
  
        if escolha_feita :
            print("\nVocê já escolheu um veículo. Não é possível escolher novamente.")
            time.sleep(2)
            break

        if ve == 1:
            v_escolhido = "Ônibus 1"
        elif ve == 2:
            v_escolhido = "Ônibus 2"
        elif ve == 3:
            v_escolhido = "Micro-ônibus"
        elif ve == 4:
            v_escolhido = "Van"
        elif ve == 0:
            print("Fechando o programa...")
            os.system('cls')
            break
        else:
            print("Opção inválida, tente novamente.")
            return veiculos_d()
        escolha_feita = [ve]  
        if ve:
            print(f"\nSeu veículo escolhido foi: {v_escolhido}")
            escolha_feita = True
            time.sleep(1)
            continue  # Sai do loop após uma escolha válida
        

def rotas_d():
    print

def paradas_d():
    print



def m_admin():
    while True:
        os.system('cls')
        print('----- Menu Administrador -----')
        print('1. Remover Veículos')
        print('2. Trocar Rotas') 
        print('3. Sair')

        adm= int(input('Digite o número correspondente: '))

        if adm == 1: ''
        elif adm == 2: ''
        elif adm == 3:  
            print('Fechando o Programa')
            os.system('cls')
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
            login_motorista()
        elif login1 == 3:
            login_administrador()
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
        continuar = input("\nPressione (Enter) para sair: ")
        if continuar == '':
            break



        
    
    




def alguma():
    pass
    
os.system('cls') # Limpa a tela
login()
    
    


