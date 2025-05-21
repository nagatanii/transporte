#   Sistema de controle de transporte: Gerenciar horários, itinerários e veículos.	
#   Data: 06/06/2025
#   Gabriel Nagatani Campos, Vinicius Garcia Moreira Madalosso, Kauan Santos Pereira 

print('------ Transporte ------')



#Biblioteca
import os

#variaveis
login1 = 0




#Listas

saida = ['06:00', '07:30', '09:00', '10:30', '12:00']
chegada = ['07:30', '09:00', '10:30', '12:00', '13:30']
                                                                            #veiculos, selecionar horarios, comprar passagem, poltronas disponiveis  


#Funções
def m_usuario():
    while True:
        print('----- Menu Usuário -----')
        print('1. Itinerários')
        print('2. Comprar Passagem') 
        print('3. Meus Bilhetes')
        print('4. Sair')
        
        usu = int(input('Digite o número correspondente: '))

        if usu == 1: itinierarios()
        elif usu == 2: ''
        elif usu == 3:  ''  
        elif usu == 4: 
            print('Fechando o Programa')
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
        elif moto == 2: ''
        elif moto == 3:  ''  
        elif moto == 4: 
            print('Fechando o Programa')
            break



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
    print('---- Itinerários ----')


    for i in range(len(saida)):
            
     print(f'Horário de Saída: {saida[i]} --> Horário de Chegada: {chegada[i]}')

        
    
    

def alguma():
    None
    
    
os.system('cls') # Limpa a tela[]
login()
    
    


