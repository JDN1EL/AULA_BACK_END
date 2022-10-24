from ast import Str


um = 1
dois = 2
inicio = int(input('Olá! bem vindo(a)!\nPara seu cadastro pressione 1 se não, pressione 2\n'))

from cliente import dados, submenu, o_menu
import conta_corrente        
o_menu()

if inicio == dois:
    exit
#teste