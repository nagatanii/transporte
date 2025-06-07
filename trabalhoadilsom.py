#   Sistema de controle de transporte: Gerenciar horários, itinerários e veículos.	
#   Data: 06/06/2025
#   Gabriel Nagatani Campos, Vinicius Garcia Moreira Madalosso, Kauan Santos Pereira 

print('------ Transporte ------')



# Biblioteca para limpar a tela e pausar o programa
import os           # usada para limpar a tela
import time         # usada para criar pausas temporais no programa

# Variáveis globais usadas em diversas funções
login1 = 0
v_escolhido = None  # Armazena o veículo escolhido pelo motorista
ve = None           # Variável auxiliar para escolha de veículo
valores = 55.00     # Valor fixo da passagem

# Dados de login para motorista
senha_motorista = '1234567'
login_motoristaa = 'kauan'

# Dados de login para administrador
senha_administrador = '7654321'
login_administradorr = 'vinicius'

# Horários de saída e chegada dos itinerários
saida = ['06:00', '07:30', '09:00', '10:30', '12:00']
chegada = ['07:30', '09:00', '10:30', '12:00', '13:30']

# Lista do carrinho de compras
carrinho = []

# Poltronas disponíveis
poltronas = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]

# Lista dos veículos
veiculos = ['Ônibus 1', 'Ônibus 2', 'Micro-ônibus', 'van']

#Lista de Rotas
rotas = [
    'Mogi > Guarulhos',
    'Mogi > São José Dos Campos',
    'Mogi > Guararema',
    'Mogi > Santos'
]


# funções


# menu do usuário comum
def m_usuario():
    while True:
        os.system('cls')    # limpa tela
        print('-----\033[1;34;40m Menu Usuário\033[m -----\n')
        print('\033[1;37;40m1. Itinerários')            # Mostrar horários
        print('\033[1;37;40m2. Comprar Passagem')       # Comprar poltronas
        print('\033[1;37;40m3. Carrinho')               # Ver poltronas compradas
        print('\033[1;31;40m4. Sair\033[m')             # Sair do menu
        
        usu = int(input('\n\033[1;37;40mDigite o número correspondente: '))

        if usu == 1: itinierarios()             # Chama a função para mostrar itinerários
        elif usu == 2: passagem()               # Função para comprar passagem
        elif usu == 3: bilhetes()               # Mostrar carrinho
        elif usu == 4: 
            print('Fechando o Programa')
            os.system('cls')
            break   # sai do menu do usuário

# autenticação para perfil de motorista.
def login_motorista():
    os.system('cls')
    print('---------LOGIN MOTORISTA---------')
    print ('\n')
    while True:

        sair = input('Digite 0 para sair ou pressione ENTER para continuar: ')
        if sair == '0':
            print('Fechando...')
            time.sleep(1)       # temporizador (dá uma pausa antes de uma ação)
            os.system('cls')
            return login()      # Retorna ao menu de login geral
        

        loginn =  input('Digite seu login: ')
        senhaa = input('Digite a sua senha: ')
        
       
        if loginn == 0:
            print('fechando...')
            login()


        if loginn == login_motoristaa and senhaa == senha_motorista:    # se o login e a senha estiverem corretos, direciona até o menu do motorista
            print ('login \033[32mcorreto!!\033[m Carregando...')
            time.sleep(3)
            m_motorista()       # Entra no menu motorista
            break
        else: print('login \033[31mincorreto!\033[m Tente outra vez')
        time.sleep(2)
        os.system('cls')
        print('---------LOGIN MOTORISTA---------')
        
# autenticação para perfil de administrador.
def login_administrador():
    os.system('cls')
    print('---------LOGIN ADMINISTRADOR---------')
    print ('\n')
    while True:

        sair = input('Digite 0 para sair ou pressione ENTER para continuar: ')
        if sair == '0':
            print('Saindo...')
            time.sleep(1)
            os.system('cls')
            return login()
        else: sair == ''
        os.system('cls')
        
        print('---------LOGIN ADMINISTRADOR---------')
        print ('\n')
        loginn =  input('Digite seu login: ')
        senhaa = input('Digite a sua senha: ')


        if loginn == login_administradorr and senhaa == senha_administrador:
            print ('login \033[32mcorreto!!\033[m Carregando...')
            time.sleep(3)
            m_admin()
            break
        else: print('login \033[31mincorreto!\033[m Tente outra vez')
        time.sleep(2)
        os.system('cls')
        print('---------LOGIN ADMINISTRADOR---------')
        print ('\n')

# menu do motorista 
def m_motorista():
    os.system('cls')
    while True:
        os.system('cls')
        print('----- Menu Motorista -----')
        print('1. Rotas Disponiveis')
        print('2. Veículos Disponiveis') 
        print('3. Sair')

        try:
            moto = int(input('Digite o número correspondente ao que Deseja: '))
        except:
            print('Digite Apenas Numeros Válidos!!')
            time.sleep(2)       # temporizador
            os.system('cls')    # limpa tela
            continue            # Volta ao início do loop para repetir o menu
        if moto == 1:
            rotas_d()
        elif moto == 2: 
            veiculos_d()
        elif moto == 3: 
            print('Fechando o Menu')
            os.system('cls')
            break               
            
# escolha de veículo pelo motorista
def veiculos_d(): 
    os.system('cls')            #limpa tela
    global v_escolhido, ve      # puxa as variavéis que estão fora para dentro da função

    if v_escolhido is not None: # se v_escolhido for verdadeiro ou true, aparecerá está mensagem dizendo, que o veiculo está armazenado.
        print('---------- Menu veículos ----------')
        print(f"\nVocê já escolheu o veículo: {v_escolhido}")
        print("\nNão é possível escolher novamente.")
        time.sleep(3)   # temporizador
        return          # Sai da função, impedindo nova escolha de veículo

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
            return m_motorista()  
        else:
            print("Opção inválida, tente novamente.")
            continue

# exibe as rotas
def rotas_d():
    os.system('cls')
    global v_escolhido, rotas       # Usa as variáveis globais 'v_escolhido' e 'rotas' dentro da função

    if v_escolhido is not None:     # Verifica se o motorista já escolheu um veículo
        print(f'seu veiculo escolhido foi {v_escolhido} ')
        index = None                # Inicializa a variável 'index' com None
        try:
            index = veiculos.index(v_escolhido)
        except ValueError:
            index = None

        if index is not None and index < len(rotas):
            print(f'A sua rota é: {rotas[index]}')
        else:
            print('Rota não disponível para este veículo.')
    else:
        print('Você ainda não escolheu um veículo.')

    print('-------ROTAS DISPONIVEIS-------')
    for i, rota in enumerate(rotas):
        print(f'Rota {veiculos[i]}: {rota}')

    while True:
        tecla = input('Digite 0 para voltar ao menu...: ')
        if tecla.strip() == '0':
            return m_motorista()
        else:
            print('tecla invalida, tente novamente!!')
        
# usado pelo administrador para excluir rotas.
def remover_rota():
    global rotas, veiculos
    os.system('cls')
    print('--- Remover Rota ---\n')

    if not rotas:
        print('Nenhuma rota disponível para remoção.\n')
    else:
        for i in range(min(len(rotas), len(veiculos))):
            print(f'{i + 1}. {veiculos[i]}: {rotas[i]}')

        try:
            opcao = int(input('\nDigite o número da rota que deseja remover: '))
            if 1 <= opcao <= len(rotas):
                removida = rotas.pop(opcao - 1)
                veiculo_removido = veiculos.pop(opcao - 1)
                print(f'\nRota "{removida}" do veículo "{veiculo_removido}" foi removida com sucesso.')
                
                # Se o veículo removido for o escolhido pelo motorista, resetar a escolha
                global v_escolhido
                if v_escolhido == veiculo_removido:
                    v_escolhido = None
                    print('Veículo selecionado pelo motorista foi removido. A escolha foi resetada.')
            else:
                print('\nOpção inválida.')
        except ValueError:
            print('\nEntrada inválida. Digite apenas números.')

    input('\nPressione Enter para voltar ao menu...')

# menu do administrador
def m_admin():
    while True:
        os.system('cls')
        print('----- Menu Administrador -----')
        print('1. Remover Veículos')
        print('2. Remover Rotas') 
        print('3. Sair')

        try:
            adm= int(input('Digite o número correspondente: '))
        except:
            print('Digite apenas números válidos.')
            time.sleep(2)
            continue

        if adm == 1:
            remover_veiculo()
        elif adm == 2:
            remover_rota()
        elif adm == 3:  
            print('Fechando o Programa')
            os.system('cls')
            break
        else:
            print('Opção inválida.')
            time.sleep(2)

# usado pelo administrador para excluir veiculos.
def remover_veiculo():
    global veiculos, rotas
    os.system('cls')
    print('--- Remover Veículo ---\n')

    if not veiculos:
        print('Nenhum veículo disponível para remoção.\n')
    else:
        for i, v in enumerate(veiculos):
            print(f'{i + 1}. {v}')

        try:
            opcao = int(input('\nDigite o número do veículo que deseja remover: '))
            if 1 <= opcao <= len(veiculos):
                removido = veiculos.pop(opcao - 1)
                rota_removida = rotas.pop(opcao - 1)  # REMOVER a rota também!
                print(f'\nVeículo "{removido}" e rota "{rota_removida}" foram removidos com sucesso.')
                
                global v_escolhido
                if v_escolhido == removido:
                    v_escolhido = None
                    print('Veículo escolhido pelo motorista foi removido.')
            else:
                print('\nOpção inválida.')
        except ValueError:
            print('\nEntrada inválida. Digite apenas números.')

    input('\nPressione Enter para voltar ao menu...')

# menu de seleção de perfil (usuário, motorista ou administrador).
def login():
   os.system('cls')
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
    
# exibe horários de saída e chegada.
def itinierarios(): #função para mostrar os horários de saída e chegada 
    os.system('cls')
    print('----\033[1;32;40m Itinerários \033[m---\n')

    while True:
        for i in range(len(saida)): #faz a leitura da lista com os horários de saída
                
            print(f'\033[1;37;40mHorário de Saída: {saida[i]} --> Horário de Chegada: {chegada[i]}')
    
    
        opcao = input("\n\033[1;31;40mDigite 0 \033[1;37;40mpara voltar ao menu anterior: \033[m")

        if opcao == '0':
            break  # Sai do loop e retorna ao menu anterior
        else:
            print("\033[1;37;40mOpção inválida ou apenas visualização. Tente novamente.\n")
            time.sleep
            os.system('cls')

# simula a compra de passagens e adição ao carrinho.
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

# exibe o conteúdo do carrinho.
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
