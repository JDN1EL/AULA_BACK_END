import numbers
from os import terminal_size
from random import random


sim = 1
não = 2
tres = 3
quatro = 4
cinco = 5
seis = 6
cc = True
cc = ""
dados = int(input('Quer fazer um cadastro?\n1 para SIM\n    OU \n2 para NÃO\n'))
if dados == 1:
    dados_nome = {'nome':input('Seu nome: ')}
if dados == 1:
    dados_numero = {'numero':int(input('Seu número de telefone: '))}
if dados == 1:
    dados_email = {'email':input('Seu E-mail: ')}
if dados == 1:
    dados_cpf = {'cpf':int(input('Seu CPF: '))}
    cc = input('Ok, cadastro concluido\nPressione ENTER para continuar..')
    if cc == "":
        print('Esse é o seu número de cliente\nLembrese de anotar e guardá-lo')
        import random
        total_de_listas = 1
        caractere_extra = 9
        numero_cliente = [caractere_extra*random.random() for total_de_listas in range(total_de_listas)]
        print (numero_cliente[::-1])
        nca = {'ncarmazenado':numero_cliente}#___nota:é aqui que o numero fica armazenado
if dados == 1:
    menu = int(input('Deseja ver nosso menu de opções:\n1 para SIM\n    OU \n2 para NÃO\n'))
    if menu == 1:
        submenu = input('''
        1 P/CONTA CORRENTE
        2 P/DEPÓSITOS
        3 P/EMPRÉSTIMOS
        4 P/SAQUES
        5 P/TRANSFERÊNCIAS
        6 P/ SAIR\n''')
        if submenu == 6:
            exit
        if menu == 2:
            exit
    if dados == 2:
        exit





#"""enterr = 1
#inicioum = input ('Olá, quer iniciar\n1 para iniciar\nOu qualquer outra para sair:\n')
# inicioum == enterr:
#armazenamento = {'cliente':int(input('Numero do cliente:\n')),
#        'numero':int(input('Numero da conta:\n')),
#        'emp':int(input('Valor do seu emprestimo:\n'))
#    })
#    break"""
#if armazenamento == armazenamento:
    #print(armazenamento ['cliente'],armazenamento ['numero'], armazenamento ['emp'])