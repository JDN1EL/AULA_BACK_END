import cliente
coleta_de_dados_um = input('Agora vamos prosseguir para sua conta\n''ENTER para continuar: ')
ncl = input('Seu numero de cliente: ')
if ncl == cliente.nca:
    nco = int(input('Ok, agora seu número de conta: '))
    if nco == cliente.nca:
        print('Seu saldo é de:{}')