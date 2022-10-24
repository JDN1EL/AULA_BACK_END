
coleta_de_dados_um = input('Agora vamos prosseguir para sua conta\n''ENTER para continuar: ')
if coleta_de_dados_um == "":

    from cliente import nca
    ncl = input('Seu numero de cliente: ')
    if ncl !=0:
        nco = float(input('Ok, agora seu número de conta: '))
        if nco != 0:
            from meus_depositos import depositar
            print('Seu saldo é de:\n', depositar)
retorno = int(input('Quer voltar para nosso menu 1\n Ou já chega de navegar por hoje! 2\n'))
if retorno == 1:
    from cliente import menu
    print(menu)
if retorno == 1:
    exit