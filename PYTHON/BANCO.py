import pymysql.cursors
from PyQt5 import uic,QtWidgets
from time import sleep as delay

SqlConexao = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password= '',
            database = 'estacionamento',
            cursorclass= pymysql.cursors.DictCursor)

# SELECT (((saida - entrada)/100)*6) FROM carros WHERE placa ='PNL1234'; PAGAMENTO VAI SER IMPLEMENTADO

def Consultar():
    ConsultaSQL = SqlConexao.cursor()
    Consulta = ('SELECT placa FROM carros WHERE placa = %s')
    placa = input('Informe a placa do veiculo: ')
    print("#" * 10)
    print('Consultando...')
    print("#" * 10)
    delay(1.3)
    ConsultaSQL.execute(Consulta,({placa}))
    ApresentaConsulta = ConsultaSQL.fetchall()
    for Placa in ApresentaConsulta:
        print("#" * 10)
        print(f'{Placa} - PLACA CADASTRADA')
        print("#" * 10)
        op = int(input('1 - Nova Consulta | 2 - Retornar ao Menu : '))
        if op == 1:
            Consultar()
        if op == 2:
            Return()
    delay(0.4)
    print("#" * 10)
    print(f'{placa} - NAO CADASTRADA')
    print("#" * 10)
    op = int(input('1 - Nova Consulta | 2 - Retornar ao Menu : '))
    if op == 1:
        Consultar()
    if op == 2:
        Return()
    ConsultaSQL.close()
    SqlConexao.close()

def Apagar():
    ApagaSql = SqlConexao.cursor()
    Apaga = ('DELETE FROM carros WHERE placa = %s')
    placa = input("Informe a placa do veiculo:")
    ApagaSql.execute(Apaga,({placa}))
    confirma = int(input(f'Os a serem removidos são {placa} . Deseja confirmar? (1 - SIM / 2 - NÃO) '))
    if confirma == 1:
        SqlConexao.commit()
    else:
        Apagar()
    ApagaSql.close()
    SqlConexao.close()

def Modificar():
    ModificaSql = SqlConexao.cursor()
    Modifica = ("UPDATE carros SET placa = %s , modelo = %s WHERE cod =%s")
    placa = input("Informe a placa do veiculo: ")
    modelo = input("Informe o modelo do veiculo: ")
    cod = int(input("Informe o cod de registro : "))
    ModificaSql.execute(Modifica, ({placa}, {modelo},{cod}))
    confirma = int(input(f'Os dados serão atualizados {placa} e {modelo}. Deseja confirmar? (1 - SIM / 2 - NÃO) '))
    if confirma == 1:
        SqlConexao.commit()
    else:
        Modificar()
    ModificaSql.close()
    SqlConexao.close()

def Todos():
    ConsultaSQL = SqlConexao.cursor()
    Listando = ('SELECT * FROM carros')
    print('Consultando...')
    delay(1.3)
    ConsultaSQL.execute(Listando)
    ApresentaConsulta = ConsultaSQL.fetchall()
    for Placa in ApresentaConsulta:
        print(Placa)
    ConsultaSQL.close()
    SqlConexao.close()

def RegistroOperador():
    TelaCadastro.show()
    placa = TelaCadastro.Placa_Line.text()
    HoraEntrada = TelaCadastro.Entrada_Line.text()
    OperadorSql = SqlConexao.cursor()
    OperadorEntrada = ("INSERT INTO carros(placa,entrada)"
                "VALUES (%s,%s)")
    info = (str(placa),str(HoraEntrada))
    OperadorSql.execute(OperadorEntrada,info)
#    confirma = int(input(f'Os dados cadastrados são {placa} e {HoraEntrada}. Deseja confirmar? (1 - SIM / 2 - NÃO)'))
#    if confirma == 1:
    confirmar = SqlConexao.commit()
    PRINCIPAL.TelaCadastro.Confirma_btt.clicked.connect(confirmar)
    print(f'Os dados cadastrados são {placa} e {HoraEntrada}')
#       print('CADASTRANDO...')
#        delay(0.3)
#       Return()
#    else:
#        RegistroOperador()
    OperadorSql.close()
    SqlConexao.close()

def SaidaOperador():
    Consultar()
    delay(0.9)
    SaidaSql = SqlConexao.cursor()
    Saida = ("INSERT INTO carros(saida)"
                "VALUES (%s)")
    HoraSaida = input("Informe o modelo do veiculo:")
    SaidaSql.execute(Saida, ({HoraSaida},))
    confirma = int(input(f'Os dados cadastrados são {HoraSaida} . Deseja confirmar? (1 - SIM / 2 - NÃO)'))
    if confirma == 1:
        SqlConexao.commit()
        Return()
    else:
        SaidaOperador()
    SaidaSql.close()
    SqlConexao.close()

def ConsultaOperador():
    ConsultaSQL = SqlConexao.cursor()
    Consulta = ('SELECT placa,entrada FROM carros WHERE placa = %s')
    placa = input('Informe a placa do veiculo: ')
    print("#" * 10)
    print('Consultando...')
    print("#" * 10)
    delay(1.3)
    ConsultaSQL.execute(Consulta, ({placa}))
    ApresentaConsulta = ConsultaSQL.fetchall()
    for Placa in ApresentaConsulta:
        print("#" * 10)
        print(f'{Placa} - PLACA CADASTRADA')
        print("#" * 10)
        op = int(input('1 - Nova Consulta | 2 - Retornar ao Menu : '))
        if op == 1:
            Consultar()
        if op == 2:
            Return()
    delay(0.4)
    print("#" * 10)
    print(f'{placa} - NAO CADASTRADA')
    print("#" * 10)
    op = int(input('1 - Nova Consulta | 2 - Retornar ao Menu : '))
    if op == 1:
        Consultar()
    if op == 2:
        Return()
    ConsultaSQL.close()
    SqlConexao.close()

def Return():
    import OPERADOR
    OPERADOR.Menu()