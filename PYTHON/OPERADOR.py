#PAINEL DE OPERAÇÃO
from time import sleep as delay

# MENU DE ACESSO.
def Menu():
    print("#"*47)
    print("#"*12,"        MENU         ", "#"*12)
    print("#" * 12, " 1 - ENTRADA         ", "#" * 12)
    print("#" * 12, " 2 - SAIDA           ", "#" * 12)
    print("#" * 12, " 3 - CONSULTA        ", "#" * 12)
    print("#" * 12, " 0 - ENCERRAR        ", "#" * 12)
    print("#"*47)
    opcao = int(input("-> "))
    if opcao == 1:
        import BANCO
        BANCO.RegistroOperador()
    if opcao == 2:
        import BANCO
        BANCO.SaidaOperador()
    if opcao == 3:
        import BANCO
        BANCO.ConsultaOperador()
    if opcao == 70290:
        import MENU
        MENU.MenuConfig()
    if opcao == 0:
        print('ENCERRANDO O PROGRAMA ....')
        delay(1.2)
        quit()

Menu()