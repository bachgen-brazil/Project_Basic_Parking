"""Criar programa para um estacionamento"""

import BANCO
from time import sleep as delay

# MENU DE CONFIGURAÇÃO.
def MenuConfig():
    print("#"*52)
    print("#"*12,"  PAINEL DE CONFIGURAÇÃO  ", "#"*12)
    print("#" * 12, " 1 - CADASTRAR CARRO         ", "#" * 12)
    print("#" * 12, " 2 - APAGAR CARRO         ", "#" * 12)
    print("#" * 12, " 3 - CONSULTAR CARRO      ", "#" * 12)
    print("#" * 12, " 4 - ATUALIZAR CARRO      ", "#" * 12)
    print("#" * 12, " 5 - LISTAR CARROS        ", "#" * 12)
    print("#" * 12, " 0 - ENCERRAR             ", "#" * 12)
    print("#"*52)
    opcao = int(input("-> "))
    if opcao == 1:
        BANCO.RegistroOperador()
        Cadastrar()
    if opcao == 2:
        Apagar()
    if opcao == 3:
        Consultar()
        if Consultar() == '':
            print('N')
    if opcao == 4:
        Atualizar()
    if opcao == 5:
        Listar()
    if opcao == 0:
        print('ATULIZANDO BANCO ....')
        delay(0.8)
        print('ENCERRANDO CONFIGURÇÃO ....')
        delay(1.2)
        BANCO.Return()

# CADASTRAR VEICULO.
def Cadastrar():
    print('Processando..')
    delay(1.1)
    print('Confirmado! Retornando ao Menu Incial..')
    delay(0.6)
    BANCO.Return()

# CONSULTAR VEICULO.
def Consultar():
    BANCO.Consultar()
    print('Retornando ao Menu Incial..')
    delay(0.6)
    MenuConfig()

# APAGAR VEICULO.
def Apagar():
    BANCO.Apagar()
    print('Processando..')
    delay(1.1)
    print('Confirmado! Retornando ao Menu Incial..')
    delay(0.6)
    MenuConfig()

# ATUALIZAR VEICULO.
def Atualizar():
    BANCO.Modificar()
    print('Processando..')
    delay(1.1)
    print('Confirmado! Retornando ao Menu Incial..')
    delay(0.6)
    MenuConfig()

def Listar():
    BANCO.Todos()


