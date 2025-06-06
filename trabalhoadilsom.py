#   Sistema de controle de transporte: Gerenciar horários, itinerários e veículos.	
#   Data: 06/06/2025
#   Gabriel Nagatani Campos, Vinicius Garcia Moreira Madalosso, Kauan Santos Pereira 

print('------ Transporte ------')



#Biblioteca
import os
import time

#variaveis
login1 = 0
v_escolhido = None
ve = None
valores = 55.00
va = 0

#Senhas
senha_motorista = '1234567'
login_motoristaa = 'kauan'

senha_administrador = '7654321'
login_administradorr = 'vinicius'

#Lista de horarios 

saida = ['06:00', '07:30', '09:00', '10:30', '12:00']
chegada = ['07:30', '09:00', '10:30', '12:00', '13:30']

#lista de compra da passagem
carrinho = []
poltronas = [1, 2 ,3 , 4 ,5 , 6, 7, 8, 9, 10]

#Lista de veiculos
veiculos = ['Ônibus 1', 'Ônibus 2', 'Micro-ônibus', 'van']


#Funções
def m_usuario():
    while True:
        os.system('cls')
        print('-----\033[1;34;40m Menu Usuário\033[m -----\n')
        print('\033[1;37;40m1. Itinerários')
        print('\033[1;37;40m2. Comprar Passagem') 
        print('\033[1;37;40m3. Carrinho')
        print('\033[1;31;40m4. Sair\033[m')
        
        usu = int(input('\n\033[1;37;40mDigite o número correspondente: '))

        if usu == 1: itinierarios()
        elif usu == 2: passagem()
        elif usu == 3: bilhetes() 
        elif usu == 4: 
            print('Fechando o Programa')
            os.system('cls')
            break

def login_motorista():
    os.system('cls')
    print('---------LOGIN MOTORISTA---------')
    print ('\n')
    while True:
        login =  input('Digite seu login: ')
        senha = input('Digite a sua senha: ')
        if login == login_motoristaa and senha == senha_motorista:
            print ('login \033[32mcorreto!!\033[m Carregando...')
            time.sleep(3)
            m_motorista()
        else: print('login \033[31mincorreto!\033[m Tente outra vez')
        time.sleep(2)
        os.system('cls')
        login_motorista()
        

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
        print('1. Rotas Disponiveis')
        print('2. Veículos Disponiveis') 
        print('3. Paradas')
        print('4. Sair')

        try:
            moto = int(input('Digite o número correspondente ao que Deseja: '))
        except:
            print('Digite Apenas Numeros Válidos!!')
            time.sleep(2)
            os.system('cls')
            continue
        if moto == 1:
            rotas_d()
        elif moto == 2: 
            veiculos_d()
        elif moto == 3: 
            paradas_d()
        elif moto == 4:
            print('Fechando o Menu')
            os.system('cls')
            login()
            break
    
def veiculos_d(): 
    os.system('cls') #limpa tela
    global v_escolhido, ve # puxa as variavéis que estão fora para dentro da função

    if v_escolhido is not None: # se v_escolhido for verdadeiro ou true, aparecerá está mensagem dizendo, que o veiculo está armazenado.
        print('---------- Menu veículos ----------')
        print(f"\nVocê já escolheu o veículo: {v_escolhido}")
        print("\nNão é possível escolher novamente.")
        time.sleep(3)
        return

    while True:

        print('----- Menu veículos -----')
        print('1. Ônibus 1')
        print('2. Ônibus 2') 
        print('3. Micro-onibus')
        print('4. Van')
        print('0. Sair')
         
        try:                    # Tenta executar o código
            ve = int(input("Digite o numero correspondente ao veiculo Que Deseja:  "))
        except:                 # Se der algum erro no código acima (por exemplo, se o usuário digitar letras), o programa não trava. Em vez disso, executa este bloco aqui.
            print("Por favor, digite apenas números válidos.")
            time.sleep(2) # Tempo para realizar a ação
        
        if ve == 1:
            v_escolhido = veiculos[0]
        elif ve == 2:
            v_escolhido = veiculos[1]
        elif ve == 3:
            v_escolhido = veiculos[2]
        elif ve == 4:
            v_escolhido = veiculos[3]
        elif ve == 0:
            print("Fechando o programa...")
            os.system('cls')
            break
        else:
            print("Opção inválida, tente novamente.")
            return veiculos_d()
        
        
        if ve:
            print(f"\nSeu veículo escolhido foi: {v_escolhido}")
            time.sleep(1)
            return  
        else:
            print("Opção inválida, tente novamente.")
            continue

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

        if adm == 1: remover_veiculo()
        elif adm == 2: ''
        elif adm == 3:  
            print('Fechando o Programa')
            os.system('cls')
            break
            
def remover_veiculo():
    os.system('cls')
    print('--- Remover Veículo ---\n')
    
    if not veiculos:  #Verifica se a lista veiculos está vazia
        print('Nenhum veículo disponível para remoção.\n')
    else:
        for i, v in enumerate(veiculos):
            print(f'{i + 1}. {v}')
        try:
            opcao = int(input('\nDigite o número do veículo que deseja remover: '))
            if 1 <= opcao <= len(veiculos):
                removido = veiculos.pop(opcao - 1)
                print(f'\n{removido} foi removido com sucesso.')
            else:
                print('\nOpção inválida.')
        except ValueError:
            print('\nEntrada inválida. Digite apenas números.')

    input('\nPressione Enter para voltar ao menu...')

def login():
   while True: 
    
        print('----\033[1;32;40mSelecione o Seu Perfil\033[m----')
        print('\033[1;37;40m1. Usuário')
        print('\033[1;37;40m2. Motorista')
        print('\033[1;37;40m3. Administrador')
        print('\033[1;31;40m4. Sair\033[m')

        try:
            login1 = int(input('\n\033[1;37;40mDigite o Número correspondente: '))
        except:
            print('\n')
            print(f"Digite Apenas Numeros Válidos!!")
            time.sleep(2)
            os.system('cls')
            continue
        

        if login1 == 1:
            m_usuario() #interface do usuário 
        elif login1 == 2:
            login_motorista()
        elif login1 == 3:
            login_administrador()
        elif login1 == 4:
            print('Fechando...')
            break 
        else:
            print('Nenhuma Correspondência, Digite Novamente!')
            time.sleep(1)
            os.system('cls')
            login()

    

def itinierarios(): #função para mostrar os horários de saída e chegada 
    os.system('cls')
    print('----\033[1;32;40m Itinerários \033[m---\n')

    while True:
        for i in range(len(saida)): #faz a leitura da lista com os horários de saída
                
            print(f'\033[1;37;40mHorário de Saída: {saida[i]} --> Horário de Chegada: {chegada[i]}')
    
    
        opcao = input("\n\033[1;31;40mDigite 0 \033[1;37;40m\033 para voltar ao menu anterior: \033[m")

        if opcao == '0':
            break  # Sai do loop e retorna ao menu anterior
        else:
            print("\033[1;37;40mOpção inválida ou apenas visualização. Tente novamente.\n")
            time.sleep
            os.system('cls')

    
def passagem(): #função para colocar poltronas no carrinho, e tambem listar quais estão disponiveis 
    os.system('cls')
    while True:
        print('---- \033[1;32;40mCompra do Bilhete de Embarque\033[m ----\n')

        if not poltronas: 
            print("\033[1;31;40mTodas as poltronas estão ocupadas.")
            break

        print('----- \033[1;30;42mPoltronas Disponíveis\033[m -----')
        for p in poltronas:
            print(f'\033[1;37;40mPoltrona: {p}')

        print('\n----\033[1;37;40m Valor Unítario da Passagem:\033[m \033[1;30;42mR$ 55,00\033[m ----\n')
        escolha = int(input('\033[1;37;40mDigite o número da poltrona desejada:'))
        
        if escolha in poltronas: 
            poltronas.remove(escolha)
            carrinho.append({'poltrona': escolha, 'valor': valores})
            print(f'\n\033[1;37;40mPoltrona {escolha} adicionada ao carrinho.')
        else:
            print("\nPoltrona \033[1;30;41m indisponível ou inválida.\033[m")
        
        continuar = input("\n\033[1;37;40mDeseja escolher outra poltrona? (s/n): ").lower() #transforma a string em minusculo para não dar erro
        if continuar != 's':
            break

def bilhetes(): #função para mostrar as poltronas adicionadas ao carrinho
    os.system('cls')
    while True:
        total = 0
        print('----- \033[1;32;40mSeu Carrinho\033[m -----')
        for item in carrinho:
            print(f"\033[1;37;40mPoltrona {item['poltrona']} - R$ {item['valor']:.2f}")
            total += item['valor']

        print(f"\n\033[1;37;40mTotal:\033[m \033[1;30;42mR$ {total:.2f}\033[m")
        continuar = input("\nPressione (Enter) para sair: ")
        if continuar == '':
            break



os.system('cls') # Limpa a tela
login()
