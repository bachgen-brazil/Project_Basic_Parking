from PyQt5 import uic,QtWidgets
import pymysql.cursors

SqlConexao = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password= '',
            database = 'estacionamento',
            )
#Gerando Aplicação
app = QtWidgets.QApplication([])

#Carregar Arquivos (App)
TelaOperador = uic.loadUi('tela_operador.ui')
TelaCadastro = uic.loadUi('tela_cadastro.ui')
TelaConsulta = uic.loadUi('tela_consulta.ui')
TelaSaida = uic.loadUi('tela_saida.ui')
Cadastro_Confirmado = uic.loadUi('CONFIRMADO_JANELA.ui')
Consulta_Localizado = uic.loadUi('CONSULTA_LOCALIZADO.ui')
Consulta_N_Localizado = uic.loadUi('CONSULTA_NLOCALIZADO.ui')


#Tela Cadastro
def Tela_Cadastro():
    TelaCadastro.show()
    TelaCadastro.Confirma_btt.clicked.connect(CADASTRO)
def CADASTRO():
    placa = TelaCadastro.Placa_Line.text()
    HoraEntrada = TelaCadastro.Entrada_Line.text()
    OperadorSql = SqlConexao.cursor()
    OperadorEntrada = ("INSERT INTO carros(placa,entrada)"
                       "VALUES (%s,%s)")
    info = (str(placa),str(HoraEntrada))
    OperadorSql.execute(OperadorEntrada, info)
    SqlConexao.commit()
    Cadastro_Confirmado.show()

def Tela_Consulta():
    TelaConsulta.show()
    TelaConsulta.ConfirmaC_btt.clicked.connect(CONSULTA)
def CONSULTA():
    placaC = TelaConsulta.PlacaC_Line.text()
    ConsultaSQL = SqlConexao.cursor()
    Consulta = ('SELECT placa FROM carros WHERE placa = %s')
    infoC = str(placaC)
    ConsultaSQL.execute(Consulta, infoC)
    valor = ConsultaSQL.fetchall()
    for L in valor:
        Consulta_Localizado.tableWidget.Item(L)

    Consulta_N_Localizado.show()

    ConsultaSQL.close()
    SqlConexao.close()

#FALTA IMPLEMENTAR
def Tela_Saida():
    TelaSaida.show()
    # Botoes Tela Saida


#Botoes Tela Operação
TelaOperador.Ent_BTT.clicked.connect(Tela_Cadastro)
TelaOperador.Cons_BTT.clicked.connect(Tela_Consulta)
TelaOperador.Sai_BTT.clicked.connect(Tela_Saida)

#Inicializando Tela Operação
TelaOperador.show()
app.exec()

