#03 - O Amontada Valley entregou os cartões de acesso para os alunos. 
#A senha inicial, informada foi gerada automaticamente a partir da data
#de nascimento do aluno
#('dd/mm/aaaa') do seguinte modo:
#mm'@'dd(invertido) + '%' + dd'&'mm(invertido) + ''+aaaa
#Exemplo: Data de nascimento: 12/04/2002
#04@21%12&401995
#Escreva uma função que receba o dia, mês e ano de nascimento de um aluno 
#e retorne sua senha 
#de acordo com as regras acima.
from random import Random


enter = 1
#dados = [] ____________________________________________________________________________________________Inicialmente ia trrabalhar com listas e tuplas mas não foi necessário:')
d = int(input('Ok vamos fazer sua senha\n1 PARA CONTINUAR..\nOU QUALQUER OUTRA PARA SAIR:\n'))  #|| |
if d == enter:#                                                                                  || |
    dn = input('Belezinha, agora dia de nascimento: ')#                                          || |
    #dados.append(dn)____________________________________________________________________________|| |
    if dn != 1:#                                                                                  | |
        mm = input('Belezinha, agora o mês: ')#                                                   | |
        #dados.append(mm)_________________________________________________________________________| |
        if mm != 1:#                                                                                |
            aa = input('O ano em que nasceu: ')#                                                    |
           # dados.append(aa)_______________________________________________________________________|
            if aa != 1:
                print('Sua senha gerada foi:\n')
                print(mm + '@' + dn[::-1] + '%' + dn + '&' + mm[::-1] + aa)
else:#________________________________________________________________________________Essa interação de início e saida é a gambiarra do dia
    exit